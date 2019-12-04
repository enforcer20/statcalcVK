from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import desc, func, cast, Date, distinct, union, DateTime, text, join, update, SmallInteger
from sqlalchemy import or_, and_, not_
from datetime import datetime
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Base = declarative_base()


# Customer table
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


# Item Table
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer(), nullable=False)


# Order Table
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, nullable=False)
    date_shipped = Column(DateTime())


# OrderLine Table
class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(Integer())
    order = relationship("Order", backref='order_lines')
    item = relationship("Item")


# Define dispatch order
def dispatch_order(order_id):
    # check whether order_id is valid or not
    order = session.query(Order).get(order_id)

    if not order:
        raise ValueError("Invalid order id: {}.".format(order_id))

    if order.date_shipped:
        print("Order already shipped.")
        return

    try:
        for i in order.order_lines:
            i.item.quantity = i.item.quantity - i.quantity

        order.date_shipped = datetime.now()
        session.commit()
        print("Transaction completed.")

    except IntegrityError as e:
        print(e)
        print("Rolling back ...")
        session.rollback()
        print("Transaction failed.")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add(c1)
session.add(c2)
session.new
session.commit()

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item3 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

session.new
session.commit()

o3 = Order(customer=c1)
orderline1 = OrderLine(item=i1, quantity=5)
orderline2 = OrderLine(item=i2, quantity=10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

for ol in c1.orders[0].order_lines:
    ol.id, ol.item, ol.quantity

print('-------')

for ol in c1.orders[1].order_lines:
    ol.id, ol.item, ol.quantity

result = session.query(Item).filter(Item.name.like("wa%")).order_by(desc(Item.cost_price)).all()
print("Print all items that start with wa and sort by the cost price in descending order")
for row in result:
    print("Item Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

# join
result = session.query(Customer, Order.date_placed).join(Order).all()
print("Join between Customer and Order")
for row in result:
    print(" Order placed on:", row.date_placed)

# Outer Join
result = session.query(Customer.first_name, Order.id).outerjoin(Order).all()
print("Outer Join between Customer and Order")
for row in result:
    print(" Order placed by:", row.first_name, " with Order ID:", row.id)

session.query(Customer.id, Customer.username, Order.id).join(Order).all()

# find all customers who either live in Peterbrugh or Norfolk

result = session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()
print("Find all customers who live in either Peterburgh or Norfolk")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

# find all customers whose first name is John and live in Norfolk
result = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()
print("Find all customers whose first name is john and live in norfolk")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

# find all johns who don't live in Peterbrugh

result = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all()
print("Find all customers whose first name is john and dont live in peterbrugh")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

result = session.query(Order).filter(Order.date_shipped == None).all()
print("Orders with Date Shipped as None")
for row in result:
    print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)

result = session.query(Order).filter(Order.date_shipped != None).all()
print("Orders with Date Shipped NOT as None")
for row in result:
    print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)

result = session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()
print("All Customers whose name start with Toby or Sarah")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

result = session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()
print("All Customers whose name that does NOT start with Toby or Sarah")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

result = session.query(Item).filter(Item.cost_price.between(10, 50)).all()
print("All Items whose cost price is between 10 and 50")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all()
print("All Items whose cost price is NOT between 10 and 50")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(Item).filter(Item.name.like("%r")).all()
print("All Items whose name ends with an 'r'")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(Item).filter(Item.name.ilike("w%")).all()
print("All Items whose name starts with 'w'")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(Customer).limit(2).all()
print("Printing all customers but limit them to 2")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)


# find the number of customers lives in each town

result = session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()
print("Find the number of customers living in each town")
print(result)

result = session.query(Customer.town).filter(Customer.id < 10).all()
print("Find the number of id < 10")
print(result)

result = session.query(Customer.town).filter(Customer.id < 10).distinct().all()
print("Find distinct id < 10")
print(result)

session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()

s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
s1.union(s2).all()
print("Union query")
print (s1.union(s2).all())

s1.union_all(s2).all()
print("Union all query")
print (s1.union_all(s2).all())

i = session.query(Item).get(8)
i.selling_price = 25.91
session.add(i)
session.commit()

# update quantity of all quantity of items to 60 whose name starts with 'W'

result = session.query(Item).filter(
    Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
print("Update quantity of all quantity of items to 60 whose name starts with 'W'")
print(result)
session.commit()

result = session.query(Item).filter(Item.name == 'Monitor').one()
session.delete(result)
session.commit()
print("Deleting Item name = Monitor")
print(result.name)

dispatch_order(1)
dispatch_order(2)

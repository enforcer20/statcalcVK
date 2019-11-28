from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Base = declarative_base()


Base.metadata.drop_all(engine)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer(), nullable=False)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(Integer())
    order = relationship("Order", backref='order_lines')
    item = relationship("Item")


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

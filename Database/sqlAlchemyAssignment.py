from sqlalchemy.orm import create_engine, Session
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Session = sessionmaker(bind=engine)

session = Session()



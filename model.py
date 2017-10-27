#Database Modeling
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, Float
from sqlalchemy import ForeignKey, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class CSV(Base):
    __tablename__ = 'CSVs'
    id = Column(Integer, primary_key=True)
    csv_file = Column(LargeBinary)
    csv_name = Column(String)


class User(Base):

    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    usertype = Column(String)

    def __repr__(self):
        return "<User>(name='%s', usertype='%s')>" %(self.name, self.password,\
                                                     self.usertype)

class Raw_data(Base):

    __tablename__ = "Machine"
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    date = Column(DateTime, server_default=func.now())

class Signal(Base):

    __tablename__ = "Signals"
    id = Column(Integer, primary_key=True)
    indicator = Column(Integer, ForeignKey('Indicator.id'))
    date = Column(DateTime, server_default=func.now())
    accuracy = Column(Boolean)

class Notification(Base):

    __tablename__ = "Notification"
    id = Column(Integer, primary_key=True)
    platform = Column(String)
    date = Column(DateTime, server_default=func.now())
    message = Column(String)

class Invoice(Base):

    __tablename__ = "Invoice"
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, server_default=func.now())
    paid = Column(Boolean)
    amount = Column(Float)
    date_paid = Column(DateTime)
    name = Column(String)


class Pay_Action(Base):

    __tablename__ = "Action"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, server_default=func.now())
    performed_by = Column(Integer, ForeignKey(User.id))
    invoice_acted = Column(Integer, ForeignKey(Invoice.id))

class Indicator(Base):
    __tablename__ = "Indicator"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime, server_default=func.now())

class Strategy(Base):
    __tablename__ = "Strategy"
    id = Column(Integer, primary_key=True)
    indicators = Column(Integer, ForeignKey(Indicator.id))
    name = Column(String)
    date = Column(DateTime, server_default=func.now())



engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

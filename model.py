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
"""
class Relatorios(Base):
    __tablename__ = 'Relatorios'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    csv_id = Column(Integer, ForeignKey('CSV.id'))
    download = Column(String)
"""

class Strategy_type(Base):
    __tablename__ = 'Strategy_type'
    id = Column(Integer, primary_key=True)
    trade_type = Column(Integer)

class Users(Base):

    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    usertype = Column(String)


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
    accuracy = Column(Float)

class Notification(Base):

    __tablename__ = "Notification"
    id = Column(Integer, primary_key=True)
    platform = Column(String)
    date = Column(DateTime, server_default=func.now())
    message = Column(String)

class Invoice(Base):

    __tablename__ = "Invoice"
    id = Column(Integer, primary_key=True)
    nro_invoice = Column(String)
    resp_invoice = Column(String)
    tipo = Column(String)
    dt_emissao = Column(String)
    dt_vencimento = Column(String)
    dt_pagamento = Column(String)
    fornecedor = Column(String)
    valor_invoice = Column(Float)
    dolar_provisao = Column(Float)
    dolar_pagamento = Column(Float)
    valor_pago = Column(Float)
    status = Column(String)
    observacao = Column(String)
    imposto = Column(Float)

class Contact(Base):

    __tablename__ = "Contact"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)


class Indicator(Base):
    __tablename__ = "Indicator"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime, server_default=func.now())
    value = Column(Float)

#Resetar tabela
class Strategy(Base):
    __tablename__ = "Strategy"
    id = Column(Integer, primary_key=True)
    indicator = Column(Integer, ForeignKey(Indicator.id))
    days_past = Column(Integer)
    accuracy = Column(Float)
    active = Column(Boolean)


class Action(Base):

    __tablename__ = "Action"
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, server_default=func.now())
    performed_by = Column(Integer, ForeignKey(Users.id))
    invoice_acted = Column(Integer, ForeignKey(Invoice.id))
    action_type = Column(String)
    notification_acted = Column(Integer, ForeignKey(Notification.id))
    strategy_acted = Column(Integer, ForeignKey(Strategy.id))



engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

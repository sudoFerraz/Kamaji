#Auxiliary Functions

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
import json
import hashlib
import requests
import pandas_datareader as web

from model import Users, Raw_data, Signal, Notification, Action, Indicator, Invoice, Contact, Strategy
import model



class ostools(object):
    def __init__(self):
        self.os = ""
        self.user = ""
        self.ip = ""

    def rotina_atualizacao(self, ip):
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade')

    def db_connection(self):
        engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
        Session = scoped_session(sessionmaker())
        Session.configure(bind=engine)
        session = Session
        return session

class strategy_type_handler(object):

    def update_strategy_type(self, session, newtype):
        strategy = session.query(model.Strategy_type).filter_by(id=1).first()
        strategy.type = newtype
        session.commit()
        session.flush()
        return strategy

class user_handler(object):

    def create_user(self, session, useremail, userpass, utype, username):
        #newpass = hashlib.md5(userpass).hexdigest()
        newuser = model.Users(email=useremail, password=userpass, name=username, usertype=utype)
        session.add(newuser)
        session.commit()
        session.flush()
        return newuser

    def change_password(self, session, useremail, newpass):
        newpass = hashlib.md5(newpass).hexdigest()
        found_user = session.query(model.Users).filter_by(email=useremail).first()
        if not found_user:
            return False
        else:
            if found_user.email == useremail:
                found_user.password = newpass
                session.commit()
                session.flush()
                return "senha resetada com sucesso"
            else:
                return False

    def verify_user(self, session, useremail, userpass):
        founduser = session.query(model.Users).filter_by(email=useremail).first()
        if not founduser:
            return False
        else:
            if founduser.email == useremail:
                if founduser.password == userpass:
                    return founduser
                else:
                    return False
            else:
                return False

    def delete_user(self, session, userid):
        deleteduser = session.query(model.Users).filter_by(id=userid).delete()
        session.commit()
        session.flush()

    def get_user(self, session, searchemail):
        founduser = session.query(model.Users).filter_by(email=searchemail).first()
        if not founduser:
            return False
        if founduser.email ==searchemail:
            return founduser
        else:
            return False

    def update_user_type(self, session, useremail):
        founduser = session.query(model.Users).filter_by(email=useremail).first()
        if not founduser:
            return False
        if founduser.usertype == 0:
            founduser.type = 1
        if founduser.usertype == 1:
            founduser.type = 0
        session.commit()
        session.flush()
        return founduser

    def update_user_pass(self, session, usernewpass, useremail):
        founduser = session.query(model.Users).filter_by(email=useremail).first()
        if not founduser:
            return False
        founduser.password = usernewpass
        session.commit()
        session.flush()
        return founduser

class data_handler(object):
    def create_data(self, session, data_price, data_date):
        new_data = model.Raw_data(price=data_price, date=data_date)
        session.add(new_data)
        session.commit()
        session.flush()
        return new_data

    def get_data(self, session, dataid):
        found_data = session.query(Raw_data).filter_by(id=dataid).first()
        if not found_data:
            return False
        if found_data.id == dataid:
            return found_data
        else:
            return False

    def get_daily_data(self, session, datadate):
        """Retorna lista de dados de uma determinada data"""
        found_datas = session.query(Raw_data).filter_by(date=datadate)
        for data in found_datas:
            if data.date != datadate:
                return False
        return found_datas

    def delete_data(self, session, dataid):
        found_data = session.query(Raw_data).filter_by(id=dataid).delete()
        session.commit()
        session.flush()

class signal_handler(object):
    def create_signal(self, session, signal_indicator, signal_accuracy):
        new_signal = model.Signal(indicator=signal_indicator, accuracy=signal_accuracy)
        session.add(new_signal)
        session.commit()
        session.flush()
        return new_signal

    def update_signal(self, session, signal_id, new_accuracy):
        found_signal = session.query(Signal).filter_by(id=signal_id).first()
        if not found_signal:
            return False
        elif found_signal:
            found_signal.accuracy = new_accuracy
            session.commit()
            session.flush()
            return found_signal

    def get_all_signals(self, session):
        signals = session.query(Signal).all()
        signal_list = []
        if signals == False:
            return False
        else:
            for signal in signals:
                signal_list.append(signal.indicator)
            return signal_list

    def get_signal_by_indicator(self, session, indicator_id):
        found_signal = session.query(Signal).filter_by(indicator=indicator_id).first()
        if not found_signal:
            return False
        if found_signal.indicator == indicator_id:
            return found_signal
        else:
            return False


    def get_signal(self, session, signal_id):
        found_signal = session.query(Signal).filter_by(id=signal_id).first()
        if not found_signal:
            return False
        if found_signal.id == signal_id:
            return found_signal
        else:
            return False

    def get_all_signals(self, session):
        signals = session.query(Signal)
        signals = signals.all()
        signal_list = []
        if signals == False:
            return False
        else:
            for signal in signals:
                signal_list.append(signal.indicator)
            return signal_list



    def delete_signal(self, session, signalid):
        deleted_signal = session.query(Signal).filter_by(id=signalid).delete()
        session.commit()
        session.flush()

    def get_daily_signals(self, session, signal_date):
        """Retorna lista de sinais de uma determinada data"""
        found_signals = session.query(Signal).filter_by(date=signal_date)
        for signal in found_signals:
            if signal.date != signal_date:
                return False
        return found_signals

class notification_handler(object):
    def create_notification(self, session, notification_platform,\
                             notification_message):
        new_notification = model.Notification(platform=notification_platform,\
                                              message=notification_message)
        session.add(new_notification)
        session.commit()
        session.flush()
        return new_notification

    def get_notification(self, session, notification_id):
        found_notification = session.query(Notification).filter_by\
            (id=notification_id).first()
        if not found_notification:
            return False
        if found_notification.id == notification_id:
            return found_notification
        else:
            return False

    def get_last_notification(self, session):
        last_notification = session.query(Notification).order_by(Notification.id.desc()).first()
        if not last_notification:
            return False
        else:
            return last_notification

    def get_all_notifications(self, session):
        notifications = session.query(Notification).all()
        notification_list = []
        if notifications == False:
            return False
        else:
            for notification in notifications:
                new_notification = {}
                new_notification['date'] = str(notification.date)
                new_notification['message'] = notification.message
                new_notification['indicadores'] = notification.platform
                new_notification = json.dumps(new_notification)
                notification_list.append(new_notification)
            return notification_list


    def delete_notification(self, session, notification_id):
        deleted_signal = session.query(Notification).filter_by\
            (id=notification_id).delete()
        session.commit()
        session.flush()

    def get_daily_notification(self, session, notification_date):
        """Retorna uma lista de notificacoes de uma determinada data"""
        found_notifications = session.query(Notification).filter_by\
            (date=notification_date)
        for notification in found_notifications:
            if notification.date != noitification_date:
                return False
        return found_notifications

class invoice_handler(object):
    def create_invoice(self, session, nunro_invoice, nuresp_invoice, nutipo, nudt_emissao, nudt_vencimento, nufornecedor, nuvalor_invoice, nudolar_provisao, nuobservacao):
        new_invoice = model.Invoice(nro_invoice=nunro_invoice, resp_invoice=nuresp_invoice, tipo=nutipo, dt_emissao=nudt_emissao, dt_vencimento=nudt_vencimento, fornecedor=nufornecedor, valor_invoice=nuvalor_invoice, dolar_provisao=nudolar_provisao, status='aberta', observacao=nuobservacao)
        session.add(new_invoice)
        session.commit()
        session.flush()
        return new_invoice

    def update_invoice(self, session, nunro_invoice, nuresp_invoice, nutipo, nudt_emissao, nudt_vencimento, nufornecedor, nuvalor_invoice, nudolar_provisao, nuobservacao):
        found_invoice = session.query(Invoice).filter_by(nro_invoice=nunro_invoice).first()
        found_invoice.resp_invoice = nuresp_invoice
        found_invoice.tipo = nutipo
        found_invoice.dt_emissao = nudt_emissao
        found_invoice.dt_vencimento = nudt_vencimento
        found_invoice.fornecedor = nufornecedor
        found_invoice.valor_invoice = nuvalor_invoice
        found_invoice.dolar_provisao = nudolar_provisao
        found_invoice.observacao = nuobservacao
        session.commit()
        session.flush()
        return new_invoice

    def delete_invoice(self, session, invoice_id):
        to_be_deleted_invoice = session.query(Invoice).filter_by(id=invoice_id).delete()
        session.commit()
        session.flush()

    def get_invoice(self, session, invoice_id):
        found_invoice = session.query(Invoice).filter_by(nro_invoice=invoice_id).first()
        if found_invoice.nro_invoice == invoice_id:
            new_invoice = {}
            new_invoice['nro_invoice'] = found_invoice.nro_invoice
            new_invoice['resp_invoice'] = found_invoice.resp_invoice
            new_invoice['tipo'] = found_invoice.tipo
            new_invoice['dt_emissao'] = found_invoice.dt_emissao
            new_invoice['dt_vencimento'] = found_invoice.dt_vencimento
            new_invoice['dt_pagamento'] = found_invoice.dt_pagamento
            new_invoice['fornecedor'] = found_invoice.fornecedor
            new_invoice['valor_invoice'] = found_invoice.valor_invoice
            new_invoice['dolar_provisao'] = found_invoice.dolar_provisao
            new_invoice['dolar_pagamento'] = found_invoice.dolar_pagamento
            new_invoice['valor_pago'] = found_invoice.valor_pago
            new_invoice['status'] = found_invoice.status
            new_invoice['observacao'] = found_invoice.observacao
            new_invoice = json.dumps(new_invoice)
            return new_invoice
        else:
            return False

    def set_payment(self, session, invoice_id, nudt_pagamento, nudolar_pagamento, nuvalor_pago, nuimposto):
        found_invoice = session.query(Invoice).filter_by(id=invoice_id).first()
        if found_invoice.id == invoice_id:
            found_invoice.dt_pagamento = nudt_pagamento
            found_invoice.dolar_pagamento = nudolar_pagamento
            found_invoice.valor_pago = nuvalor_pago
            found_invoice.imposto = nuimposto
            found_invoice.status = 'encerrada'
            session.commit()
            session.flush()
            return found_invoice
        else:
            return False

    def grab_invoice_id(self, session, invoice_name):
        found_invoice = session.query(Invoice).filter_by(name=invoice_name).first()
        if found_invoice.name == invoice_name:
            return found_invoice
        else:
            return False

    def get_all_open(self, session):
        invoices = session.query(Invoice)
        invoices = invoices.all()
        invoice_list = []
        if invoices == False:
            return invoice_list
        else:
            for found_invoice in invoices:
                if found_invoice.status == 'aberta':
                    new_invoice = {}
                    new_invoice['id'] = found_invoice.id
                    new_invoice['nro_invoice'] = found_invoice.nro_invoice
                    new_invoice['resp_invoice'] = found_invoice.resp_invoice
                    new_invoice['tipo'] = found_invoice.tipo
                    new_invoice['dt_emissao'] = found_invoice.dt_emissao
                    new_invoice['dt_vencimento'] = found_invoice.dt_vencimento
                    new_invoice['dt_pagamento'] = found_invoice.dt_pagamento
                    new_invoice['fornecedor'] = found_invoice.fornecedor
                    new_invoice['valor_invoice'] = found_invoice.valor_invoice
                    new_invoice['dolar_provisao'] = found_invoice.dolar_provisao
                    new_invoice['dolar_pagamento'] = found_invoice.dolar_pagamento
                    new_invoice['valor_pago'] = found_invoice.valor_pago
                    new_invoice['status'] = found_invoice.status
                    new_invoice['observacao'] = found_invoice.observacao
                    new_invoice = json.dumps(new_invoice)
                    invoice_list.append(new_invoice)
            return invoice_list


    def get_all_closed(self, session):
        invoices = session.query(Invoice)
        invoices = invoices.all()
        invoice_list = []
        if invoices == False:
            return invoice_list
        else:
            for invoice in invoices:
                if invoice.status == 'encerrada':
                    new_invoice = {}
                    new_invoice['id'] = invoice.id
                    new_invoice['nro_invoice'] = invoice.nro_invoice
                    new_invoice['resp_invoice'] = invoice.resp_invoice
                    new_invoice['tipo'] = invoice.tipo
                    new_invoice['dt_emissao'] = invoice.dt_emissao
                    new_invoice['dt_vencimento'] = invoice.dt_vencimento
                    new_invoice['dt_pagamento'] = invoice.dt_pagamento
                    new_invoice['fornecedor'] = invoice.fornecedor
                    new_invoice['valor_invoice'] = invoice.valor_invoice
                    new_invoice['dolar_provisao'] = invoice.dolar_provisao
                    new_invoice['dolar_pagamento'] = invoice.dolar_pagamento
                    new_invoice['valor_pago'] = invoice.valor_pago
                    new_invoice['status'] = invoice.status
                    new_invoice['observacao'] = invoice.observacao
                    new_invoice['imposto'] = invoice.imposto
                    new_invoice = json.dumps(new_invoice)
                    invoice_list.append(new_invoice)
            return invoice_list


    def get_all_invoices(self, session):
        invoices = session.query(Invoice)
        invoices = invoices.all()
        invoice_list = []
        if invoices == False:
            return False
        else:
            for found_invoice in invoices:
            	new_invoice = {}
                new_invoice['id'] = found_invoice.id
            	new_invoice['nro_invoice'] = found_invoice.nro_invoice
            	new_invoice['resp_invoice'] = found_invoice.resp_invoice
            	new_invoice['tipo'] = found_invoice.tipo
    	        new_invoice['dt_emissao'] = found_invoice.dt_emissao
    	        new_invoice['dt_vencimento'] = found_invoice.dt_vencimento
    	        new_invoice['dt_pagamento'] = found_invoice.dt_pagamento
    	        new_invoice['fornecedor'] = found_invoice.fornecedor
    	        new_invoice['valor_invoice'] = found_invoice.valor_invoice
    	        new_invoice['dolar_provisao'] = found_invoice.dolar_provisao
    	        new_invoice['dolar_pagamento'] = found_invoice.dolar_pagamento
    	        new_invoice['valor_pago'] = found_invoice.valor_pago
    	        new_invoice['status'] = found_invoice.status
    	        new_invoice['observacao'] = found_invoice.observacao
    	        new_invoice = json.dumps(new_invoice)
    	        invoice_list.append(new_invoice)
            return invoice_list




class contact_handler(object):
    def create_contact(self, session, new_name, new_email, new_phone):
        new_contact = model.Contact(name=new_name, email=new_email, phone=new_phone)
        session.add(new_contact)
        session.commit()
        session.flush()
        return new_contact

    def delete_contact(self, session, contact_email):
        found_contact = session.query(Contact).filter_by(email=contact_email).delete()
        session.commit()
        session.flush()

    def get_all_phones(self, session):
        all_contacts = session.query(Contact).all()
        if not all_contact:
            return False
        else:
            phone_list = []
            for contact in all_contacts:
                phone_list.append(contact.phone)
            return phone_list

    def get_all_emails(self, session):
        all_contacts = session.query(Contact).all()
        if not all_contacts:
            return False
        else:
            email_list = []
            for contact in all_contacts:
                email_list.append(contact.email)
            return email_list

    def get_all_contacts(self, session):
        found_contact = session.query(Contact).all()
        contact_list = []
        for contact in found_contact:
            new_contact = {}
            new_contact['name'] = contact.name
            new_contact['email'] = contact.email
            new_contact['phone'] = contact.phone
            contact_list.append(json.dumps(new_contact))
        return contact_list

class action_handler(object):
    def create_action(self, session, action_amount, action_date, action_user):
        new_action = model.Action(amount=action_amount, date=action_date, \
                                  performed_by=action_user)
        session.add(new_action)
        session.commit()
        session.flush()
        return new_action

    def get_action(self, session, action_id):
        found_action = session.query(Action).filter_by(id=action_id).first()
        if not found_action:
            return False
        if found_action.id == action_id:
            return found_action
        else:
            return False

    def delete_action(self, session, action_id):
        deleted_action = session.query(Action).filter_by(id=action_id).delete()
        session.commit()
        session.flush()

    def get_daily_actions(self, session, action_date):
        """Retorna uma lista de acoes de uma determinada data"""
        found_actions = session.query(Action).filter_by(date=action_date)
        for action in found_actions:
            if action.date != action_date:
                return False
        return found_actions

class type_handler(object):
    def set_type(self, session):
        return True

class strategy_handler(object):

    def get_all(self, session):
        strategies = session.query(model.Strategy).all()
        if not strategies:
            return "erro"
        else:
            strategy_list = []
            for strategy in strategies:
                req = {}
                req['id'] = strategy.id
                req['indicator'] = strategy.indicator
                req['days_past'] = strategy.days_past
                req['accuracy'] = strategy.accuracy
                req['active'] = strategy.active
                strategy_list.append(json.dumps(req))
            return str(strategy_list).replace("'", "")


    def create_strategy(self, session, indicator_id, min_days, new_accuracy, flag):
        if flag == 1:
            flag = True
        elif flag == 0:
            flag = False
        new_strategy = model.Strategy(indicator=indicator_id, days_past=min_days, accuracy=new_accuracy, active=flag)
        session.add(new_strategy)
        session.commit()
        session.flush()
        return new_strategy

    def get_strategy_by_indicator(self, session, indicator_id):
        found_strategy = session.query(Strategy).filter_by(indicator=indicator_id).first()
        if not found_strategy:
            return False
        else:
            if found_strategy.indicator == indicator_id:
                return found_strategy
            else:
                return False

    def get_strategy_indicator_days(self, session, indicator_id):
        found_strategy = session.query(Strategy).filter_by(indicator=indicator_id).first()
        return str(found_strategy.days_past)

    def delete_strategy(self, session, indicator_id):
        deleted_strategy = session.query(Strategy).filter_by(indicator=indicator_id).delete()
        session.commit()
        session.flush()

    def update_accuracy(self, session, indicator_id, new_accuracy):
        found_strategy = session.query(Strategy).filter_by(indicator=indicator_id).first()
        if not found_strategy:
            return False
        else:
            found_strategy.accuracy = new_accuracy
            session.commit()
            session.flush()
            return found_strategy

    def update_days(self, session, indicator_id, new_min_days):
        found_strategy = session.query(Strategy).filter_by(indicator=indicator_id).first()
        if not found_strategy:
            return False
        else:
            found_strategy.days_past = new_min_days
            session.commit()
            session.flush()
            return found_strategy

    def update_flag(self, session, indicator_id, flag):
        found_strategy = session.query(Strategy).filter_by(indicator=indicator_id).first()
        if not found_strategy:
            return False
        else:
            if flag == 1:
                flag = True
            elif flag == 0:
                flag = False
            found_strategy.active = flag
            session.commit()
            session.flush()
            return found_strategy

    def update_strategy(self, session, indicator_id, new_min_days, new_accuracy):
        found_strategy = session.query(Strategy).filter_by(indicator=indicator_id).first()
        if not found_strategy:
            return False
        if found_strategy:
            found_strategy.days_past = new_min_days
            found_strategy.accuracy = new_accuracy
            session.commit()
            session.flush()
            return found_strategy


class graph_storage(object):

    def create_csv(self, session, newcsv_file, newcsv_name):
        new_csv = model.CSV(csv_name=newcsv_name, csv_file=newcsv_file)
        session.add(new_csv)
        session.commit()
        session.flush
        return new_csv

    def update_csv(self, session, updated_csv, to_be_updated_id):
    #Updating with no new name
        to_be_updated_csv = session.query(CSV).filter_by(id=to_be_updated_id).first()
        if to_be_updated_csv.id == to_be_updated_id:
            to_be_updated_.csv_file = updated_csv
            session.commit()
            session.flush
            return to_be_updated_csv
        else:
            return False

    def delete_csv(self, session, to_be_deleted):
        found_csv = session.query(CSV).filter_by(id=to_be_deleted.id).delete()
        session.commit()
        session.flush()

    def get_csv(self, session, wanted_csv):
        #Searching trough id
        found_csv = session.query(CSV).filter_by(id=wanted_csv).first()
        if found_csv.id == wanted_csv:
            return found_csv
        else:
            return False

    def get_csv_id(self, session, wanted_csv_name):
        #Searching trough name
        found_csv = session.query(CSV).filter_by(csv_name=wanted_csv_name).first()
        if found_csv.csv_name == wanted_csv_name:
            return found_csv.id
        else:
            return False




class indicator_handler(object):
    def create_indicator(self, session, indicator_name, indicator_value):
        new_indicator = model.Indicator(name=indicator_name, value=indicator_value)
        session.rollback()
        session.add(new_indicator)
        session.commit()
        session.flush()
        return new_indicator

    def get_ticker(self, session):
        r = requests.get("https://rest-demo.tradingview.com/tradingview/v1/quotes?symbols=USDBRL", \
            headers={"accept": "application/json", "authorization": "Bearer 13982897"})
        ticker = r.json()['d'][0]['v']
        return ticker


    def get_indicator(self, session, indicator_id):
        if indicator_id == 10:
            found_indicator = session.query(Indicator).filter_by(name='tv_ch').first()
            return found_indicator.value
        elif indicator_id == 7:
            found_indicator = session.query(Indicator).filter_by(name='tv_lp').first()
            return found_indicator.value
        found_indicator = session.query(Indicator).filter_by(id=indicator_id).first()
        if not found_indicator:
            return False
        if found_indicator.id == indicator_id:
            return found_indicator.value
        else:
            return False

    def delete_indicator(self, session, indicator_id):
        deleted_indicator = session.query(Indicator).filter_by(id=indicator_id).delete()
        session.commit()
        session.flush()

    def get_indicator_by_name(self, session, indicator_name):
        found_indicator = session.query(Indicator).filter_by(name=indicator_name).first()
        if not found_indicator:
            return False
        if found_indicator.name == indicator_name:
            return found_indicator
        else:
            return False

    def get_all_indicators(self, session):
        indicators = session.query(Indicator)
        indicators = indicators.all()
        indicator_list = []
        if indicators == False:
            return False
        else:
            for indicator in indicators:
                indicator_list.append(indicator.__dict__)
            return indicator_list

    def update_indicator(self, session, indicator_id, new_value):
        found_indicator = session.query(Indicator).filter_by(id=indicator_id).first()
        if not found_indicator:
            return False
        if found_indicator:
            found_indicator.value = new_value
            session.commit()
            session.flush()
            return found_indicator

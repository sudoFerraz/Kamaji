import auxiliary
import model
from send_email import SendMessage as send
from datetime import datetime, timedelta

notification_handler = auxiliary.notification_handler()
signal_handler = auxiliary.signal_handler()
session = auxiliary.ostools().db_connection()
strategy_handler = auxiliary.strategy_handler()
contact_handler = auxiliary.contact_handler()



def check_triggers():
	trigger_vector = []

	rsi_trigger = False
	macd_trigger = False
	macdh_trigger = False
	bollinger_lb_trigger = False
	bollinger_ub_trigger = False

	rsi_signal = signal_handler.get_signal_by_indicator(session, 8)
	macd_signal = signal_handler.get_signal_by_indicator(session, 1)
	macdh_signal = signal_handler.get_signal_by_indicator(session, 3)
	bollinger_ub_signal = signal_handler.get_signal_by_indicator(session, 5)
	bollinger_lb_signal = signal_handler.get_signal_by_indicator(session, 6)

	rsi_strategy = strategy_handler.get_strategy_by_indicator(session, 8)
	macd_strategy = strategy_handler.get_strategy_by_indicator(session, 1)
	macdh_strategy = strategy_handler.get_strategy_by_indicator(session, 3)
	bollinger_lb_strategy = strategy_handler.get_strategy_by_indicator(session, 5)
	bollinger_ub_strategy = strategy_handler.get_strategy_by_indicator(session, 6)


#Checking if the actual accuracy meets the strategy conditions
	if rsi_signal:
		if rsi_signal.accuracy >= rsi_strategy.accuracy:
			rsi_trigger = True
		else:
			rsi_trigger = False
	else:
		rsi_trigger = False

	if macd_signal:
		if macd_signal.accuracy >= macd_strategy.accuracy:
			macd_trigger = True
		else:
			macd_trigger = False
	else:
		macd_trigger = False

	if macdh_signal:
		if macdh_signal.accuracy >= macdh_strategy.accuracy:
			macdh_trigger = True
		else:
			macdh_trigger = False
	else:
		macdh_trigger = False

	if bollinger_ub_signal:
		if bollinger_ub_signal.accuracy >= bollinger_ub_strategy.accuracy:
			bollinger_ub_trigger = True
		else:
			bollinger_ub_trigger = False
	else:
		bollinger_ub_trigger = False

	if bollinger_lb_signal:
		if bollinger_lb_signal.accuracy >= bollinger_lb_strategy.accuracy:
			bollinger_lb_trigger = True
		else:
			bollinger_lb_trigger = False
	else:
		bollinger_lb_trigger = False


#Checking if the trigger needs to be active in strategy
	if macd_strategy.active and macd_trigger:
		trigger_vector.append(True)
	elif not macd_strategy.active:
		trigger_vector.append(True)
	else:
		trigger_vector.append(False)
	if macdh_strategy.active and macdh_trigger:
		trigger_vector.append(True)
	elif not macd_strategy.active:
		trigger_vector.append(True)
	else:
		trigger_vector.append(False)
	if rsi_strategy.active and rsi_trigger:
		trigger_vector.append(True)
	elif not rsi_strategy.active:
		trigger_vector.append(True)
	else:
		trigger_vector.append(False)
	if bollinger_lb_strategy.active and bollinger_lb_trigger:
		trigger_vector.append(True)
	elif not bollinger_lb_strategy.active:
		trigger_vector.append(True)
	else:
		trigger_vector.append(False)
	if bollinger_ub_strategy.active and bollinger_ub_trigger:
		trigger_vector.append(True)
	elif bollinger_ub_strategy.active:
		trigger_vector.append(True)
	else:
		trigger_vector.append(False)


#Check if all the strategy conditions are met
	notification = all(trigger_vector)

#If all conditions are met, start the notification process
	if notification:
		email_list = contact_handler.get_all_emails(session)
		phone_list = contact_handler.get_all_phones(session)
		contact_numbers = len(email_list)
		last_notification = notification_handler.get_last_notification(session)
		now = datetime.today()
		if now - last_notification.date > timedelta(hours=2):
			pass


		for email in email_list:
			send("algarkamaji@gmail.com", email, "testsubject", "test", "lol")




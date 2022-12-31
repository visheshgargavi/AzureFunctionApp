import datetime
import logging

import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage

def main(msg: func.ServiceBusMessage, outmsg: func.Out[str]) -> None:
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
    message = ServiceBusMessage(
       f"{msg.get_body().decode('utf-8')}",
       session_id="MySessionID",
       application_properties={'data': 'custom_data'},
       time_to_live=datetime.timedelta(seconds=30),
       label='MyLabel'
    )
    logging.info(message)
    outmsg.set(str(message))

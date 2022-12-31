import logging
import azure.functions as func


def main(queuemsg: func.QueueMessage, inputblob: bytes, outputblob: func.Out[bytes]) -> None:
    logging.info(f'Python Queue trigger function processed {len(inputblob)} bytes')
    logging.info('Python queue trigger function processed a queue item: %s',
                 queuemsg.get_body().decode('utf-8'))
    logging.info(queuemsg)
    outputblob.set(inputblob)
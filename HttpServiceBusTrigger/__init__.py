import logging

import azure.functions as func


def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    # Log the Service Bus Message as plaintext
    msg = req.get_body().decode('utf-8')
    logging.info(msg)

    logging.info("Python ServiceBus topic trigger processed message.")
    logging.info("Message Body: " + msg)
    message.set(str(msg))
    return func.HttpResponse(f"Hello, {msg}. This HTTP triggered function executed successfully.")

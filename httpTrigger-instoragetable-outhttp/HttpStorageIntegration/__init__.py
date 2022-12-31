import json
import logging

import azure.functions as func


def main(req: func.HttpRequest, messageJSON) -> func.HttpResponse:
    message = json.loads(messageJSON)
    logging.info(message)
    return func.HttpResponse(f"Table row: {messageJSON}")

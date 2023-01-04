import logging

import azure.functions as func


def main(req: func.HttpRequest,documents: func.DocumentList) -> func.HttpResponse:
    logging.info("Success!")
    logging.info(type(documents))
    return func.HttpResponse('Ok')

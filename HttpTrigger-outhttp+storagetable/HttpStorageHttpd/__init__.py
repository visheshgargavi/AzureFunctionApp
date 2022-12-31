import logging
import json
import uuid

import azure.functions as func

def main(req: func.HttpRequest, messageJSON: func.Out[str]) -> func.HttpResponse:

    name = req.params.get("name")
    sex  = req.params.get("sex")
    rowkey = str(uuid.uuid4())
    logging.info("User has been added successfully")
    data = {
        "name": name,
        "sex": sex,
        "RowKey": rowkey,
        "PartitionKey": "test"
    }
    messageJSON.set(json.dumps(data))
    if (rowkey):
        return func.HttpResponse(f"Message created with the rowkey: {rowkey}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

import logging

import azure.functions as func


def main(myblob: func.InputStream,outputBlob: func.Out[bytes]) -> None:
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    outputBlob.set(myblob.to_string())
    logging.info("Success!")   
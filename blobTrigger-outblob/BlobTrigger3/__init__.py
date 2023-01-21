import logging

import azure.functions as func


def main(myblob: func.InputStream,outputBlob: func.Out[str]) -> None:
    clear_text = myblob.read().decode('utf-8')
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"{clear_text}")
    outputBlob.set(clear_text)
    logging.info("Success!")   

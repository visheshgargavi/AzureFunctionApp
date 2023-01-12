import azure.functions as func
import json

def main(req: func.HttpRequest, todoItems: func.SqlRowList) -> func.HttpResponse:
    print('Python HTTP trigger and SQL output binding function processed a request.')

    if req.method == "GET":
        try:
            rows = list(map(lambda r: json.loads(r.to_json()), todoItems))
            parameter = req.params.get('E-mail')
            for i in rows:
                if i['E-mail'] == parameter:
                    return func.HttpResponse(
                        json.dumps(i),
                        status_code=200,
                        mimetype="application/json"
                    )
                else:
                    return func.HttpResponse(
                        json.dumps({parameter, "Not found"}),
                        status_code=202,
                        mimetype="application/json"
                    )
        except:
            rows = list(map(lambda r: json.loads(r.to_json()), todoItems))
            return func.HttpResponse(
                json.dumps(rows),
                status_code= 400,
                mimetype="application/json"
            )
    else:
        rows = list(map(lambda r: json.loads(r.to_json()), todoItems))
        return func.HttpResponse(
            json.dumps(rows),
            status_code= 400,
            mimetype="application/json"
        )
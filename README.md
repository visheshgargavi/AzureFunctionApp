# AzureFunctionApp

## configuration
- you can add the string connector in the configuration section to connect with storage account, queue namespaces etc.
- you can add env variable in configuration section and then u can pass or use in the __init__.py file
- for testing it locally you can define it in the local.settings.json and import using the same beow code

([/images/Configuration.png?raw=true "Optional Title"](https://github.com/visheshgargavi/AzureFunctionApp/issues/1#issue-1515111262))
```hcl
import os
logging.info(os.environ['variable_name']
```

## use case
```hcl
1. Trigger(http) -> output(http)
2. Trigger(blob) -> output(blob)
3. Trigger(http) -> input(storage table) -> output(http get request)
4. Trigger(http) -> output(storage table insert data fetched using get method) -> output(http)
```

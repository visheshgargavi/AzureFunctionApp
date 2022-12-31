# AzureFunctionApp

## what is azure app function?
```hcl
Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.
```

## what is binding?
```hcl
Binding to a function is a way of declaratively connecting another resource to the function; bindings may be connected as input bindings, output bindings, or both. Data from bindings is provided to the function as parameters. You can mix and match different bindings to suit your needs.
```

## what is trigger?
```hcl
Triggers cause a function to run. A trigger defines how a function is invoked and a function must have exactly one trigger. Triggers have associated data, which is often provided as the payload of the function.
```

## what is input & output?
```hcl
An input binding is the data that your function receives. An output binding is the data that your function sends. Unlike a trigger, a function can have multiple input and output bindings.
```

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

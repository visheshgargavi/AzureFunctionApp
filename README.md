# AzureFunctionApp

## What is azure app function?
```hcl
Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. 
Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date 
resources needed to keep your applications running.

1.	Serverless function (on demand like the compute will only function if the function is invoked & all the compute, storage 
and runtime will be maintained by azure we don’t have to set any parameter or anything).
2.	Machine resources on demand & taken care by azure.
3.	Zero administration, increased velocity, pay as per go, auto scaling
4.	Less code
5.	Event trigger
6.	You only pay for function invocation and only small amount for storage.
7.	The time spent in between the start of a request and the end of the request.

Limitation of serverless.
1.	Only limited to compute services
2.	Monitoring & debugging
3.	Vendor lock-in & security

Disadvantage of serverless
1. Loss control over hardware & runtime
2. Use proprietary tools of a particular cloud provider.

Performance(Cold start) : Setup time required  to set and application env up & running when invoked for the first time 
in the defined period.
Factors are:
a.	Code size (directly proportional to line of code)
b.	Language used


```

## What is binding?
```hcl
Binding to a function is a way of declaratively connecting another resource to the function; 
bindings may be connected as input bindings, output bindings, or both. 
Data from bindings is provided to the function as parameters. You can mix and match different bindings to suit your needs.
```

## What is trigger?
```hcl
Triggers cause a function to run. A trigger defines how a function is invoked and a function must have exactly one trigger. 
Triggers have associated data, which is often provided as the payload of the function.
```

## What is input & output?
```hcl
An input binding is the data that your function receives. An output binding is the data that your function sends. 
Unlike a trigger, a function can have multiple input and output bindings.
```

## To create azure function using command line

```hcl
func init
func new
func start

To start the service and collect log on local editor(Func + f5)
```

## __init__.py
- It is the file that store the function configuration what needed to be done

## function.json
- File consist of all the binding related code, name, input & output direction etc

## hosts.json
- File consists of version, retry time, security header/custom header etc.
- File can be found in app files
https://github.com/visheshgargavi/AzureFunctionApp/issues/2#issue-1515115688

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
5. Time trigger(https://github.com/visheshgargavi/AzureFunctionApp/issues/3#issue-1515117073)
```

# AzureFunctionApp

## configuration
- you can add the string connector in the configuration section to connect with storage account, queue namespaces etc.
- you can add env variable in configuration section and then u can pass or use in the __init__.py file
![Alt text]([/images/Configuration.png?raw=true "Optional Title"](https://github.com/visheshgargavi/AzureFunctionApp/issues/1#issue-1515111262))
```hcl
import os
logging.info(os.environ['variable_name']
```

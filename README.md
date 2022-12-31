# AzureFunctionApp

## configuration
- you can add the string connector in the configuration section to connect with storage account, queue namespaces etc.
- you can add env variable in configuration section and then u can pass or use in the __init__.py file
```hcl
import os
logging.info(os.environ['variable_name']
```

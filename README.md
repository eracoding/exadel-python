# exadel-python
##HomeWork 1:
Custom converter from csv to json, and from json to csv
without using csv package.
1) Implement logic using OOP
2) if csv field has more than 1 value, in json it should be list of data
3) ' ' should be replaced to " "
4) , should be added when it requires
5) result of ur formatting should pass validation in json online validator
6) please push ur output as separated file, to we can check it through online validator
Custom CSV-to-JSON and JSON-to-CSV formatter

##How to Use:
Proceed to 'CSV-converter' directory and run command:
```shell
python csv-json.py
```

##JSON structure-type:
JSON file input should be in the following form in order to perform convertion successfully:
```
{
    "Row1" : {
        "key": value
        },
    "Row2" : {
        "key": value
        }
}
```

And, similarly, the output would be in the following form:
```
{
    "Row1" : {
        "key": value
        },
    "Row2" : {
        "key": value
        }
}
```

##The end of HomeWork 1
## Seed Audit Testing Framework

### Requirements
* Python 3.9
* Pipenv
* Selenium webdriver
* Appium

### Installation
Install dependencies and activate the virtual environment
From project root, run:
```sh
pipenv install --dev
pipenv shell
```

### Executing testcases
From project root, run:

```sh
pytest
```

### Executing testcases and publish results with ZS4J
From project root, run the following command to use ZS4J Report API, a .report.json file will be generated and a new text execution will be created automatically
[`POST /testexecutions`](https://support.smartbear.com/zephyr-scale-cloud/api-docs/#operation/createTestExecution)
```sh
pytest --tm4j
```

### Executing tests and uploading results to Zephyr Scale manually
In order to instruct pytest to generate the JUnit XML results file, all that is required is to execute the tests with `--junitxml` parameter followed by the xml file name. Here is an example:

```
pytest --junitxml=output/junitxml_report.xml
```

The command line above will execute the pytest tests and generate the JUnit XML results file `output/junitxml_report.xml`. Then, this file containing the test results can be uploaded to Zephyr Scale using the following API endpoint: [`POST /automations/executions/junit`](https://support.smartbear.com/zephyr-scale-cloud/api-docs/#operation/createJUnitExecutions).

The above mentioned API accepts either a single XML file as well as a .zip file containing multiple XML files. The POST request will create a new test cycle in Zephyr Scale containing the results and will respond with the key of the created test cycle.

Below, an example using curl of how to use the API endpoint for uploading one single file:

```
curl -H "Authorization: Bearer ${TOKEN}" -F "file=@TestSuites.xml;type=application/xml" https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?projectKey="JQA"&autoCreateTestCases=true
```

Note the query parameters on the URL. The projectKey specifies what project will be used to create the test cycle. The autoCreateTestCase will create a test case using the pytest test method name when no matching test case is found.


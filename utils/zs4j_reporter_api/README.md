# Project summary
Package providing ZS4J Cloud REST API for test automation integration.
    
# Configure
In order to use ZS4J Cloud REST API, you need to configure ZS4J reporter with `ZS4J_api.configure_ZS4J_api` function first:
```python
from ZS4J_reporter_api import ZS4J_api


def my_test_run_setup(my_access_key, my_project_key):

    ZS4J_api.configure_ZS4J_api(
        api_access_key=my_access_key,
        project_key=my_project_key
    )
```
| Param          | Mandatory | Description                                                                                                                                            | Type | Example |
|----------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------|---------|
| api_access_key | Yes       | API key to access ZS4J. To get it see [Instruction](https://support.smartbear.com/ZS4J-cloud/docs/api-and-test-automation/generating-access-keys.html) | str  |         |
| project_key    | Yes       | Jira / ZS4J project prefix without trailing dash                                                                                                       | str  | QT      |

# Usage
## Test cycle
You need ZS4J test cycle where to submit test execution results.
You could create new ZS4J test cycle in your test run setup in order to use its key for test execution results submitting with `tm4_api.create_test_cycle` function:
```python
from ZS4J_reporter_api import ZS4J_api


def my_test_run_setup():

    ZS4J_test_cycle_key = ZS4J_api.create_test_cycle(
        test_cycle_name="My ZS4J test cycle"    
    )

    return ZS4J_test_cycle_key
```
| Param                | Mandatory | Description                                                            | Type | Example                              |
|----------------------|-----------|------------------------------------------------------------------------|------|--------------------------------------|
| test_cycle_name      | Yes       | Name of your test cycle                                                | str  | My ZS4J test cycle                   |
| description          | No        | Description of the test cycle outlining the scope                      | str  | Some feature test run                |
| planned_start_date   | No        | Planned start date of the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z' | str  | 2020-07-15'T'12:00:00'Z'             |
| planned_end_date     | No        | Planned end date for the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z'  | str  | 2020-07-15'T'12:30:00'Z'             |
| jira_project_version | No        | ID of the version from Jira                                            | int  | 1000                                 |
| status_name          | No        | Name of a status configured for the project                            | str  | Done                                 |
| folder_id            | No        | ID of a folder to place the test cycle within                          | int  | 10001                                |
| owner_id             | No        | Atlassian Account ID of the owner of the test cycle                    | str  | 377441B7-835D-4B08-B7F4-219E9E62C015 |

## Test execution results
With ZS4J test cycle key you can now submit test execution result. You also could use test cycle key of already existing ZS4J test cycle if you want.
Pass test cycle key and test execution results to `ZS4J_api.create_test_execution_result` function:
```python
from ZS4J_reporter_api import ZS4J_api

def my_test_teardown(tm4_test_cycle_key, ZS4J_test_case_key, execution_status):
    
    ZS4J_api.create_test_execution_result(
        test_cycle_key=tm4_test_cycle_key,
        test_case_key=ZS4J_test_case_key,
        execution_status=execution_status    
    )
```
| Param               | Mandatory | Description                                                                                                                                                                                        | Type | Example                                                                                                                                                                                                            |
|---------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_cycle_key      | Yes       | Key of ZS4J test cycle to put test execution to                                                                                                                                                    | str  | TIS                                                                                                                                                                                                                |
| test_case_key       | Yes       | Key of test case the execution applies to                                                                                                                                                          | str  | SA-T10                                                                                                                                                                                                             |
| execution_status    | Yes       | Name of the Test Execution Status                                                                                                                                                                  | str  | Pass                                                                                                                                                                                                               |
| test_script_results | No        | List of objects with test steps results: statusName (str), actualEndDate (str, yyyy-MM-dd'T'HH:mm:ss'Z'), actualResult (str). Number of objects should match to steps number in ZS4J test script.  | list | [{"statusName": "Pass", "actualEndDate": "2020-07-15'T'12:30:00'Z'", "actualResult": "This step passed"}, {"statusName": "Fail", "actualEndDate": "2020-07-15'T'12:30:10'Z'", "actualResult": "This step failed"}] |
| actual_end_date     | No        | Date test was executed. Format: yyyy-MM-dd'T'HH:mm:ss'Z'                                                                                                                                           | str  | 2020-07-15'T'12:30:00'Z'                                                                                                                                                                                           |
| environment_name    | No        | Environment assigned to the test case                                                                                                                                                              | str  | Staging                                                                                                                                                                                                            |
| execution_time      | No        | Actual execution time in milliseconds                                                                                                                                                              | int  | 121000                                                                                                                                                                                                             |
| executed_by_id      | No        | Atlassian Account ID of the user who executes the test                                                                                                                                             | str  | 377441B7-835D-4B08-B7F4-219E9E62C015                                                                                                                                                                               |
| assigned_to_id      | No        | Atlassian Account ID of the user assigned to the test                                                                                                                                              | str  | 377441B7-835D-4B08-B7F4-219E9E62C015                                                                                                                                                                               |
| comment             | No        | Comment against the overall test execution                                                                                                                                                         | str  | Test failed on step 2, check with Dev team                                                                                                                                                                         |

# Exceptions
## ZS4JConfigurationException
Raised by `ZS4J_api.configure_ZS4J_api` and `ZS4J_api.create_test_execution_result` functions if `ZS4J_api.configure_ZS4J_api` function was not called before:
```bash
ZS4J_reporter_api.ZS4J_exceptions.ZS4J_configuration_exceptions.ZS4JConfigurationException: You must configure ZS4J reporter API before calling ZS4J, call ZS4J_api.configure_ZS4J_api method first
```

## ZS4JResponseException
Raised by `ZS4J_api.configure_ZS4J_api` and `ZS4J_api.create_test_execution_result` functions if ZS4J Cloud responded with response status code different from `201 Created`:
```bash
ZS4J_reporter_api.ZS4J_exceptions.ZS4J_response_exceptions.ZS4JResponseException: Response status code: 400, response message: Bad Request
```
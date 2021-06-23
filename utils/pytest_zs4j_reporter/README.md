# Project summary
Pytest plugin which allows to upload test execution result to [ZS4J Cloud](https://support.smartbear.com/ZS4J-cloud/docs/index.html) version. Plugin works on the top of the `json-reporter` pytest plugin and `ZS4J_reporter_api` library.

## Plugin configuration

Create `pytest.ini` within your project and put the variables there (see below table)

| Param                      | Mandatory | Description                                                                                                                                            | Example                  |
|----------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| ZS4J_project_prefix        | Yes       | Jira / ZS4J project prefix without trailing dash                                                                                                       | QT                       |
| ZS4J_api_key               | Yes       | API key to access ZS4J. To get it see  [Instruction](https://support.smartbear.com/ZS4J-cloud/docs/api-and-test-automation/generating-access-keys.html)|                          |
| ZS4J_testcycle_key         | No        | ZS4J existing test cycle key. A new test cycle created if not specified                                                                                | R40                      |
| ZS4J_testcycle_prefix      | No        | Prefix for new test cycle. Default: autoreport. Full test cycle name is "<prefix> <day-month-year hh:mm:ss UTC>". e.g. "14-Jul-2020 16:41:24 UTC"      | Login autotests          |
| ZS4J_testcycle_description | No        | Description for the new test cycle. A description for the existing test cycle won't be changed                                                         | Update v14.43.136        |
| ZS4J_project_webui_host    | No        | Jira server base host. If provided will generate a link to a newly created test cycle                                                                  | klika-tech.atlassian.net |
| ZS4J_result_mapping        | No        | How to map test result - Pytest vs ZS4J. ZS4J-default (default) or pytest. see "Result mapping" section                                                | ZS4J-default             |

Example:

```ini
[pytest]
ZS4J_project_prefix = SA
ZS4J_api_key = eyJ0eXAiOiJKV1QiLCJhb
ZS4J_testcycle_key = R40
ZS4J_testcycle_prefix = login tests
ZS4J_testcycle_description = Update v14.43.136 
ZS4J_project_webui_host = grainchain.atlassian.net
```

# Usage

## Writing the tests
To be able to report your test to ZS4J your test names should follow convetion: `test_T<ZS4J test id>_the_rest_of_test_name.`
So workflow will be:
*  Create test case in ZS4J (from UI)
*  Notice it's unique id
*  Create test in pytest with ZS4J prefix in name.

Let's say in ZS4J project with project key `QT` full test key is `QT-T1234`. In this case in pytest it should be created like

```python
def test_T1234_login_as_user():
    ...test code goes here
```

## Result mapping
Pytest has test result status names different from ZS4J  
The mapping is configured via **ZS4J_result_mapping** parameter (optional)  

Possible values: ZS4J-default (default), pytest  
By default, the statuses are mapped according to the following scheme:  

 Pytest   | ZS4J         | Description
 ---------|--------------|-------------
 passed   | Pass         | 
 failed   | Fail         |
 skipped  | Not executed |
 xfailed  | Pass         | Failed, as it should
 xpassed  | Fail         | Should fail, but was passed

ZS4J test result statuses are configurable  
For more precise mapping, pytest statuses can be added to ZS4J via its UI

 Pytest   | ZS4J
 ---------|------
 passed   | Pass 
 failed   | Fail
 skipped  | Skip
 xfailed  | xFail
 xpassed  | xPass

ZS4J_result_mapping=pytest will activate this scheme  

## Metadata
It is possible to add and report additional metadata using `ZS4J_r` fixture. Currently supported only `comment`. Example:

```python
def test_T1701_my_test(ZS4J_r):
    ZS4J_r.comment = 'Here might be some comment for this test<br>second line here<br>third line here'
```

The published comment field will also contain a crash info in case if the test execution fails. Example:
```text
crash info:
path: /opt/work/ZS4J_reporter_pytest/tests/common/report_tests.py
lineno: 17
message: assert False
```
Please note that if you use ZS4J_r fixture you won't be able to run the test without enabling plugin `--ZS4J`

## How to run
Finally we're ready to run our test(s) with reporting to ZS4J. It is simple as just run pytest with `--ZS4J` option  
`--ZS4J-no-publish` flag can be used if you don't want to publish your execution results to ZS4J

```bash
pytest --ZS4J
```

## Result
* .report.json file created in CWD
* The file is overwritten each time
* Execution result is uploaded to ZS4J

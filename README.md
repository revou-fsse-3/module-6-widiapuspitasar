# Module 6 Checkpoint

## Link Documentation Postman:

Employees & Animals: https://documenter.getpostman.com/view/32968385/2sA2r6ZRAX

## Overview

Unit test for Flask and code coverage

## Test Coverage

Below is the test coverage report for the project:

```plaintext
---------- coverage: platform win32, python 3.11.8-final-0 -----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
app\__init__.py                         16      0   100%
app\controller\animal_route.py          56     19    66%
app\controller\employees_route.py       56     19    66%
app\models\animals_management.py         9      0   100%
app\models\employees.py                 10      0   100%
app\repositories\animal_repo.py         26     18    31%
app\repositories\employees_repo.py      27     19    30%
app\service\animal_service.py           28      9    68%
app\service\employees_service.py        29      9    69%
app\utils\api_response.py                3      0   100%
app\utils\database.py                    4      0   100%
--------------------------------------------------------
TOTAL                                  264     93    65%

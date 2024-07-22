Basic Framework model with playwright and python lybaries.
Topics Covered:
Sample pytest functions for automation execution.
handling pytest fixtures
Generating the html report for the execution
Grouping/tagging the functions using decorators (Ex: )
Handling test data driven approch using pandas(reading data from excel & csv)
Screen shot generation and logging is in progress.

In-Order to run all the existing pycharm methods/functions in project use below command.

Run Command in terminal : pytest -v -s --html=reports/report.html

In-Order to run specific test cases using the tagging/grouping mechanisem use below command.

Run Command in terminal : pytest -v -s -m sanity --html=reports/report.html       

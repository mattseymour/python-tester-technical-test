# Python tester - simple technical test

The aim of this repo is to be a simple technical test which will test some
basic skills of a python application tester. Take as long as you need to complete this test (but, try to take less than 90 minutes).

## Application Overview:
The program simply takes a URL and an html dom tag (a, div, form) as arguments. The application performs a GET request on the url and counts the number of occurances of a particular tag using the `BeautifulSoup.find_all` function. The number of occurances of a html dom element is then passed into a fizz buzz function. Example output of a successful run is:

    > div = 12 = fizz

## Skills tests:

* code review
* writing unit tests
* write some basic application code
* Identify an issue creating a test to identify the issue

## Important Notes:
 * Read each step of the task carefully. If you are unsure of what the question is asking email matt a.t actual-experience d.o.t com.
 * Start at step 1 of the task and work your way through each task in order.
 * Once your 90 minutes are up push all your changes to your repo
 * **For each step of the task completed create a new commit**. At the end of the test you should have a commit per task.

## Setup:
If you are using pip you can install the requirements using:

    pip install -r requirements.txt

The application can be run by running:

    python src/application.py <url> <tag>

    or

    python src/application.py # At this point it will ask you for input

    <tag> is a html dom element.

## Tasks:

1. Fork this repository.


2. At the top of the `src/application.py` file add a code comment with your name and current time.

Example:

    # Matt Seymour - 11:04am

Commit this change, and push them to github. Now create a merge request for the task.


3: The original code has not been code reviewed. In `src/application.py` at the bottom of the code (in a commend block) perform a code review listing the issues you see in the application. Commit your changes.


4: A user of this application has told you the result of 'fizz buzz' in the application output is incorrect. Write a unit test which confirms there is a problem with this function. Commit your changes.

Note: If the number is divisible by 3 and not by 5 return fizz; if the number is divisible by 5 and not 3 return buzz; if the number if divisible by 3 and 5 return fizzbuzz; else return an empty string.


5: Fix the fizz buzz function so it passes your unit test. Commit your changes.


6: The developer who wrote this code forgot unit tests, write some unit tests to backwards test the current application functionality. Commit your changes.


7: Write a unit test to test the `element_count()` function. Write this test using the mock framework so a network connection is not required on the tester machine in order to run the tests. Commit your changes.

Note: The mock framework is part of core Python3 (https://docs.python.org/3/library/unittest.mock.html); If you are using Python2 you will need to install the mock package : http://www.voidspace.org.uk/python/mock/


8: Using the code review points you raised in step 3. Write new unit test(s) which will test some of the changes you would make to the code (for example a test to check error handling). Commit your changes.


9: Now we have unit tests, improve the application code using the changed your code review from step 3. (Do not modify the unit test you created earlier). Commit your changes.


10: Push your changes to github On the existing pull request write a comment stating you are finished. Optional bonus point: write what you thought of the test.

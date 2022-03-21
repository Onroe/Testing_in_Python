#                            Testing_in_Python

# Automated Testing in Python  with Unit test

### UNIT TEST: Checks that a single component function in the right way

### INTERGRATION TEST: Checks multiple components to determine how well they fucntion with each other.

##  Execute test case 

```python
$  python test_sum.py
   Test passed
   Test passed
   
```

##  Execute test case using a test runner(unit test)

```python

$ python test_sum_unittest.py

```


## Use nose to run multiple test cases inside a folder

```python
$ pip install nose2
$ python -m nose2

```

##   Create unit tests for functions in a project

###  Create python file Testing_in_python/add/_init_.py with function that sums a list, tuple


###  Create python file Testing_in_python/test.py  to run tests

###  Execute test

```python
$ python -m unittest test

```

###  Execute multiple tests

```python
$  python -m unittest discover

```



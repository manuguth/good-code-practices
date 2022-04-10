# Python testing

To write unit tests, we will use the [pytest module](https://docs.pytest.org/en/6.2.x/).


## Simple Palindrome Example

A (failing) example is given for [palindromes](https://en.wikipedia.org/wiki/Palindrome) [inspired by [this tutorial](https://realpython.com/pytest-python-testing/)].

To run the unit tests, you need to go into the `python-testing` folder
```
cd python-testing
```
and then you can run the tests via
```
pytest -v test_palindrome.py
```

As a first exercise, please fix the unit tests by adapting the palindrome code.
Are all the tests making sense?




## Data Generation, Histogramming and Plotting

After a first warm up we want to implement a full chain from data generation, histogramming to plotting.

The three functions (classes) `generate_data`, `histogram` and `plot_histogram` are already predefined in the folder `mymodule`. You need to add now the required functionalities to these functions and write unit tests for the `generate_data` function and the `histogram` class. Write your unit tests in the `test_unit_mymodule.py` file.

As last step, you will then write an integration test, to test the full chain. This will be implemented in `integration_test_my_module.py` and then added to the gitlab CI in the `.gitlab-ci.yml` file.


If everything goes well you should be able to see the produced plot in the end via this kind of link:
https://gitlab.cern.ch/rodem-workshops/rodem-good-practices/-/jobs/artifacts/master/file/plot.pdf?job=integration_test_mymodule

You need to adapt this link matching your repository link.



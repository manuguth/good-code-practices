import pytest
import numpy as np
from mymodule import generate_data, histogram, plot_histogram

############################################
# unit tests of the generate_data function #
############################################

# check for raised errors
def test_generate_data_value_error_dist():
    assert True

def test_generate_data_type_error_seize():
    assert True

# check important values
def test_generate_data_check_size():
    assert True



########################################
# unit tests of the histogram function #
########################################

# creating dummy data
@pytest.fixture
def example_data_set():
    return np.concatenate(
        [
            np.ones(3),
            np.ones(5) * 4,
            np.ones(8) * 7,
        ]
    )

def test_histogram_one_bin(example_data_set):
    hist = histogram(1)
    counts, bins = hist(example_data_set)
    assert True
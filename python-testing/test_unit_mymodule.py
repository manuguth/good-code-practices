import pytest
import numpy as np
from mymodule import generate_data, Histogram

############################################
# unit tests of the generate_data function #
############################################


# check for raised errors
def test_generate_data_value_error_dist():
    with pytest.raises(ValueError):
        generate_data("test", 1)


def test_generate_data_type_error_seize():
    with pytest.raises(TypeError):
        generate_data("normal", 1.3)


def test_generate_data_type_error_seed():
    with pytest.raises(TypeError):
        generate_data("normal", 1, seed=1.3)


# check important values
def test_generate_data_check_size():
    assert len(generate_data("normal", 1)) == 1


def test_generate_data_check_distribution():
    mu = 10
    data = generate_data("normal", int(1e5), loc=mu)
    assert np.mean(data) == pytest.approx(mu, 0.01)


def test_generate_data_check_mu_normal():
    mu = 10
    data = generate_data("exp", int(1e5), scale=mu)
    assert np.mean(data) == pytest.approx(mu, 0.01)


def test_generate_data_check_seed_exp():
    scale = 10
    size = int(1e5)
    seed = 127
    dummy_data = np.random.default_rng(seed=seed).exponential(
            size=size, scale=scale
        )
    data = generate_data("exp", int(1e5), scale=scale, seed=seed)
    np.testing.assert_array_equal(dummy_data, data)


########################################
# unit tests of the Histogram function #
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
    hist = Histogram(1)
    expected_counts, expected_bins = (np.array([16]), np.array([1.0, 7.0]))
    counts, bins = hist(example_data_set)
    np.testing.assert_array_equal(counts, expected_counts)
    np.testing.assert_array_equal(bins, expected_bins)


def test_histogram_normed(example_data_set):
    hist = Histogram(1, normed=True)
    counts, _ = hist(example_data_set)
    assert counts == 1


def test_histogram_unc(example_data_set):
    hist = Histogram(1)
    hist(example_data_set)
    assert hist.get_unc == 4


def test_histogram_normed_unc(example_data_set):
    hist = Histogram(1, normed=True)
    hist(example_data_set)
    assert hist.get_unc == 1 / 4

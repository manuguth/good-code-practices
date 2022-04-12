"""
Generating data using a random seed and a distribution argument
"""
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def generate_data(dist: str, size: int, seed: int=None, **kwargs):
    """
    Parameters
    ----------
    dist : str
        possible distributions which are generated (either normal or exp)
    seize : int
    seed : int
        random seed to make the generation reproducable
    kwargs :
        arguments for the `normal` and `exponential` random generators from
        numpy

    Returns
    -------
    data_set : numpy histogram

    Notes
    -----
    for more information about the `normal` and `exponential` genarators see
        https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal
        https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential
    """
    logging.info("Generating %i data points for %s distribution.", size, dist)

    # generate data_set here for the 2 different distributions
    data_set = None

    logging.debug("Used the seed %i.", seed)
    return data_set

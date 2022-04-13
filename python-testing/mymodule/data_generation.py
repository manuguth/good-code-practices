"""
Generating data using a random seed and a distribution argument
"""
import logging
import numpy as np

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_data(dist: str, size: int, seed: int = None, **kwargs):
    """
    Parameters
    ----------
    dist : str
        possible distributions which are generated (either normal or exp)
    size : int
        size of generated data
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
    if dist == "normal":
        # possible kwargs: loc (mean), scale (standard deviation)
        data_set = np.random.default_rng(seed=seed).normal(size=size, **kwargs)
    elif dist == "exp":
        # possible kwargs: scale
        data_set = np.random.default_rng(seed=seed).exponential(
            size=size, **kwargs
            )
    else:
        raise ValueError(
            f"Specified '{dist}' as `dist` parameter, but only "
            "'normal' or 'exp' are supported"
        )

    logging.debug("Used the seed %i.", seed)
    return data_set

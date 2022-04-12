"""
Filling histograms with the generated data and calculate stat. uncertainties
"""
from itertools import pairwise
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Histogram:
    """
    Histogram class

    Attributes
    ----------
    binning : numpy array
        Binning of the histogram, all options which can be given to
        np.histogram
    counts : numpy array
    bin_edges : numpy array
    bincentres : numpy array

    Methods
    -------
    calc_unc:
        Calculates the statistical uncertainties per bin
    get_unc:
        Retrieving the uncertainty
    """

    def __init__(self, binning, normed=False):
        """
        Parameters
        ----------
        binning : numpy array
            Binning of the histogram, all options which can be given to
            np.histogram
        normed : bool
            norming the histogram to integral 1 (default: False)
        """
        self.binning = binning
        logging.debug("Initialised binning %s", self.binning)
        self.normed = normed
        logging.debug("Setting norm option to %s", self.normed)
        self.norm_value = None
        self.counts = None
        self.bin_edges = None
        self.unc = None

    def __call__(self, data_set):
        """
        Parameters
        ----------
        data_set : numpy array

        Returns
        -------
        counts : numpy array
        binning : numpy array
        """
        # use np.histogram here
        self.counts, self.bin_edges = (None, None)
        return self.counts, self.bin_edges

    @property
    def get_unc(self):
        """
        Retrieving the uncertainty

        Returns
        -------
        unc : numpy array
        """
        return self.unc

    def calc_unc(self):
        """
        Calculating stat. uncertainty per bin and saving it as class variable.
        """
        # calculate stat. unc. here - use Poisson unc.

        self.unc = None
        logging.debug("Uncertainties are given by %f.", self.unc)

"""Filling histograms with generated data and calculate stat. uncertainties."""
import logging
from itertools import pairwise
import numpy as np

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
        self.bincentres = None
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
        self.counts, self.bin_edges = np.histogram(data_set, self.binning)
        self.norm_value = len(data_set)
        self.calc_unc()
        if self.normed:
            self.counts = self.counts / self.norm_value
        self.bincentres = [
            (b1 + b2) / 2 for b1, b2 in pairwise(self.bin_edges)
            ]
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
        if self.normed:
            self.unc = np.sqrt(self.counts) / self.norm_value
        else:
            self.unc = np.sqrt(self.counts)

        logging.debug("Uncertainties are given by %f.", self.unc)

"""
Plotting the histograms created in the histogram step.
"""
import logging
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def plot_histogram(hist):
    """
    Parameters
    ----------
    np_hist :   numpy histogram
                a 1D numpy histogram which should be plotted
    plot_args : dict
                arguments controling the plotting style
    Saves
    -----
    plot as pdf
    """
    logging.info("Start plotting histogram.")
    fig = plt.figure(figsize=(8, 5.5), constrained_layout=True)
    axis = fig.gca()
    band_lower = hist.counts - hist.get_unc

    # add here your solution for plotting

    file_name = "histo.pdf"
    logging.info("Saved plot as %s.", file_name)
    plt.clf()

"""
Plotting the histograms created in the histogram step.
"""
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
    logging.info(f"Start plotting histogram.")
    fig = plt.figure(figsize=(8, 5.5), constrained_layout=True)
    ax = fig.gca()
    band_lower = hist.counts - hist.get_unc

    # add here your solution for plotting

    logging.info(f"Saved plot as {file_name}.")
    plt.clf()
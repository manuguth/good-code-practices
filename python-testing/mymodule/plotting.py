"""
Plotting the histograms created in the histogram step.
"""
import logging
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def plot_histogram(hist, file_name: str):
    """
    Parameters
    ----------
    hist : numpy histograma
        1D numpy histogram which should be plotted
    file_name : str
        name of the output file
    Saves
    -----
    plot as pdf
    """
    logging.info("Start plotting histogram.")
    fig = plt.figure(figsize=(8, 5.5), constrained_layout=True)
    axis = fig.gca()
    band_lower = hist.counts - hist.get_unc

    plt.hist(
        hist.bin_edges[:-1],
        hist.bin_edges,
        weights=hist.counts,
        histtype="step",
        linewidth=2.0,
        color="#1f77b4",
        stacked=False,
        fill=False,
    )
    plt.hist(
        hist.bincentres,
        bins=hist.bin_edges,
        bottom=band_lower,
        weights=hist.unc * 2,
        fill=False,
        hatch="/////",
        linewidth=0,
        edgecolor="#666666",
        label="stat. unc.",
    )
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    axis.legend(loc="upper right")
    plt.xlabel("entries", horizontalalignment="right", x=1.0)
    plt.ylabel("a.u.", horizontalalignment="right", y=1.0)

    plt.savefig(file_name, transparent=True)
    logging.info("Saved plot as %s.", file_name)
    plt.clf()

"""
Integration test bringing together generate_data, histogram and plot_histogram
"""
from mymodule import generate_data, Histogram, plot_histogram

if __name__ == "__main__":
    # generating histogram with exponential distribution
    data = generate_data("exp", int(1e3), scale=1e2)
    hist = Histogram(10, normed=True)
    hist(data)
    plot_histogram(hist, file_name="exp-hist.pdf")

    # generating histogram with normal distribution
    data_normal = generate_data(
        dist="normal", size=int(1e3), scale=1e2, loc=-4
        )
    hist_normal = Histogram(10, normed=True)
    hist_normal(data_normal)
    plot_histogram(hist_normal, file_name="normal-hist.pdf")

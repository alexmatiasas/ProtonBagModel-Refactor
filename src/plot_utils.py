import matplotlib.pyplot as plt

class PlotConfig:
    def __init__(self, xlabel=None, ylabel=None, title=None, xlim=None, ylim=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.xlim = xlim
        self.ylim = ylim

    def apply_to_ax(self, ax):
        if self.xlabel:
            ax.set_xlabel(self.xlabel)
        if self.ylabel:
            ax.set_ylabel(self.ylabel)
        if self.title:
            ax.set_title(self.title)
        if self.xlim:
            ax.set_xlim(*self.xlim)
        if self.ylim:
            ax.set_ylim(*self.ylim)
        ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
        ax.grid(True)

def plot_pressure_distribution(r, pressures, labels, colors, styles, config: PlotConfig):
    fig, ax = plt.subplots(figsize=(6, 4), dpi=200)

    for P, label, color, style in zip(pressures, labels, colors, styles):
        ax.plot(r, r**2 * P, label=label, color=color, linestyle=style)

    config.apply_to_ax(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()
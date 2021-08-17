import time

from matplotlib.ticker import MaxNLocator


class IMG:
    def __init__(self):
        self.imgx = []
        self.imgy = []

    def add(self, x, y):
        self.imgx.append(x)
        self.imgy.append(y)


def plot(plt, IM):
    plt.scatter(IM.imgx, IM.imgy)
    plt.title("Memory access trace")
    plt.xlabel("Cycle")
    plt.axes().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel("Memory Address")
    plt.axes().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.savefig(fname=f"plots/time_{time.time()}.png", dpi=600, bbox_inches="tight")

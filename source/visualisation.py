import pandas as pd
import matplotlib.pyplot as plt

def sort_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

    return sorted_dict

def plot_horizontal_bar(data, title, xlabel, ylabel, center_zero = False):
    df = pd.Series(data)

    ax = df.plot(kind='barh')

    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3)

    if center_zero:
        max_value = max(abs(df.min()), abs(df.max()))
        plt.xlim(-max_value - 2, max_value + 2)
        plt.axvline(0, linestyle='--')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.tight_layout()
    
    filename = title.lower().replace(" ", "_")
    plt.savefig(f"../docs/graphs/{filename}.png", dpi=300)

    plt.show()

def plot_bar(data, title, xlabel, ylabel):
    ax = data.plot(kind='bar')

    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()

    filename = title.lower().replace(" ", "_")
    plt.savefig(f"../docs/graphs/{filename}.png", dpi=300)

    plt.show()
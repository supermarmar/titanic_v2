import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
LINE_WIDTH = 1.5
EDGE_COLOR = "black"
WIDTH = 15
HEIGHT = 10


def set_up_plot(title: str, width: int = WIDTH, height: int = HEIGHT):
    plt.close("all")
    plt.title(title)


def export_plot(file_name: str):
    plt.savefig(file_name, transparent=False)
    plt.show()


# Continuous variables
def plot_histogram(df: pd.DataFrame, column: str, bins: int = 30, transformed: bool = False):
    color = "red" if not transformed else "orange"
    set_up_plot(f"Histogram of {column}")
    sns.histplot(
        df[column],
        bins=bins,
        kde=True,
        color=color,
        linewidth=LINE_WIDTH,
        edgecolor=EDGE_COLOR,
    )
    export_plot(f"histogram_{column}.png")


# Continuous variables
def plot_boxplot(df: pd.DataFrame, column: str, transformed: bool = False):
    color = "red" if not transformed else "orange"
    set_up_plot(f"Boxplot of {column}")
    sns.boxplot(
        x=column,
        data=df,
        linewidth=LINE_WIDTH,
        linecolor=EDGE_COLOR,
        color=color,
        saturation=0.5,
    )
    export_plot(f"boxplot_{column}.png")


# Categorical variables or Discrete numerical variables
def plot_barchart(df: pd.DataFrame, column: str, transformed: bool = False, cat_type: bool = True):
    if cat_type:
        color = "cyan" if not transformed else "magenta"
    else:
        color = "red" if not transformed else "orange"
    set_up_plot(f"Bar chart of {column}")
    sns.countplot(x=column, data=df, color=color, linewidth=LINE_WIDTH, edgecolor=EDGE_COLOR)
    export_plot(f"bar_chart_{column}.png")


def pie_chart(df: pd.DataFrame, column: str):
    set_up_plot(f"Pie chart of {column}")
    plt.pie(
        df[column].value_counts(),
        labels=df[column].value_counts().index,
        startangle=90,
        colors=sns.color_palette("husl"),
        autopct="%1.1f%%",
    )
    export_plot(f"pie_chart_{column}.png")

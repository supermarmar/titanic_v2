import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
LINE_WIDTH = 1.5
EDGE_COLOR = "black"
WIDTH = 10
HEIGHT = 5


def set_up_plot(title: str, width: int = WIDTH, height: int = HEIGHT):
    plt.title(title)
    plt.figure(figsize=(width, height))


# Continuous variables
def plot_histogram(
    df: pd.DataFrame, column: str, bins: int = 30, transformed: bool = False
):
    color = "red" if not transformed else "orange"
    sns.histplot(
        df[column],
        bins=bins,
        kde=True,
        color=color,
        linewidth=LINE_WIDTH,
        edgecolor=EDGE_COLOR,
    )
    set_up_plot(f"Histogram of {column}")


# Continuous variables
def plot_boxplot(df: pd.DataFrame, column: str, transformed: bool = False):
    color = "red" if not transformed else "orange"
    sns.boxplot(
        x=column,
        data=df,
        linewidth=LINE_WIDTH,
        linecolor=EDGE_COLOR,
        color=color,
        saturation=0.5,
    )
    set_up_plot(f"Boxplot of {column}")


# Categorical variables or Discrete numerical variables
def plot_barchart(
    df: pd.DataFrame, column: str, transformed: bool = False, cat_type: bool = True
):
    if cat_type:
        color = "cyan" if not transformed else "magenta"
    else:
        color = "red" if not transformed else "orange"
    sns.countplot(
        x=column, data=df, color=color, linewidth=LINE_WIDTH, edgecolor=EDGE_COLOR
    )
    set_up_plot(f"Bar chart of {column}")


def pie_chart(df: pd.DataFrame, column: str):
    plt.pie(
        df[column].value_counts(),
        labels=df[column].value_counts().index,
        startangle=90,
        colors=sns.color_palette("husl"),
        autopct="%1.1f%%",
    )
    set_up_plot(f"Pie chart of {column}")

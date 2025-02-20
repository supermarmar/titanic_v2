import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
LINE_WIDTH = 1.5
EDGE_COLOR = "black"
WIDTH = 10
HEIGHT = 5
PALETTE = "viridis"
SCATTER_PALLETE = "husl"


def set_up_plot(title: str, width: int = WIDTH, height: int = HEIGHT):
    plt.title(title)
    plt.figure(figsize=(width, height))


def plot_bivar_histogram(df: pd.DataFrame, cat_col: str, num_col: str, bins: int = 30):
    sns.histplot(
        data=df,
        x=num_col,
        hue=cat_col,
        bins=bins,
        kde=True,
        linewidth=LINE_WIDTH,
        edgecolor=EDGE_COLOR,
    )
    set_up_plot(f"Histogram of {num_col} by {cat_col}")


def plot_multivar_boxplot(df: pd.DataFrame, cat_col: str, num_col: str, cat_col_2: str = None):
    if cat_col_2 != None:
        sns.boxplot(
            x=cat_col,
            y=num_col,
            hue=cat_col_2,
            data=df,
            linewidth=LINE_WIDTH,
            linecolor=EDGE_COLOR,
            palette=PALETTE,
        )
        set_up_plot(f"Boxplot of {num_col} by {cat_col} and {cat_col_2}")
    else:
        sns.boxplot(
            x=cat_col,
            y=num_col,
            data=df,
            linewidth=LINE_WIDTH,
            linecolor=EDGE_COLOR,
            color="red",
        )
        set_up_plot(f"Boxplot of {num_col} by {cat_col}")


def plot_bivar_barchart(df: pd.DataFrame, x: str, hue: str):
    sns.countplot(
        x=x,
        data=df,
        hue=hue,
        linewidth=LINE_WIDTH,
        edgecolor=EDGE_COLOR,
        palette=PALETTE,
    )
    set_up_plot(f"Bar chart of {x} by {hue}")


def plot_multivar_scatterplot(df: pd.DataFrame, x_col: str, y_col: str, hue: str = None):
    if hue == None:
        sns.scatterplot(data=df, x=x_col, y=y_col)
        set_up_plot(f"Scatter plot of {x_col} and {y_col}")
    else:
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, palette=SCATTER_PALLETE)
        set_up_plot(f"Scatter plot of {x_col} and {y_col} by {hue}")


def plot_pairplot(df: pd.DataFrame, hue: str = None):
    cont_vars = list(df.select_dtypes(include=["float64"]).columns)
    if hue == None:
        sns.pairplot(df[cont_vars])
    else:
        cont_vars.append(hue)
        sns.pairplot(df[cont_vars], hue=hue, palette=SCATTER_PALLETE)


def plot_heatmap(df: pd.DataFrame):
    numeric_vars = df.select_dtypes(include=["int64", "float64", "bool"]).columns
    correlation_matrix = df[numeric_vars].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    set_up_plot("Heatmap of correlation matrix")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
LINE_WIDTH = 1.5
EDGE_COLOR = "black"
WIDTH = 15
HEIGHT = 10
PALETTE = "viridis"
SCATTER_PALLETE = "husl"


def set_up_plot(title: str, width: int = WIDTH, height: int = HEIGHT):
    plt.close("all")
    plt.title(title)


def export_plot(file_name: str):
    plt.savefig(file_name, transparent=False)
    plt.show()


def plot_bivar_histogram(df: pd.DataFrame, cat_col: str, num_col: str, bins: int = 30):
    set_up_plot(f"Histogram of {num_col} by {cat_col}")
    sns.histplot(
        data=df,
        x=num_col,
        hue=cat_col,
        bins=bins,
        kde=True,
        linewidth=LINE_WIDTH,
        edgecolor=EDGE_COLOR,
    )
    export_plot(f"histogram_{num_col}_by_{cat_col}.png")


def plot_multivar_boxplot(df: pd.DataFrame, cat_col: str, num_col: str, cat_col_2: str = None):
    if cat_col_2 != None:
        set_up_plot(f"Boxplot of {num_col} by {cat_col} and {cat_col_2}")
        sns.boxplot(
            x=cat_col,
            y=num_col,
            hue=cat_col_2,
            data=df,
            linewidth=LINE_WIDTH,
            linecolor=EDGE_COLOR,
            palette=PALETTE,
        )
        export_plot(f"boxplot_{num_col}_by_{cat_col}_and_{cat_col_2}.png")
    else:
        set_up_plot(f"Boxplot of {num_col} by {cat_col}")
        sns.boxplot(
            x=cat_col,
            y=num_col,
            data=df,
            linewidth=LINE_WIDTH,
            linecolor=EDGE_COLOR,
            color="red",
        )
        export_plot(f"boxplot_{num_col}_by_{cat_col}.png")


def plot_bivar_barchart(df: pd.DataFrame, x: str, hue: str):
    set_up_plot(f"Bar chart of {x} by {hue}")
    sns.countplot(
        x=x,
        data=df,
        hue=hue,
        linewidth=LINE_WIDTH,
        edgecolor=EDGE_COLOR,
        palette=PALETTE,
    )
    export_plot(f"bar_chart_{x}_by_{hue}.png")


def plot_multivar_scatterplot(df: pd.DataFrame, x_col: str, y_col: str, hue: str = None):
    if hue == None:
        set_up_plot(f"Scatter plot of {x_col} and {y_col}")
        sns.scatterplot(data=df, x=x_col, y=y_col)
        export_plot(f"scatter_plot_{x_col}_and_{y_col}.png")
    else:
        set_up_plot(f"Scatter plot of {x_col} and {y_col} by {hue}")
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, palette=SCATTER_PALLETE)
        export_plot(f"scatter_plot_{x_col}_and_{y_col}_by_{hue}.png")


def plot_pairplot(df: pd.DataFrame, hue: str = None):
    cont_vars = list(df.select_dtypes(include=["float64"]).columns)
    if hue == None:
        sns.pairplot(df[cont_vars])
        export_plot("pairplot.png")
    else:
        cont_vars.append(hue)
        sns.pairplot(df[cont_vars], hue=hue, palette=SCATTER_PALLETE)
        export_plot(f"pairplot_by_{hue}.png")


def plot_heatmap(df: pd.DataFrame):
    numeric_vars = df.select_dtypes(include=["int64", "float64", "bool"]).columns
    correlation_matrix = df[numeric_vars].corr()

    set_up_plot("Heatmap of correlation matrix")
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    export_plot("heatmap.png")

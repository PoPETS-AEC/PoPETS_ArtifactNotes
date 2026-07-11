import argparse


def saveFig(path, size=[4, 3]):
    plt.rcParams["figure.autolayout"] = True
    # Sane default fig size for papers
    matplotlib.rcParams["figure.figsize"] = size

    # Uses Opentype-compatible fonts
    # conferences often require this for camera ready, so if you don't do it pre-submission you'll have a nightmare at camera-ready time.
    matplotlib.rcParams["pdf.fonttype"] = 42
    matplotlib.rcParams["ps.fonttype"] = 42
    # Automatically make the directory hierarchy so I can just save figures with path names
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Makes background transparent so plots can go in slides and look good
    plt.gcf().patch.set_alpha(0)
    # Default fig size
    plt.gcf().set_size_inches(*size)
    # Make figure fill whole PDF (otherwise figs have huge margins in LaTeX
    plt.tight_layout(
        pad=0,
    )
    plt.savefig(path, bbox_inches="tight")
    plt.clf()
    # Sets seaborn whitegrid on every plot for consistency (darkgrid is nice for slides)
    sns.set_style("whitegrid")


def plotArtifactsOverYears(df, figsDir):
    data = df.groupby(["artifact_url"]).tail(1)
    sns.set_style("whitegrid")
    ax = sns.displot(
        data,
        x="year",
        hue="badges",
        multiple="stack",
        hue_order=["reproduced", "functional", "available"],
        palette=sns.color_palette()[0:3][::-1]
    )
    sns.move_legend(
        ax,
        "lower center",
        bbox_to_anchor=(0.5, 1),
        ncol=3,
        title=None,
        frameon=False,
        reverse=True,
    )
    ax.set_axis_labels("Year", "Number of Artifacts")
    saveFig(figsDir + "artifacts-over-years.pdf")
    return


def plotCurrentYear(inputCurrentYear, figsDir):
    from matplotlib.ticker import MaxNLocator
    sns.set_style("whitegrid")
    df = pd.read_csv(inputCurrentYear)
    df_long = df.melt(
        id_vars=["issue", "badges"],
        value_vars=["submitted", "awarded"],
        var_name="status",
        value_name="count",
    )

    ax = sns.catplot(
        data=df_long,
        x="badges",
        y="count",
        hue="status",
        col="issue",
        kind="bar",
        height=4,
        aspect=1.2,
        # palette=sns.color_palette("colorblind")
    )

    for item in ax.axes.flat:
        #set yaxis to integer
        item.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_axis_labels("", "Number of Artifacts")
    ax.set_titles("Issue {col_name}")
    sns.move_legend(
        ax,
        "lower center",
        bbox_to_anchor=(0.5, 1),
        ncol=2,
        title=None,
        frameon=False,
        reverse=True,
    )

    saveFig(figsDir + "current-year.pdf")
    return

def plotOverviewCurrentYear(inputCurrentYear, figsDir):
    from matplotlib.ticker import MaxNLocator
    sns.set_style("whitegrid")
    df = pd.read_csv(inputCurrentYear)

    dfperissue = df.groupby("issue")["awarded"].sum().reset_index()

    ax = sns.barplot(
        dfperissue,
        x="issue",
        y="awarded"
    )
    ax.bar_label(ax.containers[0]) # type: ignore
    ax.set_xlabel("Issue")
    ax.set_ylabel("Number of Artifacts")

    saveFig(figsDir + "current-year-per-issue.pdf")

    dfperbadge = df.groupby("badges")["awarded"].sum().reset_index()

    ax = sns.barplot(
        dfperbadge,
        x="badges",
        y="awarded"
    )
    ax.bar_label(ax.containers[0]) # type: ignore
    ax.set_xlabel("Badges")
    ax.set_ylabel("Number of Artifacts")

    saveFig(figsDir + "current-year-per-badge.pdf")


    return


def plotAll(df, inputCurrentYear, figsDir):
    plotArtifactsOverYears(df, figsDir)
    plotCurrentYear(inputCurrentYear, figsDir)
    plotOverviewCurrentYear(inputCurrentYear, figsDir)

    return


def loadResults(inputDir):
    dfs = []

    for file in os.listdir(os.fsencode(inputDir)):
        filename = os.fsdecode(file)
        with open(inputDir + filename, "r") as result:
            data = yaml.safe_load(result)
            dftemp = pd.DataFrame(data["artifacts"])
            dftemp["year"] = filename.split(".yaml")[0]
            if filename in ["2020.yaml", "2021.yaml", "2022.yaml", "2023.yaml"]:
                dftemp["badges"] = "available"
            elif filename == "2024.yaml":
                dftemp["badges"] = np.where(
                    dftemp["badges"] == "artifact-available", "available", "reproduced"
                )
            else:
                dftemp["badges"] = dftemp["badges"].str.split(",")
                dftemp = dftemp.explode("badges", ignore_index=True)
            dfs.append(dftemp)

    return pd.concat(dfs).sort_values(by=["year", "badges"], ascending=[True, True])


if __name__ == "__main__":
    # Create Argument Parser
    parser = argparse.ArgumentParser(
        prog="python3 stats.py",
        description="Generate figs for PETS AEC presentations",
    )
    parser.add_argument(
        "-inputDir",
        "--inputDir",
        help="Input folder",
        default="./results/",
    )
    parser.add_argument(
        "-inputCurrentYear",
        "--inputCurrentYear",
        help="Input current year filename",
        default="./current-year-stats.csv",
    )
    parser.add_argument(
        "-figsDir",
        "--figsDir",
        help="Figs Directory",
        default="./figs/",
    )
    args = parser.parse_args()

    import os

    if not (os.path.isdir(args.inputDir)):
        raise Exception("Error: file(s) missing")
    else:
        # Automatically create the output directory hierarchy if needed
        os.makedirs(os.path.dirname(args.figsDir), exist_ok=True)
        import pandas as pd
        import yaml
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib
        import seaborn as sns

        plotAll(loadResults(args.inputDir), args.inputCurrentYear, args.figsDir)

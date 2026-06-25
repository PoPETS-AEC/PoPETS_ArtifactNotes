import argparse

if __name__ == "__main__":
    # Create Argument Parser
    parser = argparse.ArgumentParser(
        prog="python3 generate-results.py",
        description="Generate yamnl results for secartifact website from hotcrp csv file (also used by generate-links.py)",
    )
    parser.add_argument(
        "-inputFile",
        "--inputFile",
        help="Input csv file",
    )
    parser.add_argument(
        "-outputFile",
        "--outputFile",
        help="Output yaml file",
    )
    args = parser.parse_args()

    import os

    if not (os.path.isfile(args.inputFile)):
        raise Exception("Error: file(s) missing")
    else:
        # Automatically create the output directory hierarchy if needed
        os.makedirs(os.path.dirname(args.outputFile), exist_ok=True)
        import yaml
        import pandas as pd

        inputFilename = args.inputFile
        outputFilename = args.outputFile

        df = pd.read_csv(inputFilename)
        artifacts = []

        for index, row in df.iterrows():
            item = {}
            item["paper_url"] = ""
            item["title"] = row["Title"]
            item["artifact_url"] = row["Final link"]
            item["badges"] = str.lower(row["Status"])
            artifacts.append(item)

        with open(outputFilename, "w") as output:
            yaml.dump({"artifacts": artifacts}, output, default_flow_style=False, sort_keys=False, default_style='"')

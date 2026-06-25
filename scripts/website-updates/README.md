# `generate-results.py`

Quick script to parse csv file obtained from HotCRP (with final artifact link and badges) into the yaml file expected for the https://secartifacts.github.io/ website and by the `generate-links.py` script

Usage: `python3 generate-results.py --inputFile ./Artifact_2026_4-data.csv --outputFile ./2026.4.yaml`

# `generate-links.py`

A script to generate the links for the official PETS website for artifacts from prior yaml file.

Usage: `python3 generate-links.py --inputFile ./2026.4.yaml --outputFile ./2026.4.html`

The generated `.html` file contains the corresponding links to use in `202X/paperlist.php` and `202X.N.yaml` for the official website and proceedings.
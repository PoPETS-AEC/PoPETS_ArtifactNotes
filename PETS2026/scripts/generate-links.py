import yaml

filename = "results"
inputFilename = filename + ".yaml"
outputFilename = filename + ".html"

with open(inputFilename, "r") as f:
    input = yaml.safe_load(f)

    with open(outputFilename, "w") as output:

        for artifact in input["artifacts"]:
            output.write("\n{}\n".format(artifact["title"]))
            if artifact["badges"] == "available":

                output.write(
                    ' <a href="{}" target="_blank" class="artifact-available">Artifact: Available</a>\n'.format(
                        artifact["artifact_url"]
                    )
                )
                output.write(
                    "  artifact-available: {}\n".format(artifact["artifact_url"])
                )

            elif artifact["badges"] == "available, functional":
                output.write(
                    ' <a href="{}" target="_blank" class="artifact-available artifact-functional">Artifact: Available, Functional</a>\n'.format(
                        artifact["artifact_url"]
                    )
                )
                output.write(
                    "  artifact-available: {}\n".format(artifact["artifact_url"])
                )
                output.write("  artifact-functional:\n")

            elif artifact["badges"] == "available, functional, reproduced":
                output.write(
                    ' <a href="{}" target="_blank" class="artifact-available artifact-functional artifact-reproduced">Artifact: Available, Functional, Reproduced</a>\n'.format(
                        artifact["artifact_url"]
                    )
                )
                output.write(
                    "  artifact-available: {}\n".format(artifact["artifact_url"])
                )
                output.write("  artifact-functional:\n")
                output.write("  artifact-reproduced:\n")

            elif artifact["badges"] == "functional":
                output.write(
                    ' <a href="{}" target="_blank" class="artifact-functional">Artifact: Functional</a>\n'.format(
                        artifact["artifact_url"]
                    )
                )
                output.write(
                    "  artifact-functional: {}\n".format(artifact["artifact_url"])
                )

            elif artifact["badges"] == "functional, reproduced":
                output.write(
                    ' <a href="{}" target="_blank" class="artifact-functional artifact-reproduced">Artifact: Functional, Reproduced</a>\n'.format(
                        artifact["artifact_url"]
                    )
                )
                output.write(
                    "  artifact-functional: {}\n".format(artifact["artifact_url"])
                )
                output.write("  artifact-reproduced:\n")

            else:
                raise Exception(
                    "issue with badge with paper: {}".format(artifact["title"])
                )

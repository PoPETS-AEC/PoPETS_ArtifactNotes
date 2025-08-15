# Artifact Appendix (Required for all badges)

Paper title: **Enter the exact title of your PETS accepted paper here**

Requested Badge(s):
  - [ ] **Available**
  - [ ] **Functional**
  - [ ] **Reproduced**

Note:
- Authors should not leave the placeholder descriptions initially provided with
this file into the submitted version with their artifact.
- Similarly, authors should feel free to remove this note, delete the sections
that are not required for the badge(s) they are applying for, and omit from the
section titles the "(required/encouraged for badge ...)" indications.
- Authors should feel free to provide this content as a separate file in their
artifact or as part of their existing documentation (e.g., `README.md`). In the
latter case, we only ask that section titles remain the same.

## Description (Required for all badges)
Replace this with the following:
- List the paper that the artifact relates to (i.e., paper
title, authors, year, or even a BibTex cite).
- A short description of your artifact and how it is relevant to your
paper.

### Security/Privacy Issues and Ethical Concerns (Required for all badges)
Replace this by a description of security or privacy risks that your artifact
may hold for the machine of the person trying to evaluate or reuse your
artifact. For example, if your artifact requires a specific security mechanism,
like a firewall, ASLR, or another thing, to be disabled for its execution. Also,
emphasize if your artifact contains malware samples, or something similar, to be
analyzed. In addition, you should highlight any ethical concerns regarding your
artifact.

## Basic Requirements (Required for Functional and Reproduced badges, encouraged for Available badge)

### Hardware Requirements (Required for Functional and Reproduced badges, encouraged for Available badge)
Replace the following by the minimal hardware requirements to execute your
artifact. If no specific hardware is needed, then state something like "Can run
on a laptop (No special hardware requirements)".

Note that if you are giving remote access to some hardware to reviewers for the
purpose of the artifact evaluation only, do not provide these instructions here
but rather in the corresponding submission field on HotCRP. Also, make sure to
preserve the anonymity of the reviewer at any time.

Instead, provide here instructions for someone trying to reuse your artifact in
the future (i.e., not an artifact reviewer). For instance state how they could
gain access to that hardware, e.g., by buying, renting, or even emulating it.

Additionally, if you are applying for the "Reproduced" badge, please also list
the exact hardware specifications of the machine(s) and/or device(s) on which
experiments and results reported in the paper were performed. This is especially
relevant in cases were results might be influenced by the hardware used (e.g.,
performance and timing experiments, etc.).

### Software Requirements (Required for Functional and Reproduced badges, encouraged for Available badge)
Replace the following by the minimal OS and software requirements, as well as
their versions, to evaluate your artifact. This description is essential if you
rely on proprietary software or software that might not be easily accessible for
other reasons.

Note that if you are giving access to something to reviewers for the purpose of
the artifact evaluation only (private dataset for instance), do not provide
these instructions here but rather in the corresponding submission field on
HotCRP.

Instead, provide here instructions for someone trying to reuse your artifact in
the future (i.e., not an artifact reviewer). Describe how someone can obtain and
install all third-party software, datasets, models, etc. For instance, you
should provide dummy and/or synthetic data to replace potentially private
dataset, showcase the expected data format, and demonstrate the functionality of
the rest of the artifact.

Additionally, if you are applying for the "Reproduced" badge, make sure to list
the exact software specifications and versions used for the experiments and
results reported in the paper (or point to a file in your artifact that has that
list).

### Estimated Time and Storage Consumption (Required for Functional and Reproduced badges, encouraged for Available badge)
Replace the following by estimated values for:
- The overall human and compute times running the artifact will take.
- The overall disk space it will consume.

This helps reviewers to schedule the evaluation in their time plan and others in
general to see if everything is running as intended. This should also be
specified at a finer granularity for each experiment (see below).

## Environment (Required for all badges)
In the following, describe how to access your artifact and all related and
necessary data and software components. Afterward, describe how to set up
everything and how to verify that everything is set up correctly.

### Accessibility (Required for all badges)
Replace the following by a description of how to access your artifact via
persistent sources. Valid hosting options are institutional and third-party
digital repositories (e.g., GitHub, Gitlab, BitBucket, Zenodo, Figshare, etc.).
Please do not use personal web pages or cloud storage services like Google
Drive, Dropbox, etc.

Note that once your artifact evaluation is finalized and a badge decision has
been made, artifact chairs will collect a stable and persistent reference to
your artifact to list on the website. For repositories that evolve over time
(e.g., git repositories), this will be a specific commit-id or tag. We do not
suggest providing such link for your artifact here at submission time, as it is
very likely that changes will happen during the evaluation process to address
the reviewer's feedback requiring the link to be updated.

### Set up the environment (Required for Functional and Reproduced badges)
Replace the following by a description of how one should set up the environment
for your artifact, including downloading and installing dependencies and the
installation of the artifact itself (i.e., from the very first download or clone
command one should perform). Be as specific as possible here. If possible, use
code segments to simplify the workflow, e.g.,

```bash
git clone git@my_awesome_artifact.com/repo
apt install libxxx xxx
```

Describe the expected results where it makes sense to do so.

### Testing the Environment (Encouraged for Functional and Reproduced badges)
Replace the following by a description of the basic functionality tests to check
if the environment is set up correctly. These tests could be unit tests,
training an ML model on very low training data, etc. If these tests succeed, all
required software should be functioning correctly. Use code segments to simplify
the workflow, e.g.,

```bash
./test.sh
```

Include the expected output for unambiguous outputs of tests.

## Artifact Evaluation (Required for Functional and Reproduced badges)
This section should include all the steps required to evaluate your artifact's
functionality and validate your paper's key results and claims. Therefore,
highlight your paper's main results and claims in the first subsection. And
describe the experiments that support your claims in the subsection after that.

### Main Results and Claims (Required for Functional and Reproduced badges)
List all your paper's results and claims that are supported by your submitted
artifacts.

#### Main Result 1: Name
Describe the results in 1 to 3 sentences. Refer to the related sections,
figures, and/or tables in your paper and reference the experiments that support
this result/claim (see example below).

#### Main Result 2: Name
Describe the results in 1 to 3 sentences. Refer to the related sections,
figures, and/or tables in your paper and reference the experiments that support
this result/claim (see example below).

...

For example:
#### Main Result 3: Example Name
Our paper claims that an "example result" of "X unit" and "Y unit" (reported in
"Figure F" and "Table T") can be obtained with our prototype, this is
reproducible by executing [Experiment 3](#experiment-3-example-name)


### Experiments (Required for Functional and Reproduced badges)
List each experiment to execute to reproduce your results. Describe:
 - How to execute it in detailed steps.
 - What the expected result is.
 - How long it takes to execute in human and compute times (approximately).
 - How much space it consumes on disk (approximately) (omit if <10GB).
 - Which claim and results does it support, and how.

#### Experiment 1: Name
- Time: replace with estimate in human-minutes/hours + compute-minutes/hours.
- Storage: replace with estimate for disk space used (omit if <10GB).

Provide a short explanation of the experiment and expected results. Describe
thoroughly the steps to perform the experiment and to collect and organize the
results as expected from your paper (see example below). Use code segments to
simplify the workflow, e.g.,
```bash
python experiment_1.py
```

#### Experiment 2: Name
- Time: replace with estimate in human-minutes/hours + compute-minutes/hours.
- Storage: replace with estimate for disk space used (omit if <10GB).

Provide a short explanation of the experiment and expected results. Describe
thoroughly the steps to perform the experiment and to collect and organize the
results as expected from your paper (see example below). Use code segments to
simplify the workflow, e.g.,
```bash
./experiment2.sh
```

...

For example:
#### Experiment 3: Example Name
- Time: 10 human-minutes + 3 compute-hours
- Storage: 20GB

This example experiment reproduces [Main Result 3: Example
Name](#main-result-3-example-name), the following script will run the
simulation automatically with the different parameters specified in the paper.

```bash
./experiment-example.sh
```

Results from this example experiment will be aggregated over several iterations
by the script and output directly in raw format along with variances and
standard deviations in the `output-folder/` directory. You will also find there
the plots for "Figure F" in `.pdf` format and the table for "Table T" in `.tex`
format. These can be directly compared to the results reported in the paper, and
should not quantitatively vary by more than 5% from expected results.


## Limitations (Required for Functional and Reproduced badges, encouraged for Available badge)
Describe which steps, experiments, results, graphs, tables, etc. are included or
are not reproducible with the provided artifact. Provide an argument why this is
not included/possible.

## Notes on Reusability (Encouraged for all badges)
First, this section might not apply to your artifacts. Use it to share
information on how your artifact can be used beyond your research paper, e.g.,
as a general framework. The overall goal of artifact evaluation is not only to
reproduce and verify your research but also to help other researchers to re-use
and improve on your artifacts. Please describe how your artifacts can be adapted
to other settings, e.g., more input dimensions, other datasets, and other
behavior, through replacing individual modules and functionality or running more
iterations of a specific part.

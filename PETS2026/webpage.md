# PoPETs 2026 Artifact Evaluation

PoPETs reviews and publishes digital artifacts related to its accepted papers.
This process aids in the reproducibility of results and allows others to build
on the work described in the papers. Artifact submissions are requested from
authors of all accepted papers, and although they are optional, we strongly
encourage you to submit your artifacts for review.

Possible artifacts include (but are not limited to):

- Source code (e.g., system implementations, proof of concepts)
- Datasets (e.g., network traces, raw study data)
- Scripts for data processing or simulations
- Machine-generated proofs
- Formal specifications
- Build environments (e.g., VMs, Docker containers, configuration scripts)

Artifacts are evaluated by the artifact evaluation committee. The committee
evaluates the artifacts to ensure that they provide an acceptable level of
utility. Issues considered include software bugs, readability of the
documentation, appropriate licensing, and the reproducibility of the results
presented in the paper. After your artifact has been approved by the committee,
we will accompany the paper link on [petsymposium.org](https://petsymposium.org)
with a link to the artifact along with the obtained artifact badges so that
interested readers can find and use your hard work.

## Artifact Submission Guidelines

- All submitted artifacts should be relevant to their corresponding PoPETs
  paper. Please upload a copy of your paper.
- Many papers have several artifacts (e.g., multiple source code repositories,
  datasets, build environments), which is great! Please keep in mind that we'll
  need a single link to put on the PETS website and that all artifacts
  associated with your paper should be discoverable from that one link. If you
  have several git repositories, we suggest using
  [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
- Please include a `README.md` file with your submission that briefly explains
  the type and purpose of the artifact. At a prominent position in the
  `README.md` file make clear to which paper the artifact belongs (i.e., paper
  title, authors, year, even BibTeX cite if you want) and how the artifact is
  relevant to the paper.
- Please include the content of the [ARTIFACT-APPENDIX.md](ARTIFACT-APPENDIX.md)
  file in your artifact (either include it in the `README.md` file or add it as
  a separate file.). It contains information that should be filled out by
  authors and that is important for not only reviewers during the evaluation
  process, but also future researchers attempting to re-use your artifact.
  Provide a direct link to that file content at submission.


### Source Code Submissions

All source code should be accompanied by a `README.md` file or other
documentation that describes how to build and/or run the code. Reviewers will
provide feedback on the clarity of the instructions and attempt to follow them
and build and/or run the code.

Any source code submissions should be accompanied by a build environment such
as a virtual machine or a Docker container that has been configured with all
the dependencies and prerequisites necessary to build the code.
- If you use a virtual machine, please state how many resources it will consume
  and any configuration steps that are required. Your virtual machine should not
  usually have to download additional dependencies when you run your
  installation scripts. If that is the case, reassess your build process and
  consider making changes to limit the amount of network resources needed.
- Note that, if needed and to ease the process, we provide artifact reviewers
  with VM instances that can be spawn from HotCRP to perform the evaluation.
  Your artifact, however, should also be executable and helpful for the public
  and not only on these VMs. Hence, your descriptions and scripts should be as
  generic as possible.
- If your artifact runs on compute providers, like AWS or similar, state the
  amount of money/credits required to run the experiments and provide account
  credentials with enough credits. Our reviewers won't invest their money or
  credit cards to set up accounts. If this cannot be provided, provide an
  alternative way of running your artifact. If this is not possible, reconsider
  your choices of badges (see below).

If the code is in a compiled language, the code should compile in the provided
build environment by performing the provided instructions. Compilation and setup
should be automated as much as possible. Ideally, there will be one script that
builds your software, runs your tests, and produces the results in a
comprehensible way.

Please ensure that your code has a license and clearly states this information.
The following resources may help you to choose a license:
- For a clear, easy to follow guide see: https://choosealicense.com/
- For more in-depth detail on open source and copy-left licenses, see
    https://www.gnu.org/licenses/license-list.en.html and
    https://opensource.org/licenses

Our goal is that the artifacts are useful for as long as possible. Some tips
on improving the longevity of your source code artifact are:
- Include and pin the versions of your software's dependencies wherever
  possible.
- Reference specific hashes of git commits for additional git repositories you
  may be using (we suggest using [git
  submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)).
- Virtual machine images or Docker images tend to last longer than their
  respective install scripts or Docker files and allow researchers to more
  accurately reproduce your exact execution environment, though the trade-off is
  that they will be larger. If you make images available, we also require that
  you also release the scripts or files that let you build them.
- Artifacts are not required to be able to run on all hardware and OSes. If
  your artifact requires any particular hardware/OS for valid reasons,
  please make it clear in the submission.

### Dataset Submissions

- All datasets should be clearly documented in a way that allows researchers
  working on similar problems to re-use the dataset for their work.
- If the dataset includes survey results, provide a copy of the original survey
  with raw results. This is vital for replication studies and helping
  researchers interpret the context of your results.
- Please state the sizes of datasets in the documentation.
- It's encouraged to accompany the data with processing scripts that demonstrate
  how to use the data and produce the graphs or statistical output that appear
  in the paper.

## Artifact Badges

Each accepted artifact can be granted up to three badges. During submission,
authors must select which badges they want their artifacts to be evaluated
against. To ease reviewing effort, we encourage authors to apply appropriately
to all the badges for which they believe requirements are met by their artifact
(see below). Our interpretation of the individual badges is globally aligned
with the ones of [other conferences](https://secartifacts.github.io/). If you
have concerns or questions about these badges please contact the artifact
evaluation chairs directly.

### Artifact Available
This "Artifact Available" badge indicates that the artifact is publicly
available at a permanent location (not behind any kind of paywall or restricted
access). If the artifact requires you as an author to manually approve requests
for access, it is not public and will not qualify for the "Artifact Available"
badge.

Valid hosting options are institutional and third-party digital repositories
(e.g., GitHub, Gitlab, BitBucket, Zenodo, Figshare, etc.). Please do not use
personal web pages or cloud storage services like Google Drive, Dropbox, etc.

For the "Artifact Available" badge, the reviewers check that the artifact can be
retrieved, and that it includes a license. The reviewers check that the artifact
is relevant to the paper. This badge does *not* mean that the reviewers have
reproduced the results or checked that the code executes or that they have
reproduced the results for full functionality.

Checklist for "Available Badge":
- [ ] Publicly available (single link).
- [ ] License present.
- [ ] Relevant to paper.
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

### Artifact Functional <ToDO: review>
For the "Artifact Functional" badge the artifact should satisfy these criteria:
- Documentation: It clearly documents how it relates to the paper, and how it
  should be used.
- Completeness: It includes all the core contributions described in the paper.
- Exercisability: It includes the scripts and data needed to run the experiments
  described in the paper. The software must successfully execute or compile in
  the provided environment.

Some artifacts may not, by definition, be able to satisfy the completeness or
exercisability criteria. For instance, an artifact may have a proprietary
machine learning model as a key component of the system, and so, achieving
completeness may be difficult. Artifacts may rely on datasets that are too large
to be included, or contain personally identifiable information, and so,
satisfying exercisability is difficult. We guide authors below, using some
examples, on how they can still prepare their artifact to achieve this badge.
Additionally, some artifacts, such as longitudinal studies or hardware-based
contributions, may be infeasible for the “Artifact Reproduced” badge (see
below), as reviewers have limited time and only commodity hardware available.
Nevertheless, these authors can prepare their artifacts for the “Artifact
Functional” badge, as described in the examples:

Checklist for "Functional Badge":
- [ ] 
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

<TODO Notes> 
IP protections and commercialization prospects should not inhibit this; e.g.
authors can choose restrictive licenses that prohibit others from using their
code or design a smaller working prototype to demonstrate reproducibility; the
Functional + Reproduced badge combo can be used towards this. 

SLURM cluster -> smaller example?


### Artifact Reproduced <ToDO: review>
The "Artifact Reproduced" badge requires the core contributions of the paper to
be reproduced by the reviewers. Authors must specify the commands to run the
artifacts clearly and describe how to reproduce each core finding of the paper.
Best practice is to point out which part of the paper is reproduced by a given
script, e.g., name the table or figure. Also, the authors must highlight which
results of the paper are not reproducible with the given artifacts and argue
why.


Checklist for "Reproduced Badge":
- [ ] 
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.


<TODO notes> Note that minor additional experiments that do not significantly
contribute to the paper may not be included in the artifact.

Make it clear that reviewers are supposed to look at the standard deviation figs
and then even with fewer runs than the total number used in the paper, they can
still check whether the results have been reproduced.


### Persistent and Stable Link
When the artifact evaluation is over, a persistent and stable link pointing to
the final evaluated version of the artifact will be collected for each accepted
artifact. This link and the awarded badge(s) will be added to the website next
to the corresponding paper title. As updates to the artifact are likely to occur
to address reviewers' feedback, we will only collect this persistent and stable
link (likely a DOI, or a link to a specific git commit/tag depending on the
hosting option picked) after a final decision is made.


### Examples <ToDO review examples>
Consider the experiments in your artifact as arranged in a pipeline of multiple
stages, such as data collection, data processing, and producing plots or tables
for the paper. The “Completeness” and “Exercisability” criteria require each
stage to be represented. Our key advice is to present each stage, including the
ones that cannot be fully run. These can be represented in either a simplified
manner or run on dummy data to check the functionality of the stage. If
possible, provide the expected outcome of the fully run stage such that
preceding stages are performed on 'real' data again. In the following we
present some examples:

**Tools based on large machine learning (ML) models.** If an ML model is
required to execute the presented tool, the authors should provide it, unless it
is proprietary. Authors may use `git-lfs` to commit large model files to their
repository. If they can not share the model, we expect them to share a dummy
model, which may perhaps perform worse, but which can be used to test the
principle functionality of the presented tool. Ideally, authors should provide
the code to train the original model, though depending on the contributions of
the paper, it need not be executed.

**Lengthy experiment runtimes.** Similar to the point above, even if the
experiment requires days or weeks of compute time on commodity hardware, the
"Artifact Functional" badge can be achieved. In such cases the authors should
also provide a simplified version of the experiment, which may run on less
training data or for fewer epochs of time, in order to enable the reviewers to
check the functionality of that stage. Authors should additionally provide
results of the full experiments in the repository, so that reviewers can verify
the functionality of the later stages with these results.

**User studies, longitudinal studies and crawls.**  Some studies cannot be
repeated within the reviewing process. However, the authors should provide the
evaluation scripts to reproduce the main results of the paper. Pseudonymized raw
data should also be provided, unless forbidden by legal requirements, privacy,
or ethical concerns. In such cases, a data set with dummy data should be
included. Reviewers should be able to execute the evaluation scripts on either
the pseudonymized raw data or dummy data.

**Hardware-based contributions.** If the artifact requires certain hardware,
please request for it within the "hardware requirement" section in the
[ARTIFACT-APPENDIX.md](ARTIFACT-APPENDIX.md) template. If special physical
setups are required, the authors may simulate the hardware. Authors should
publish the raw results of the experiments, so that reviewers can verify the
remaining stages as functional.


# What makes a Good Submission

To ensure a smooth submission process, please follow these important guidelines:

Authors should fill out the [ARTIFACT-APPENDIX.md](ARTIFACT-APPENDIX.md) file
provided and include it in their artifact (either in the `README.md` file or as
a separate file). Check the badges you deem reasonable for your artifact and, if
necessary, describe which stages are simplified or skipped and why. This will
help the reviewer better understand your work and ensure a seamless review
process.

Authors should alpha-test their artifact and instructions themselves from a
fresh install (or ask an acquaintance to do so) and fix potential issues that
are uncovered before submission.

Authors are also encouraged to check out the [resources and
examples](TODO-ADD_LINK) of artifact packaging that have been put together by
the artifact evaluation chairs. These guides describe some best practices and
ways to package artifact for different popular programming workflows, authors
should feel free to use them as starting point and build on them to package and
release their artifact. Note that these resources are not comprehensive, so
authors and reviewers are asked please to not interpret them as the only way to
package an artifact (we also welcome suggestions to these resources in the form
of issues, pull requests, or direct contributions).

For the "Artifact Functional" and/or "Artifact Reproduced" badges, very clear
documentation, instructions, and mapping between claims, results, and
experiments usually go a long way in facilitating the evaluation. Ideally,
reviewers should be able to execute a single script to install, configure, and
reproduce results. Similarly, parameters swap for experiments should be
automated.

During the evaluation, prompt and professional communication with reviewers is
essential to reach a final decision. Authors are kindly requested to respond to
reviews and comments within a time span of one week. This will facilitate
constructive discussions and allow for timely feedback incorporation.

Lastly, in the event that changes are requested during the review process, we
kindly ask authors to endeavor to incorporate them, at least partially, within
two weeks after the request. These requested modifications should not be left
to the last minute, if some fixes require more time, authors are encouraged to
communicate a timeline by which these changes will be made for reviewers to best
plan around for their evaluation.

Your cooperation in adhering to these guidelines will greatly contribute to the
efficiency and effectiveness of your submission and review process. We eagerly
anticipate receiving your high-quality contributions and look forward to
showcasing your research!

## Artifact Award <ToDo>

<TODO notes> criteria, for reviewers: imagine that you were working in the field of
that artifact, would you be able to reuse it easily?


# What Makes a Good Review <Todo>

The goal of our artifact evaluation is to ensure the artifacts are as useful as
possible. Towards this goal, artifact evaluation process is interactive, and we
expect the authors to take into account the reviewers' comments and modify their
artifacts accordingly. As such, the reviews or posted comments should contain
sufficient details for the authors to make the appropriate changes; for example,
if the code fails, then reviewers should include the environment that it is run
on and the error messages. After the authors have fixed the issues, they will
add a comment on the submission site, at which point the reviewers can either
approve the artifact or provide additional comments for another rounds of
revision.

<TODO notes> interactive, have read the call for artifact and appendix to
understand the requirements and asks from authors, start evaluation early,
discuss and work with authors to fix their artifact if any issue, edit
preliminary review as edits are made by authors, stay polite and considerate,
tag Artifact Evaluation Chairs on artifacts that may need our attention for some
reason or if any question.

## Distinguished Artifact Reviewers

Since PETS 2025, we recognize members of the artifact evaluation committee that
go above and beyond as [distinguished artifact
reviewers](https://petsymposium.org/reviewer-awards.php), based on:

- Timeliness, including responding to authors’ updates.
- High quality reviews and discussions that significantly improve the artifact.
- Helping out with extra reviews e.g., for artifacts with special requirements,
  etc.


# Volunteer for the Artifact Evaluation Committee

We are looking for volunteers to serve on the artifact evaluation committee. As
a committee member, you will perform review of artifacts according to the
guidelines above. We are looking for volunteers who will be interested in
providing feedback on documentation and instructions, trying to get source code
to build, or have experience with re-using published datasets. Please fill out
the reviewer nomination form linked in the menu of the PETS website and then
email [artifact26@petsymposium.org](mailto:artifact26@petsymposium.org).

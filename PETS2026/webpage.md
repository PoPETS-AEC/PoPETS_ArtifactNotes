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
  have several git repositories, we suggest using [git
  submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
- Please include a `README.md` file with your submission that briefly explains
  the type and purpose of the artifact. At a prominent position in the
  `README.md` file make clear to which paper the artifact belongs (i.e., paper
  title, authors, year, even BibTeX cite if you want) and how the artifact is
  relevant to the paper.
- Please include the content of the
  [ARTIFACT-APPENDIX.md](https://petsymposium.org/files/ARTIFACT-APPENDIX.md)
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

Any source code submissions should be accompanied by a build environment such as
a virtual machine or a Docker container that has been configured with all the
dependencies and prerequisites necessary to build the code.
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
  your choices of badges (see badges guidance section).

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

Our goal is that the artifacts are useful for as long as possible. Some tips on
improving the longevity of your source code artifact are:
- Include and pin the versions of your software's dependencies wherever
  possible.
- Reference specific hashes of git commits if using several git repositories (we
  suggest using [git
  submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)).
- Virtual machine images or Docker images tend to last longer than their
  respective install scripts or Docker files and allow researchers to more
  accurately reproduce your exact execution environment, though the trade-off is
  that they will be larger. If you make images available, we also require that
  you also release the scripts or files that let you build them.
- Artifacts are not required to be able to run on all hardware and OSes. If your
  artifact requires any particular hardware/OS for reasonable reasons, please
  make it clear in the submission.

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
(see details below). Our interpretation of the individual badges is aligned with
the one of [other conferences](https://secartifacts.github.io/). If you have
concerns or questions about these badges please contact the artifact evaluation
chairs directly.

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

### Artifact Functional
To be awarded the "Artifact Functional" badge the artifact should satisfy these
criteria:
- Documentation: The artifact clearly documents how it relates to the paper, and
  how it should be used (i.e., installation + execution).
- Completeness: It includes all the core contributions described in the paper.
- Exercisability: It includes the scripts and data needed to run the experiments
  described in the paper. The software must successfully execute or compile in
  the provided environment.

Some artifacts may not, by definition, be able to satisfy the completeness or
exercisability criteria. For instance, an artifact may have a proprietary
machine learning model as a key component of the system, and so, achieving
completeness may be difficult. Artifacts may rely on datasets that are too large
to be included, or contain personally identifiable information, and so,
satisfying exercisability may be difficult. 

Consider the experiments in your artifact as arranged in a pipeline of multiple
stages, such as data collection, data processing, and producing plots or tables
for the paper. The "Completeness" and 'Exercisability" criteria require each
stage to be represented. Our key advice is to present each stage, including the
ones that cannot be fully run. These can be represented in either a simplified
manner or run on dummy data to check the functionality of the stage. If
possible, provide the expected outcome of the fully run stage such that
preceding stages are performed on 'real' data again. We provide under the
"Badges Guidance" section, some specific examples on how authors can still
prepare their artifact for the "Artifact Functional" badge in these cases.

Checklist for "Functional Badge":
- [ ] Clear documentation is provided.
- [ ] Completeness criterion fulfilled (with potential limitations reasonably
  argued).
- [ ] Exercisability criterion fulfilled (with potential limitations reasonably
  argued).
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

### Artifact Reproduced
The "Artifact Reproduced" badge requires the core contributions of the paper to
be reproduced by the reviewers. Authors must specify the commands to run the
artifacts clearly and describe how to reproduce each core finding of the paper.
Best practice is to point out which part of the paper is reproduced by a given
script, e.g., name the table or figure. Also, the authors must highlight which
results of the paper are not reproducible with the given artifacts and
reasonably argue why. Additionally, authors are encouraged to contemplate how
their artifact could be re-used by others in the future and describe potential
ways for improvement, etc.

Authors are also asked to automate as much as possible the execution of the
experiments, manual effort from reviewers to run and interpret the results
should be kept to a minimum. For instance, if an experiment is performing a swap
across different parameters, a script automating it should be provided. Ideally,
results should also be automatically parsed and output in a comprehensible way.

To award the "Artifact Reproduced" badge, reviewers must be absolutely confident
that they can reproduce the core results of the paper with the provided
artifact. As a rule of thumb, a claim should be considered reproducible if the
results by reviewers are within 5% of the reported value in the paper. It is the
reviewer's role to enforce that this expectation (or a similar one adapted to
each specific artifact) is met before awarding the "Artifact Reproduced" badge.

Additionally, some experiments may by nature be harder to fully reproduced
during the timeframe of the artifact evaluation: e.g., take a while to run, need
several iterations, train a model on a large dataset, etc. In these cases,
authors should still provide the instructions and expected results for the
"long" version of the experiment, and also for a simplified one (e.g., fewer
iterations, smaller dataset, etc.). Indeed, even on a simplified version or
fewer runs, reviewers should still somewhat be able to look at the results and
the standard deviation, and check that results from the paper can be reproduced.

Finally, some artifacts, such as longitudinal studies or hardware-based
contributions, may be infeasible for the “Artifact Reproduced” badge (see badges
guidance below), as reviewers have limited time and only commodity hardware
available. Nevertheless, these authors can and should still prepare their
artifacts for the “Artifact Functional” badge.

Note: by nature, an artifact awarded the "Artifact Reproduced" badge needs to
also meet the requirements of the "Artifact Functional" badge.

Checklist for "Reproduced Badge":
- [ ] Meets "Functional Badge" requirements.
- [ ] List of the core contributions and claims of the paper identified.
- [ ] Clear mapping between claims, experiments, and results provided.
- [ ] Minimal amount of manual effort required from reviewers, i.e., fair amount
  of automation.
- [ ] Reviewers obtain reproducible results (i.e., within 5% of the claimed
  value).
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

### Persistent and Stable Link
When the artifact evaluation is over, a persistent and stable link pointing to
the final evaluated version of the artifact will be collected for each accepted
artifact. This link and the awarded badge(s) will be added to the website next
to the corresponding paper title. As updates to the artifact are likely to occur
to address reviewers' feedback, we will only collect this persistent and stable
link (likely a DOI, or a link to a specific git commit/tag depending on the
hosting option picked) after a final decision is made.

### Badges Guidance
Next, we provide some guidance around the choice of badges for authors, followed
by a few examples encountered in past editions along with our suggestions to
authors in similar situations.

**All submitted artifacts should apply at least for "Artifact Available".**
Unless for some unusual and reasonably justified cases, when doing so could
endanger someone. For instance, if the artifact demonstrates exploiting a
vulnerability and making the artifact available would harm users, authors could
apply for just the "Functional and Reproduced Badges". Note that IP protections
and commercialization prospects should not inhibit authors from applying for the
"Artifact Available" badge; e.g., authors can choose restrictive licenses that
prohibit others from using their code or design a smaller working prototype to
demonstrate reproducibility.

**Lengthy experiment runtimes or large amount of compute resources needed.**
Although experiments may require days or weeks of compute time on commodity
hardware, the "Artifact Functional" badge can usually still be achieved. In such
cases, authors should also provide a simplified version of the experiments,
which may run on fewer data or fewer epochs of time, in order to enable the
reviewers to check the functionality of that stage. Authors should additionally
provide results of the full experiments in the repository, so that reviewers can
verify the functionality of the later stages with these results. A similar
approach could also be adopted to apply for the "Artifact Reproduced" badge, if
the results of the simplified experiments somewhat align with the ones reported
in the paper.

**Tools based on large datasets, machine learning (ML) models, or other files.**
If a large dataset, ML model, or other file is required to execute the presented
tool, the authors should provide it, unless it is proprietary. If they can not
share the dataset or model, we expect them to share a synthetic dataset or dummy
model, which may, perhaps perform worse, but which can be used to test the
principle functionality of the presented tool. Ideally, authors should provide
the code to train the original model, though depending on the contributions of
the paper, it need not be executed.

Authors should note that the hosting options that we consider as valid have
different file size limits and constraints and that dividing or compressing such
large files may be needed. For instance, GitHub has a 100MiB file size limit and
that `git-lfs` can be used to commit large files (2GB limit). For Zenodo (our
suggestion to host datasets), the per record limitation is 50GB/100 files with a
one-time quota increase up to 200GB per record. Other alternatives (HuggingFace,
OCI containers, etc.) exist and would need to be explored by authors to see if
they meet their artifact's needs.

**User studies, longitudinal studies, and crawls.** Some studies cannot be
repeated within the reviewing process. However, the authors should still provide
the evaluation scripts to reproduce the main results of the paper. Anonymized
raw data should also be provided, unless forbidden by legal requirements,
privacy, or ethical concerns. In such cases, a dataset with dummy or synthetic
data should be included. Reviewers should be able to execute the evaluation
scripts on either anonymized raw data or dummy data.

**Hardware-based contributions.** If the artifact requires certain hardware,
please make sure to indicate it adequately at submission time. If special
physical setups are required, the authors may simulate the hardware. Authors
should also publish the raw results of the experiments, so that reviewers can
verify the remaining stages as functional.

# What makes a Good Submission
To ensure a smooth submission process, please follow these important guidelines:

Authors should fill out the
[ARTIFACT-APPENDIX.md](https://petsymposium.org/files/ARTIFACT-APPENDIX.md) file
provided and include it in their artifact (either in the `README.md` file or as
a separate file). Check the badges you deem reasonable for your artifact and, if
necessary, describe which stages are simplified or skipped and why. This will
help the reviewer better understand your work and ensure a seamless review
process.

Authors should alpha-test their artifact and instructions themselves from a
fresh install (or ask an acquaintance to do so) and fix potential issues that
are uncovered before submission.

Authors are also encouraged to check out the [resources and
examples](https://github.com/PoPETS-AEC/examples-and-other-resources) of
artifact packaging that have been put together by the artifact evaluation
chairs. These guides describe some best practices and ways to package artifact
for different popular programming workflows, authors should feel free to use
them as starting point and build on them to package and release their artifact.
Note that these resources are not comprehensive, so authors and reviewers are
asked please to not interpret them as the only way to package an artifact (we
also welcome suggestions to these resources in the form of issues, pull
requests, or direct contributions).

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
two weeks after the request. These requested modifications should not be left to
the last minute, if some fixes require more time, authors are encouraged to
communicate a timeline by which these changes will be made for reviewers to best
plan around for their evaluation.

Your cooperation in adhering to these guidelines will greatly contribute to the
efficiency and effectiveness of your submission and review process. We eagerly
anticipate receiving your high-quality contributions and look forward to
showcasing your research!

## Artifact Award
Since PETS 2022, some artifacts are recognized by an [artifact
award](https://petsymposium.org/artifact-award.php). The main objective through
that award is to reward authors that put a lot of effort into the release of
their artifact and to showcase great exemplars of submissions that exceptionally
contribute to the open-science and reproducibility efforts of our community.

Reviewers can nominate the artifact they are assigned to as an award candidate
based on several criteria such as quality, completeness, documentation, ease of
reuse, artifact maturity and audience, interactivity and responsiveness of
authors, etc. Ultimately, nominations are reviewed and ranked.

Our suggestion to authors is really to just prepare and release their artifact
in the same way that they wish anyone in their field would do to facilitate
adoption and reproducibility by others.

# What Makes a Good Review
The goal of the artifact evaluation is to ensure that the released artifacts are
as useful as possible to others. To that end, common best practices and
requirements have been encoded in the form of three different badges:
"Available", "Functional", "Reproduced" that authors can apply towards. Artifact
reviewers are invited to familiarize themselves with the artifact call,
guidelines, requirements, artifact appendix format, and other resources that
have been shared with authors, and to reach out to artifact chairs with any
question or confusion if something is not clear.

Towards the goal of contributing to open-science and reproducibility, the
artifact evaluation process is designed to be interactive; authors are expected
to take into account reviewers' comments and modify their artifact accordingly.
As such, reviewers are kindly asked to start their evaluation as early as
possible and to post reviews or comments that contain sufficient details for the
authors to make the appropriate changes. For example, if the code fails, then
reviewers should include the environment that it is run on, the error messages,
and potential steps that were attempted to fix them. It is crucial for the
process that reviewers discuss and work with authors to help them improve their
artifact: once authors communicate to reviewers that issues were resolved,
reviewers should then take another look and, either, approve the artifact or
provide additional comments if other revisions are needed, until a final
decision is made.

Some reviewing practical tips include:
- Starting the evaluation early.
- Notifying artifact evaluation chairs as soon as possible if missing resources
  or hardware to perform the evaluation.
- Posting a preliminary review and updating it as authors make edits.
- Providing a concise list of issues/suggestions first (this helps give an
  overview to everyone), followed by more details if needed.
- Explicitly numbering or naming these issues/suggestions (this facilitates
  future references to them in comments between authors and reviewers).
- Actively participating in the discussions.
- Kindly pinging authors for updates or for a timeline if no status or answer.
- Staying polite and professional.
- Tagging artifact evaluation chairs if any question or if something need to be
  brought up to their attention.

## Distinguished Artifact Reviewers
Since PETS 2025, we recognize some members of the artifact evaluation committee
as [distinguished artifact
reviewers](https://petsymposium.org/reviewer-awards.php), based on the following
criteria:
- Timeliness, including responding to authors’ updates.
- High quality reviews and discussions that significantly improve the artifact.
- Going above and beyond, helping out with extra reviews, helping with artifacts
  with special requirements, etc.

# Volunteer for the Artifact Evaluation Committee
We are looking for volunteers to serve on the artifact evaluation committee. As
a committee member, you will perform review of artifacts according to the
guidelines above. We are looking for volunteers who will be interested in
providing feedback on documentation and instructions, trying to get source code
to build, or have experience with re-using published datasets. Please fill out
the reviewer nomination form linked in the menu of the PETS website and then
email [artifact26@petsymposium.org](mailto:artifact26@petsymposium.org).

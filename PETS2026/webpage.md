# PoPETs 2026 Artifact Evaluation
PoPETs reviews and publishes digital artifacts related to its accepted papers.
This process aids in the reproducibility of results and allows others to build
on the work described in the papers. Artifact submissions are requested from
authors of all accepted papers, and although they are optional, we strongly
encourage you to submit your artifacts for review.

Possible artifacts include (but are not limited to):
- Source code (e.g., system implementation, proof of concepts)
- Datasets (e.g., network traces, raw study data)
- Machine-generated proofs
- Formal specifications
- Build environments (e.g., VMs, Docker containers, configuration scripts)
- User study questionnaires and aggregate, anonymized results (after ethical considerations)

Artifacts are evaluated by the artifact evaluation committee. Issues considered 
include software bugs, readability of the documentation, appropriate licensing, 
and the reproducibility of the results presented in the paper. After your artifact 
has been approved by the committee,
the paper link on [petsymposium.org](https://petsymposium.org) will be accompanied
by a link to the artifact along with the obtained artifact badges so that
interested readers can find and build upon your work.

## Artifact Submission Guidelines
- All submitted artifacts should be relevant to their corresponding PoPETs
  paper. Please upload a copy of your paper.
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
All source code should be accompanied by a `README.md` file that describes how to 
build and/or run the code. Reviewers will provide feedback on the clarity
of the instructions and attempt to follow them
and build and/or run the code.

Any source code submissions should be accompanied by a build environment such as
a virtual machine (VM) or a Docker container that has been configured with all the
dependencies (software and datasets) necessary to build the code.
- If you provide a VM image, please state how many resources it will consume
  and any configuration steps that are required. Your VM should not
  usually have to download additional dependencies when you run your
  installation scripts. If that is the case, reassess your build process and
  consider making changes to limit the amount of network resources needed.
- We provide artifact reviewers
  with VM instances that can be spawn from HotCRP to perform the evaluation.
  Your artifact, however, should also be executable in general, 
  and not only on these VMs. Hence, your descriptions and scripts should be as
  generic as possible.
- If your artifact runs on cloud computing platforms such as AWS EC2 etc., state the
  amount of money/credits required to run the experiments and provide account
  credentials with enough credits. Our reviewers are _not_ expected to invest their money or
  credit cards to set up accounts. If this cannot be provided, provide an
  alternative way of running your artifact. If this is not possible, reconsider
  your choices of badges (see the FAQ section).

If the code is in a compiled language, the code should compile in the provided
build environment by performing the provided instructions. Compilation and setup
should be automated as much as possible. Ideally, there will be one script that
builds your software, runs your tests, and produces the results in a
comprehensible way.

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
against. (As we detail below, in general, all submitted artifact should apply at least for "Artifact Available" badge, unless doing so would endanger someone.) To ease reviewing effort, we encourage authors to apply appropriately
to all the badges for which they believe requirements are met by their artifact. Our interpretation of the individual badges is aligned with
the one of [other conferences](https://secartifacts.github.io/). If you have questions about which badges to apply for, first go through the FAQ below and then please contact the artifact evaluation
chairs directly.

### Artifact Available
For the "Artifact Available" badge, the reviewers check that the artifact is publicly accessible, has a license and is relevant to the paper.

Your artifact should be publicly accessible at a permanent location; it should _not_ be behind any kind of paywall or restricted access or private repository. If the artifact requires you as an author to manually approve requests for access, it is not public and will not qualify for the "Artifact Available"
badge. Note that all components of your artifact should be publicly available (e.g. source code, datasets etc.). 

Valid hosting options are institutional and third-party digital repositories
(e.g., GitHub, Gitlab, BitBucket, Zenodo, Figshare, etc.). Please do not use
personal web pages or cloud storage services like Google Drive, Dropbox, etc.

#### **Question: I need to upload a file that is larger than 100MB, but [Github does not allow that](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#about-size-limits-on-github). How can I make my file available?**

- If your file is at most 2GB, Github recommends [using Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage). 
- If your file is at most 50GB, then you should consider [hosting it as a record on Zenodo](https://support.zenodo.org/help/en-gb/1-upload-deposit/80-what-are-the-size-limitations-of-zenodo). Artifacts have also used [Huggingface](https://huggingface.co/docs/hub/en/storage-limits) successfully to host large ML models.  
- If directly uploading your file to one of the aforementioned platforms does _not_ work, then you may split the file into multiple chunks. You can also contact the artifact chairs if you have trouble with this step. 
- Do **not** use Google Drive or Dropbox links; they are not version-controlled in any way. 

#### **Question: My paper has several artifacts, such as one source code repository and few datasets, or  multiple source code repositories for different purposes. What should I submit for the "Artifact Available" badge?** 

We will need a single link to put on the PETS website and all artifacts
associated with your paper should be discoverable from that one link. 
- If you have several Git repositories, we suggest using [git
submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
- If you are using Zenodo to host your datasets and a Git repository for your code, ensure that your README.md in your Git repository includes a link to the Zenodo record, and you may submit your Git repository for artifact evaluation. 

#### **Question: Which license should I choose for my artifact?**
- For a clear, easy to follow guide see: https://choosealicense.com/
- For more in-depth detail on open source and copy-left licenses, see
  https://www.gnu.org/licenses/license-list.en.html and
  https://opensource.org/licenses.
- Before you begin extending other authors' libraries, check that doing so would comply with the terms of the license.

#### **All submitted artifacts should apply at least for "Artifact Available",**
unless doing so could endanger someone. For instance, if the artifact demonstrates exploiting a
vulnerability and responsible disclosure is in progress and has not been completed yet, making the artifact available would harm users. In this case, authors could
apply for just the "Functional and Reproduced Badges". 

#### **Question: I want to commercialize my artifact. Should I still apply for any badges?** 
IP protections and commercialization prospects should not inhibit authors from applying for the
"Artifact Available" badge. For instance, authors can choose restrictive licenses that
prohibit others from using their code. Alternately, authors can design a smaller working prototype to
demonstrate reproducibility of the contributions of their paper.

#### Checklist for "Available Badge":
- [ ] Publicly available artifact with a single link.
- [ ] Presence of license.
- [ ] Relevance to paper.
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

This badge does *not* mean that the reviewers have checked that the code executes or that they have 
  reproduced the results of the paper.

### Artifact Functional
To be awarded the "Artifact Functional" badge the artifact should satisfy these
criteria:
- Documentation: The artifact clearly documents how it should be used (i.e., installation + execution).
- Completeness: It includes all key components described in the paper.
- Exercisability: It includes the scripts and data needed to run the experiments
  described in the paper. The software must successfully execute in
  the provided environment.

[//]: # (Some artifacts may not, by definition, be able to satisfy the completeness or)
[//]: # (exercisability criteria. For instance, an artifact may have a proprietary)
[//]: # (machine learning model as a key component of the system, and so, achieving)
[//]: # (completeness may be difficult. Artifacts may rely on datasets that may contain personally identifiable information or datasets that cannot be released under the licensing terms, and so,)
[//]: # (satisfying exercisability may be difficult.)

Consider the experiments in your artifact as arranged in a pipeline of multiple
stages, such as data collection, data processing, and producing plots or tables
for the paper. The "Completeness" and "Exercisability" criteria require each
stage to be represented. Present each stage, even if it cannot be fully run. These can be represented in either a simplified manner or run on dummy data to check the functionality of the stage. If
possible, provide the expected outcome of the fully run stage such that
preceding stages are performed on 'real' data again. Under the FAQ, we provide some specific examples on how authors can still
prepare their artifact for the "Artifact Functional" badge in these cases.

#### Checklist for "Functional Badge":
- [ ] Meets "Available Badge" requirements. 
- [ ] Clear documentation is provided.
- [ ] Completeness criterion fulfilled (with potential limitations reasonably
  argued).
- [ ] Exercisability criterion fulfilled (with potential limitations reasonably
  argued).
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

### Artifact Reproduced
The "Artifact Reproduced" badge requires the main claims of the paper to
be reproduced by the reviewers. Implicitly, an artifact awarded the "Artifact Reproduced" badge needs to
also meet the requirements of the "Artifact Functional" badge.

Authors must specify the commands to run the
artifacts clearly and describe how to reproduce each main claim of the paper.
Best practice is to point out which part of the paper is reproduced by a given
script, e.g., name the table or figure. Also, the authors must highlight which
results of the paper that are not reproducible with the given artifact and
explain why. Authors are encouraged to contemplate how
their artifact could be re-used by others in the future and describe potential
ways for improvement, etc.

Authors are asked to automate as much of the execution of the
experiments as possible; manual effort from reviewers to run and interpret the results
should be minimized. For instance, if an experiment is performing a swap
across different parameters, a script automating it should be provided. Ideally,
results should also be automatically parsed and output in a comprehensible way, as close to the output in the paper as possible (table or figure etc.).

To award the "Artifact Reproduced" badge, reviewers must be able to reproduce the main claims of the paper with the provided
artifact. As a rule of thumb, a quantitative claim should generally be
considered reproducible if the results obtained by reviewers are within 5% of
the reported value in the paper. That being said, some artifact-specific factors
may prevent this; in these cases, artifact reviewers should also consider if the
results that they obtain align qualitatively with the claims made in the paper.
It is the reviewer's role to enforce that these quantitative and/or qualitative
expectations are met before awarding the "Artifact Reproduced" badge.

Additionally, some experiments may by nature be harder to fully reproduced
during the timeframe of the artifact evaluation: e.g., take a while to run, need
several iterations, train a model on a large dataset, etc. In these cases,
authors should still provide the instructions and expected results for the
"long" version of the experiment, and also for a simplified one (e.g., fewer
iterations, smaller dataset, etc.). Indeed, even on a simplified version or
fewer runs, reviewers should still somewhat be able to look at the results and
the standard deviation, and check that results from the paper can be reproduced.

Finally, some artifacts, such as longitudinal studies or hardware-based
contributions, may be infeasible for the “Artifact Reproduced” badge (see FAQ below), as reviewers have limited time and only commodity hardware
available. Nevertheless, these authors can and should still prepare their
artifacts for the “Artifact Functional” badge.

#### Checklist for "Reproduced Badge":
- [ ] Meets "Functional Badge" requirements.
- [ ] List of the core contributions and claims of the paper identified.
- [ ] Clear mapping between claims, experiments, and results provided.
- [ ] Minimal amount of manual effort required from reviewers, i.e., fair amount
  of automation.
- [ ] Reviewers obtain reproducible results quantitatively (i.e., within 5% of
  the claimed value) and/or qualitatively.
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

### Artifact Link
When the artifact evaluation is over, a persistent and stable link pointing to
the final evaluated version of the artifact will be collected for each accepted
artifact. Depending on the
hosting option picked, this is likely a link to a specific Git commit/tag or a DoI for a Zenodo record etc. 
This link and the awarded badge(s) will be added to the website next
to the corresponding paper title. As updates to the artifact are likely to occur
to address reviewers' feedback, we will only collect this link after a final decision is made.

### Frequently Asked Questions

#### **Question: I have a user study. How can I get the Artifact Available badge?**

An example of a [good user study artifact](https://github.com/blues-lab/priv-eng-dataset/tree/ca35ffbb3c38ff7877c01ee92bfda29b2033ae6e) is available here. Authors of papers with user studies can generally achieve the "Artifact Available" badge, by including the following in their artifact:
- user study questionnaire
- if participants were informed of, and consented to, _anonymized_ transcript or responses being released, explicitly mention this, and release these transcripts or questionnaire responses.
  We also recommend including demographics of your user study participants.

#### **Question: I am designing a course or a game to teach privacy. Hpw can I get the Artifact Available badge?**

Here are examples of artifacts regarding [an undergraduate course](
https://github.com/MaishaB/undergraduate-privacy-curriculum/tree/0a7f27a8b4220298040323fb100daa658583717b) and a [game](https://github.com/DataSmithLab/Panopticon/tree/236b792058b2cc65a43c55b624bb4649b4bbd328) to teach privacy.

For courses, thoroughly document the course structure, including the number of lessons or modules, lesson titles, number and types of assessments. You should also include:
- written and programming exercises
- tutorials
- assessments, including quizzes or exams.

For games, document the game mechanics, game materials, setup instructions as well as per-round instructions. You may include videos to supplement, but not replace, your documentation.

While in general we expect both game and course-related artifacts to be awarded the "Artifact Available" badge, the aforementioned artifact included programming exercises that could be fully exercised by the reviewers and was thus awarded the "Artifact Functional" badge.

#### **Question: My paper involves a large dataset, machine learning (ML) model, or other such large files. How can I get the Artifact Functional badge?**
If a large dataset, ML model, or other file is required to execute the presented
tool, the authors should provide it, unless it is proprietary. If they can not
share the dataset or model, we expect them to share a synthetic dataset or dummy
model, which may, perhaps perform worse, but which can be used to test the
principle functionality of the presented tool. Ideally, authors should provide
the code to train the original model, though depending on the contributions of
the paper, it need not be executed. 

Authors should note that the hosting options listed under the "Artifact Available" badge have
different file size limits and constraints and that dividing or compressing such
large files may be needed. Please refer to the instructions under the "Artifact Available" badge on how to upload large files to your repository. 

#### **Question: My experiment has a lengthy runtime or requires a large amount of compute resources. How can I get the Artifact Functional badge?**
Although experiments may require days or weeks of compute time on commodity
hardware, the "Artifact Functional" badge can usually still be achieved, by following _each_ of the steps below.
- Provide a simplified version of the experiments, which may run on fewer data or fewer epochs of time, in order to enable the reviewers to check the functionality of that stage. If
  the results of the simplified experiments align with the ones reported
  in the paper, then authors can also aim for the "Artifact Reproduced" badge.
- Provide results of the full experiment in the repository, so that reviewers can
  verify the functionality of the later stages with these results.

#### **Question: My paper involves a longitudinal study or crawl. How can I get the Artifact Functional and Reproduced badges?**

Authors should provide:
- Anonymized raw data, unless forbidden by legal requirements,
  privacy, or ethical concerns. In this case, authors should include
  a dataset with dummy or synthetic data should be included. Please follow the instructions above (under the "Artifact Available" badge) to upload large files to your artifact.
- Evaluation scripts to reproduce the results of the paper. Reviewers should be able to execute the evaluation scripts on either anonymized raw data or dummy data.

#### **Question: My paper involves a hardware-based contribution. How can I prepare my artifact?** 
- If the artifact requires GPU VMs, Trusted Execution Environments, IoT devices and Smartphones, ensure that you indicate this at submission time.
- If other special hardware is required, then artifact chairs will attempt to procure the hardware from other artifact evaluation committee members. If this is not possible, then the artifact chairs may require authors to be involved in a video call to evaluate the artifact for the "Artifact Functional" and "Artifact Reproduced" badges. 
- The authors may also simulate the hardware, though this is challenging.
- Authors should additionally publish the raw results of the experiments, so that reviewers can
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
fresh install (or ask a friend to do so) and fix potential issues that
are uncovered before submission.

Authors are also encouraged to check out the [resources and
examples](https://github.com/PoPETS-AEC/examples-and-other-resources) of
artifact packaging that have been put together by the artifact evaluation
chairs. These guides describe best practices to package the artifact
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
Since PETS 2022, distinguished artifacts are recognized by an [artifact
award](https://petsymposium.org/artifact-award.php). The main objective through
that award is to reward authors who put a lot of effort into the release of
their artifact and to showcase exemplar submissions that contribute to the open-science and reproducibility efforts of our community.

From PETS 2025 onwards, we have provided explicit criteria for reviewers to judge whether an artifact should be nominated for this award. Reviewers should consider the artifact quality, completeness, documentation, ease of reuse, artifact maturity and audience, interactivity and responsiveness of
authors, etc. Ultimately, nominations are reviewed and ranked.

Our suggestion to authors is to simply prepare and release their artifact
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
reviewers should then take another look and either approve the artifact or
provide additional comments until a final
decision is made.

Some reviewing practical tips include:
- Starting the evaluation early.
- Notifying artifact evaluation chairs as soon as possible if you are missing resources
  or hardware to perform the evaluation.
- Posting a preliminary review and updating it as authors make edits (an
  "[EDIT]" tag or striking out text can be useful to indicate modified and/or
  solved comments, etc.).
- Providing a concise list of issues/suggestions first (this helps give an
  overview to everyone), followed by more details if needed.
- Explicitly numbering or naming these issues/suggestions; doing so facilitates
  future references to them in comments between authors and reviewers.
- Actively participating in the discussions.
- Politely pinging authors for updates or for a timeline if no response is received to your comments after a week.
- Staying polite and professional.
- Tagging artifact evaluation chairs if you do not hear back from the authors, or if something needs to be brought up to their attention.

## Distinguished Artifact Reviewers
Since PETS 2025, we recognize some members of the artifact evaluation committee
as [distinguished artifact
reviewers](https://petsymposium.org/reviewer-awards.php), based on the following
criteria:
- Timeliness, including responding to authors' updates.
- High quality reviews and discussions that significantly improve the artifact.
- Going above and beyond, such as by helping out with extra reviews, helping with artifacts
  with special requirements, etc.

# Volunteer for the Artifact Evaluation Committee
We are looking for volunteers to serve on the artifact evaluation committee. As
a committee member, you will perform review of artifacts according to the
guidelines above. We are looking for volunteers who will be interested in
providing feedback on documentation and instructions, trying to get source code
to build, or have experience with re-using published datasets. Please fill out
the reviewer nomination form linked in the menu of the PETS website.

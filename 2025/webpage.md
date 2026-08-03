# PoPETs Artifact Evaluation

PoPETs reviews and publishes digital artifacts related to its accepted papers. This process aids in the reproducibility of results and allows others to build on the work described in the papers. Artifact submissions are requested from authors of all accepted papers, and although they are optional, we strongly encourage you to submit your artifacts for review.

Possible artifacts include (but are not limited to):

- Source code (e.g., system implementations, proof of concepts)
- Datasets (e.g., network traces, raw study data)
- Scripts for data processing or simulations
- Machine-generated proofs
- Formal specifications
- Build environments (e.g., VMs, Docker containers, configuration scripts)

Artifacts are evaluated by the artifact evaluation committee. The committee evaluates the artifacts to ensure that they provide an acceptable level of utility. Issues considered include software bugs, readability of the documentation, appropriate licensing, and the reproducability of the results presented in the paper. After your artifact has been approved by the committee, we will accompany the paper link on petsymposium.org with a link to the artifact along with the obtained artifact badges so that interested readers can find and use your hard work.

## Artifact Submission Guidelines

- All submitted artifacts should be relevant to their corresponding PoPETs paper. Please upload a copy of your paper.
- Many papers have several artifacts (e.g., multiple source code repositories, datasets, build environments), which is great! Please keep in mind that we'll need a single link to put on the PETS website and that all artifacts associated with your paper should be discoverable from that one link.
- Please include a README.md file with your submission that briefly explains the type and purpose of the artifact. At a prominent position in the README.md file make clear to which paper the artifact belongs and how the artifact is relevant to the paper.
- Please include the [ARTIFACT-EVALUATION.md](ARTIFACT-EVALUATION.md) file in your artifact (either include it in the README.md file or add it as a separate file.). It is important for the reviewers during the reviewing process. Provide a direct link to that file at the submission page.


### Source Code Submissions

- All source code should be accompanied by a README.md file or other documentation that describes how to build and/or run the code. Reviewers will provide feedback on the clarity of the instructions and attempt to follow them and build and/or run the code.
- Any source code submissions should be accompanied with a build environment such as a virtual machine or a Docker container that has been configured with all the dependencies and prerequisites necessary to build the code. If you use a virtual machine, please state how many resources it will consume and any configuration steps that are required. Your virtual machine should not usually have to download additional dependencies when you run your install scripts. If that is the case, reassess your build process and consider making changes to limit the amount of network resources needed. You can also use one of the VM images provided by us, which you can spawn from within HotCRP. In this case please provide the name of the used image. Please keep in mind that our VMs are only available to the reviewers and you, to ease the process, and they are not available to the public. Your artifact, however, should also be runnable and helpful for the general public. Hence, your descriptions and scripts should be as generic as possible. If your artifact runs on compute providers, like AWS or similar, state the amount of money/coins required to run the experiments and provide account credentials with enough coins. Our reviewers won't invest their money or credit cards to setup accounts. If this cannot be provided, provide an alternative way of running your artifact. If this is not possible,reconsider your choices of badges (see below).
- If the code is in a compiled language, the code should compile in the provided build environment by performing the provided instructions.
- Compilation and setup should be automated as much as possible. Ideally, there will be one script that builds your software, runs your tests, and produces the results in a comprehensible way.
- Please ensure that your code has an license and clearly states this information. The following resources may help you to choose a license:
    - For a clear, easy to follow guide see: https://choosealicense.com/
    - For more in-depth detail on open source and copy-left licenses, see https://www.gnu.org/licenses/license-list.en.html and https://opensource.org/licenses
- Our goal is that the artifacts are useful for as long as possible. Some tips on improving the longevity of your source code artifact are:
    - Include the versions of your software's dependencies wherever possible.
    - Mention specific hashes of git commits that match the state your artifact was in at the time of submission.
    - Virtual machines and Docker images will last longer than Docker files and allow researchers to more accurately reproduce your exact execution environment (though the trade off is that they will be larger)
    - Artifacts are not required to be able to run on all hardwares and OSes. If your artifact requires any particular hardware/OS, please make it clear in the submission.

### Dataset Submissions

- All datasets should be clearly documented in a way that allows researchers working on similar problems to re-use the dataset for their work.
- If the dataset includes survey results, provide a copy of the original survey with raw results. This is vital for replication studies and helping researchers interpret the context of your results.
- Please state the sizes of datasets in the documentation.
- It's encouraged to accompany the data with processing scripts that produce the graphs or statistical output that appear in the paper.

## Artifact Badges

Each accepted artifact can be granted up to three badges. During the submission, the authors must select which badges they want their artifacts to be evaluated against. We encourage the authors to choose the badges appropiately, to ease the reviewing effort. Our understanding of the individual badges is aligned with other conferences, e.g., [USENIX SS](https://secartifacts.github.io/usenixsec2023/badges)

### Artifact Available
This "Artifact Available" badge indicates that the artifact is publicly available at a permanent location (not be behind any kind of paywall or restricted access). If the artifact requires you as an author to manually approve requests for access, it is not public and will not qualify for the "Artifact Available" badge. If you have concerns or questions about this badge please contact us directly. Valid hosting options are institutional and third-party digital repositories. Please do not use personal web pages. The link should be persistent; for repositories that evolve over time (e.g., Git repositories), please specify a specific commit-id or tag to be evaluated. The reviewers check that the artifact can be retrieved, and that it includes a license. The reviewers check that the artifact is relevant to the paper. This badge does *not* mean that the reviewers have reproduced the results or checked that the code executes or that they have reproduced the results for full functionality.

### Artifact Functional
For the "Artifact Functional" badge the artifact should satisfy these criteria:
- Documentation: It clearly documents how it relates to the paper, and how it should be used.
- Completeness: It includes all the core contributions described in the paper.
- Exercisability: It includes the scripts and data needed to run the experiments described in the paper. The software must be successfully executable?

Some artifacts may not, by definition, be able to satisfy the completeness or exercisability criteria. For instance, an artifact may have a proprietary machine learning model as a key component of the system, and so, achieving completeness may be difficult. Artifacts may rely on datasets that are too large to be included, or contain personally identifiable information, and so, satisfying exercisability is difficult. We guide authors below, using some examples, on how they can still prepare their artifact to achieve this badge. Additionally, some artifacts, such as longitudinal studies or hardware-based contributions, may be infeasible for the “Artifact Reproduced” badge (see below), as reviewers have limited time and only commodity hardware available. Nevertheless, these authors can prepare their artifacts for the “Artifact Functional” badge, as described in the examples:

#### Examples
Consider the experiments in your artifact as arranged in a pipeline of multiple stages, such as data collection, data processing, and producing plots or tables for the paper. The “Completeness” and “Exercisability” criteria require each stage to be represented. Our key advice is to present each stage, including the ones that cannot be fully run. These can be represented in either a simplified manner or run on dummy data to check the functionality of the stage. If possible, provide the expected outcome of the fully run stage such that preceeding stages are performed on 'real' data again. In the following we present some examples:

**Tools based on large machine learning (ML) models.** If an ML model is required to execute the presented tool, the authors should provide it, unless it is proprietary. Authors may use `git-lfs` to commit large model files to their repository. If they can not share the model, we expect them to share a dummy model, which may perhaps perform worse, but which can be used to test the principle functionality of the presented tool. Ideally, authors should provide the code to train the original model, though depending on the contributions of the paper, it need not be executed.

**Lengthy experiment runtimes.** Similar to the point above, even if the experiment requires days or weeks of compute time on commodity hardware, the "Artifact Functional" badge can be achieved. In such cases the authors should also provide a simplified version of the experiment, which may run on less training data or for fewer epochs of time, in order to enable the reviewers to check the functionality of that stage. Authors should additionally provide results of the full experiments in the repository, so that reviewers can verify the functionality of the later stages with these results.

**User studies, longitudinal studies and crawls.**  Some studies cannot be repeated within the reviewing process. However, the authors should provide the evaluation scripts to reproduce the main results of the paper. Pseudonymized raw data should also be provided, unless forbidden by legal requirements, privacy, or ethical concerns. In such cases, a data set with dummy data should be included. Reviewers should be able to execute the evaluation scripts on either the pseudonymized raw data or dummy data.

**Hardware-based contributions .** If the artifact requires certain hardware, please request for it within the "hardware requirement" section in the [ARTIFACT-EVALUATION.md](ARTIFACT-EVALUATION.md) template. If special physical setups are required, the authors may simulate the hardware. Authors should publish the raw results of the experiments, so that reviewers can verify the remaining stages as functional.

### Artifact Reproduced
The "Artifact Reproduced" badge requires the core contributions of the paper to be reproduced by the reviewers. Authors must specify the commands to run the artifacts clearly and describe how to reproduce each core finding of the paper. Best practice is to point out which part of the paper is reproduced by a given script, e.g., name the table or figure. Also, the authors must highlight which results of the paper are not reproducible with the given artifacts and argue why. Note that minor additional experiments that do not significantly contribute to the paper may not be included in the artifact.

# What makes a Good Submission

To ensure a smooth submission process, please follow these important guidelines:
Firstly, authors should fill out the [ARTIFACT-EVALUATION.md](ARTIFACT-EVALUATION.md) file provided and include it in their artifact (either in the README.md file or as a separate file). Mention the badges you deem reasonable for your artifact and, if necessary, describe which stages are simplified or skipped and why. This will help the reviewer better understand your work and ensure a seamless review process. Secondly, prompt communication is essential. Authors are kindly requested to respond to reviews and comments within a time span of two weeks. This will facilitate constructive discussions and allow for timely feedback incorporation. Lastly, in the event that changes are requested during the review process, we kindly ask authors to endeavor to incorporate them, at least partially, within two weeks after the request. Your cooperation in adhering to these guidelines will greatly contribute to the efficiency and effectiveness of our submission and review process. We eagerly anticipate receiving your high-quality contributions and look forward to showcasing your research!

# What Makes a Good Review

The goal of our artifact evaluation is to ensure the artifacts are as useful as possible. Towards this goal, artifact evaluation process is interactive and we expect the authors to take into account the reviewers' comments and modify their artifacts accordingly. As such, the reviews should contain sufficient details for the authors to make the appropriate changes; for example, if the code fails, then the review should include the environment that it is run on and the error messages. After the authors have fixed the issues, they will add a comment on the submission site, at which point the reviewers can either approve the artifact or provide additional comments for another rounds of revision.

# Volunteer for the Artifact Evaluation Committee

We are looking for volunteers to serve on the artifact evaluation committee. As a committee member, you will perform review of artifacts according to the guidelines above. We are looking for volunteers who will be interested in providing feedback on documentation and instructions, trying to get source code to build, or have experience with re-using published datasets. Please email artifact25@petsymposium.org to be on the artifact evaluation committee.

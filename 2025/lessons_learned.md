## Call for Artifact

- Better guidelines around hardware requirements (i.e., SLURM cluster, etc.),
  can authors provide a smaller example on which it is somewhat aligned with
  results in paper?

- Private dataset? Submit a synthetic one to release your code and obtain
  functional badge

- Award / Distinguished artifact reviewer: We’ve made a list of distinguished
  reviewers this cycle, based on:
  - a) timeliness, including responding to authors’ updates
  - b) high quality reviews that significantly improve the artifact
  - c) helping out with extra reviews e.g. for artifacts with resources.

- No GG drive link allowed -> authors should use of Zenodo, figshare, GIT LFS,
  etc.

- Artifact submission deadlines to sync with revision/acceptance notifications
  (to leave enough time to authors to get things ready)
  - Currently, the artifact submission deadline is 3 weeks after the paper
    acceptance notification for that round. But in practice, we have waited
    until we receive the list of major revisions as well from the PC chairs, so
    each round is delayed. This back loads the last round where we had 40
    artifacts in the last round, which was difficult to manage.

- Distinguishing between the Functional and Reproduced badges: we should be
strict in that the reproduced badge should, successfully reproduce **all**
results of the paper. The onus should be on the reviewers to check that. Papers
that do some results but not all, for example, should not get this badge (except
if well justified).
  - Okay if some experiments are not reproduced but make sure the Notes for
Reusability or Limitations section is clear.

## Submissions

- Check badges applied for after submissions are in and see if we need to
  pre-emptively reach out to authors about something (available not applied for,
  etc.)

- Create spreadsheet for overview of papers/reviews/PC

## Tips for discussions and interaction

- Stay polite even if authors might not appear to be

- Provide clear and concise list of changes (defer to details after)
  - Number the asks, this makes it easier for authors to refer back to them


## HotCRP instance

- 1 per issue - first round needs to be ready for September usually

- Keep all communications through HotCRP for better context, don’t tell authors
  that they can email the chair alias to update their artifact link, etc.

- There is a known issue that authors comments are not visible until reviewers
  have posted their reviews: https://github.com/kohler/hotcrp/issues/312

- Hide award score to authors

- Separate sections for each badge will clarify things
  - Add a section “response to authors”? or tell reviewers that they *should*
    continuously edit their review and put a tag like "[EDIT]" or something
  - Guidelines to reviewers to post a review and keep updating it along with the
  comments and answers from the authors


- ~~We should add a field into the submission form with the final link and the~~
  ~~authors should put in the final link there. Then, I wonder if we can use
  the~~ ~~“Collect final submissions” feature in HotCRP to get all the paper
  title,~~ ~~decision (badges) and submission links.~~
    - Unfortunately, the "collect final submissions" feature was designed for
      PDF files
    - Let's figure it out manually every time we post the message with decision
      on badges to authors and we ask authors if they are okay with the link

- Optional hotcrp field for ssh keys / credentials

- To improve bidding: ask for type of artifact, resources, required, specific
  hardware as **topics**

- Make comments/interactions visible to any reviewers as long as they are not
conflicted (not only artifact you are assigned):
  - Other reviewers’ for the same artifact make their names visible
  - Allow reviewers to see the comments and discussion on other artifacts

- Use score/rate review feature for distinguished artifact reviewers and
  encourage reviewers to rate each other


## For authors
- Do not link to a specific commit in the documentation at submission: this will
  likely change during the review process

- Test yourself or ask a friend to check your artifact instructions from a fresh
  install - it helps debug most of the issues artifact reviewers encounter when
  trying to install./deploy the artifact (reviewers are **not** alpha testers)

- Process is supposed to be interactive, update your artifact as the discussion
  goes (do not wait until last minute to address all required changes, do it
  continuously)

## For reviewers
- Provide checklist or clearer guidance for badges

- Known hotcrp issue comment visibility if review not posted
  https://github.com/kohler/hotcrp/issues/312


- Responsiveness: regularly emailing the reviewers e.g. once every week or even
  more, helps with reducing the number of late reviews.
  - Reviewers tend to inform chairs when they have life stuff going on
    (emphasize in emails to let us know the earliest possible so that we can
    assign the review to someone else)
  - Non-responsive reviewers lead to other reviewers having to pick up the
    slack, and needs to be selective who we extend the invite to, especially
    when reviewers are non-responsive for multiple rounds.


- Formalizing criteria for selecting the artifact award and what reviewers
  should keep in mind for the “Award Worthiness” button

  - Only 1 reviewer for artifacts that are available?
  - 2 reviewers for functional
  - 3+ reviewers reproduced
  - Shepherding for getting reviews and artifacts to final stage => Empower a
    reviewer to be a shepherd/discussion lead and make sure the artifact is
    finalized?


- ICS calendar with deadlines like done for regular PETS’26 PC?

## Other

- IoT device needed:
  - We did a couple through video calls with authors in the past (not ideal)
  - What are other AECs doing?
  - Access to infrastructure for reproducibility: the Sphere project is
    interested in this. https://sphere-project.net/


- Artifacts that require keys to access cloud APIs. Generally, authors have
  shared their own test keys. We should add an optional text field to the HotCRP
  submission form asking authors to provide a set of test keys to access cloud
  services etc.


## Examples needed

- Dockerfile for GPU here https://github.com/sacs-epfl/shatter with CI

- FAQ:  for submodules (SSH vs HTTPs), VPN&SSH Access (tailscale, key pair,
  etc.)

- Privacy-preserving ML datasets -> limit on GitHub LFS - Zenodo for datasets is
  the way to go - No Google Drive links at all -> 50GB on Zenodo, you can
  request an increase

- Papers that involve multiple repositories- they almost always do it without
  using submodules -> give instructions for submodules


- Zenodo link for dataset in documentation - bash script to download

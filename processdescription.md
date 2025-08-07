# Process Description for (new) Artifact Evaluation Co-Chairs
On this page introduce some of the involved processes we have in the Artifact
Evaluation.

## Starting a new year for artifact review

Each August, just as PoPETs starts a new review cycle, we also start a new
review cycle for artifact review. There are a few things that need to be done to
set things up.

### Inviting artifact committee members

We need to make sure the artifact committee PC is ready to go by the first round
deadline (cf. [deadlines.md](PETS2026/deadlines.md)). We usually send an
invitation email with stats from the previous year and changes for the upcoming
year. This email is sent in three variants:
- [One version](EmailTemplates/) to the existing artifact committee.
- [Another version](EmailTemplates/) to author as new potential committee
  members.
- [And third one](EmailTemplates/) to new nominated persons.

There is an option to sign up or nominate people to be on the artifact
committee in the "Reviewer Nomination Form". If you have not gotten the list of
artifact reviewers from the current chairs, you can try reaching out to them.
We've gotten a large list of reviewers this way.

Once an artifact reviewer has replied to the invitation email, add them to the
HotCRP instance. (See below.) You should also email the publicity chairs to
update the list of committee members.

## Starting a new round of artifact reviews

### Creating a new HotCRP instance

We now use separate instances for different rounds. You'll need to email the
PoPETs HotCRP admin to create a new instance. The URL for the artifact
submission site has been https://artifact.petsymposium.org/artifactYYYY.R where
YYYY is the 4 digits of the upcoming year and R is the round number. As an
example, in November of 2023 we are now setting up the instance for the 2024
round 2 submission year and so the submission site is
https://artifact.petsymposium.org/artifact2024.2.

The current HotCRP admin is Ian Goldberg. For up to date information, check for
the "Infrastructure Chairs" on this year's CFP.

If this is the first round, you will have to add the email addresses of the
reviewers that accepted the invitations directly. If this is not the first
round, then HotCRP admin can run a script to copy over the email list from the
previous round.

### Configuring the HotCRP instance

There is not much configuration necessary to accept submissions. Make sure you
open submissions for the first round and set the submission deadline if desired.
In the settings menu, select the "Submission Form" setting. Make sure both an
abstract and PDF are required. Add a new submission field titled "Artifact link
and brief description" of type "multiline text". Set the topics so reviewers can
indicate preferences. So far we've used "source code", "data sets", and "other"
but feel free to experiment :)

We recently added an indicator for specialized hardware, this helps for
identifying artifacts that we may need to reach out to external reviewers for.

Make sure you select "Save changes" before leaving the screen.

You will also want to ensure the review form has been configured to the
preferred information. (e.g. artifact readiness, artifact award worthiness)

Text Input, label: Artifact Summary Text Input, label: Comments to authors
Artifact Readiness
1. Not suitable for review
2. Needs work
3. Ready

Award Worthiness (Configure as not visible to authors)
1. Not suitable
2. Perhaps suitable
3. Definitely consider

## Process Change Recommendations/For Consideration
- Clarification in call as to expectations (functionality and availability
  required)
- Add section to artifact review form for response to authors/updates. Several
  reviewers have been updating their review and labeling it but others have not.
  This will make things clearer for all involved
- Instructions to reviewers doc: include information about courtesy, types of
  good comments/evaluations, etc.
- Add deadline for artifacts to reach acceptance stage to prevent too much
  overlap with other rounds and to prevent limbo states for becoming too
  prolonged

Pre-2023 TODO List:
- turn readme into a table of contents/guide to access other information in the
  repository as it expands. e.g. there could be a for authors, for reviewers,
  for chair breakdown
- Make new reviewer doc. Include: typical timelines, reviewing advice, FAQ
- create list of questions as they come up to eventually generate FAQ for
  reviewers and authors of artifacts

## General Notes in Progress
After a paper has been accepted to an issue of PoPETs the list of accepted
papers is sent to the artifact chairs by the current program chairs. This list
will be used to generate the HotCRP accounts and send out an invitation to
submit an artifact to all authors.

All accepted artifacts should be emailed to the maintainer of the PoPETs
website. We typically send the paper title and the artifact link.

Reoccuring todo list
- update committee on website

## Notice to Authors Timeline
The invitation should include:
- timeline estimates for authors
- explanation of the process
- link to call for artifact page with information on what is an artifact
- contact info for chairs

Authors are invited to submit an artifact approximately x time intervals after
their paper has been accepted. They will have an interval of y time to prepare
their artifact and submit it. After submission reviews will be received
(ideally) after z weeks. This normally corresponds to the camera ready paper
deadline. The authors will then receive an email informing them there are
reviews available and they can begin responding to the reviews to improve their
artifact and move it towards submission. This iterative process will continue
for the specified time duration and then a decision will be reached. After a
decision has been reached there is no further action required on the part of the
authors.


## Notice to Reviewers Timeline



## Sending out Mail via HotCRP
Currently use one instance for all issues. Be very careful to select the correct
ones. For example: sent to all authors without decision versus send to all
authors. It's difficult to filter authors so either do it by hand or you can
also select for authors with unresolved submissions or something like that.

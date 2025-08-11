# Process Description for (new) Artifact Evaluation Co-Chairs

On this page, we introduce some of the processes we have in place for the
Artifact Evaluation of PETS

## New artifact chair

- Send email to candidate that was picked
- Video call for onboarding
- Give access to GitHub organization, Slack with other Artifact chairs from
  other conferences, create artifactYY@email alias
- Make admin on past year’s instances to navigate and poke around (familiarize with things)
- Attend current PETS if possible
- Help with potential backlog of artifact reviews
- Help extract statistics, review slides for town hall, awards, BoF session,
  etc.

## Role of artifact chair


- Overview role: preparing submission servers for artifacts, updating calls,
  fixing deadlines, putting together a PC, managing submissions, bidding,
  assigning reviews, sharing with publicity chairs the list of accepted
  artifacts, communicating with chairs from regular PC for artifact invite
  (initial email being sent to authors), maintaining list of authors and papers
  from previous rounds and status.

- A lot of emails and reminders to stay on top of things for each round.

- Appointed for 2 years for overlap with previous co-chair and next one. In the
past, the system has been that the old chair leads the new chair through the 1st
and 3rd rounds, and the new chair does the 2nd and fourth rounds. But, it can be
overwhelming handling the last round alone since usually there are double as
many artifacts as in the previous rounds.

- Finalizing the list of all papers, with their final badges (which may differ
  from the initial ones) and their final links to be sent to the web chairs

- Infrastructure Chair deploys the hotcrp instance and configures email alias
  for chairs

- Artifact Infrastructure Chair for the VMs (Tobias Fiebig) “Technically, this
is not me, but https://measurement.network providing the service... but I am
currently the main person doing things there (frantically trying to onboard
more, but still a way to go. ;-))”

## Starting a new year for artifact review

Each August, just as PoPETs starts a new review cycle, we also start a new
review cycle for artifact review. There are a few things that need to be done to
set things up.

### Inviting artifact committee members

We need to make sure the artifact committee PC is ready to go by the first round
deadline (cf. [deadlines.md](PETS2026/deadlines.md)). We usually send an
invitation email with stats from the previous year and changes for the upcoming
year. This email is usually sent in three variants:
- One version to the existing artifact committee.
- Another version to author as new potential committee members.
- And third one to new nominated persons.

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
round, then the HotCRP admin can run a script to copy over the email list from
the previous round.

### Configuring the HotCRP instance

Other than adding the PC, editing the submission form, and review form, there is
not much configuration necessary to accept submissions. Just make sure to open
submissions when the HotCRP instance is ready. Also make sure you select "Save
changes" before leaving the screen.

For the "Submission Form", make sure both an abstract and PDF are required. Add
a new submission field titled "Artifact link and brief description" of type
"multiline text". Set the topics, so reviewers can indicate preferences and
authors can indicate the need for specialized hardware through the topics. This
also helps for identifying artifacts for which we may need to reach out to
external reviewers.

Configure the "Review form" accordingly.

You can see the [HotCRP site configuration used in 2026 here](/PETS2026/hotcrp-site-configuration.json)


## Invite to submit an artifact and badge notification
After a paper has been accepted to an issue of PoPETs the list of accepted
papers is sent to the artifact chairs by the current program chairs. This list
will be used to send out an invitation to submit an artifact to all authors.

All accepted artifacts should be emailed to the maintainer of the PoPETs
website. We typically send the paper title and the artifact link as well as
badge(s) awarded.

Re-occurring ToDo list:
- update committee on website

## Notice to Authors Timeline
The invitation should include:
- timeline estimates for authors
- explanation of the process
- link to call for artifact page with information on what is an artifact
- contact info for chairs

Authors are invited to submit an artifact after their paper has been accepted
(or pre-emptively while their revisions are being finalized). They will have
between a few weeks to a few days to prepare their artifact and submit it. After
submission, reviewers are expected to interact with authors to improve the
artifact and resolve potential issues, they post comments and a preliminary
review that is continuously updated. Authors are expected to be responsive and
to fix things as they come (not leave everything to the last minute). When
comments or a review is posted, authors get an email notification immediately
(make sure to configure HotCRP correctly for that), they can begin responding to
the reviews to improve their artifact and move it towards submission. This
iterative process will continue for the specified time duration and then a
decision will be reached. After a decision has been reached there is no further
action required on the part of the authors (except checking that permanent and
stable link that is picked for the badge on the website is the correct one).

## Sending out Mail via HotCRP

HotCRP has some filtering features to select different recipients, see
[communication templates](PETS2026/communication-templates/) for email examples.

For example: sent to all authors without decision versus send to all authors.
It's sometimes difficult to filter authors so either do it by hand or you can
also select for authors with unresolved submissions or something like that.

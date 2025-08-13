# Process Description for (new) Artifact Evaluation Co-Chairs

On this page, we introduce some of the processes we have in place for the
Artifact Evaluation of PETS

## New artifact chair

- Send invite email to candidate that was picked
- Video call for onboarding
- Give access to GitHub organization, Slack with other Artifact chairs from
  other conferences, create artifactYY@email alias
- Make admin on past year’s instances to navigate and poke around (familiarize with things)
- Attend current PETS if possible, collect suggestions from authors
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

- Artifact Infrastructure Chair for the VMs (Tobias Fiebig through the service
  https://measurement.network that he created).

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

### VM instances

We offer VMs to reviewers for artifact evaluation if necessary. These VMs can be
directly spawn from the HotCRP interface. This is a service provided by
https://measurement.network currently ran by Tobias Fiebig.

We need to contact the infrastructure chair in charge of the VMs for integration
with the HotCRP instance. Essentially, they apply patches to the HotCRP source
code to add an integration with a hypervisor that allows for the creation and
management of VMs from the submission website. Thanks to these patches, we also
support markdown for reviews and comments (which is very useful for artifact
evaluation).

As of 2026, the VM types (for 22.04 and 24.04) available are:

- Standard (16gb memory, 4 cores, 40GB Disk)
- Docker pre-installed (16gb memory, 4 cores, 40GB Disk)
- Compute (64gb memory, 16 cores, 100GB Disk)
- scan (16gb memory, 4 cores, 40GB Disk; Like base, but on a dedicated network
  and auto-configuring a webserver with information on these systems being used
  for artifact evaluation for active measurements; This has blanket-coverage
  from our IRB for artifact evaluation, as long as the original paper got IRB
  clearance from their own org.)

Additionally, there are gpu-0x01 and gpu-0x02. These are VMs with 64gb memory
and 16 cores, and each with a dedicated NVIDIA A30.

In general, only _one_ instance of each (gpu-0x01 and gpu-0x02) can be running
at the same time. Multiple users can have shut-down VMs, though.

So, for example:

User A, User B and User C create a gpu-0x01 instance (no matter if ubuntu 22.04
or ubuntu 24.04). If User A is running the VM, and User B wants to use it, User
A must shut down the VM. However, when User B is done and shuts it down, User A
can boot their instance again, and all data will have been persistent.

The same for GPU-0x02; And, of course, _one_ instance of each can run in
parallel, but does _not_ share data.

So, in the example above, if User A runs GPU-0x01, and User C wants to also use
their GPU-0x01, but instead decides to boot up a new GPU-0x02 instance, they
will not have access to their data from their GPU-0x01 instance.


Users can (and should!) shutdown and delete their VMs as soon as they are done
with them. Of course, users usually forget, so you (as chair) should have an eye
on that.

The GPU VMs are somewhat special, and you should stay on top of their use, i.e.,
ensure that people check in with you when using them, and also turn them off
when they are no longer needed.


Once artifact evaluations are finalized for an issue, contact back the
infrastructure chair in charge of the VMs for them to remove the VMs and disable
the VM integration with the HotCRP instance.


Related archive file: [PETS2024/terms-of-use-vm.md](PETS2024/terms-of-use-vm.md)

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

## Notes
#### Document what is logged:
- Who started/deleted what type of machine when
- Which mac/ipv4/ipv6 address a users' VM had
- Standard weblogs for hotcrp+what hotcrp logs

#### Acceptable use/abuse policy:
- Only use infrastructure for artifact evaluation
- No private use (entailed by the former, but good to make explicit as well)
- Do not try to break/exploit the infrastructure; If you manage to find a
  vulnerability, report and do not snoop in other people's data; Ideally send
  patches.
- Do not engage in abuse against the Internet apart from active measurements
  that are being reproduced
- Do not do measurements from non-scan VMs
- Turn of and delete VMs you no longer need
- All VMs are wiped 1 week after an artifact has been accepted/rejected.
- Perform basic hygiene for the machines you allocated, i.e., do not set weak
  passwords and ideally use SSH key authentication
- Abuse leads to a loss of the VM privilege.

## MOTD
This is a template for MOTDs for different VM types:

#### All VMs

```
###############################################################################
# Dear User,                                                                  #
# By using our artifact evaluation VMs, you agree to the following terms:     #
#                                                                             #
# Data Collection: The artifact evaluation system logs when you created a VM, #
#     which MAC/IPv4/IPv6 address it received, and when the VM is removed.    #
#     This data will be deleted two weeks after the artifact review process   #
#     has been concluded for this cycle.                                      #
# Acceptable Use: Only use the provided systems for artifact evaluation.      #
#     Private use and non artifact-related use are not permitted.             #
# Care for the Infrastructure: Infrastructure is a common good. Do not break  #
#     it, if you find a vulnerability, contact abuse@measurement.network and  #
#     do not snoop in other people's data. We have a zero tollerance policy   #
#     for abuse and will remove access upon the first observed malicious act. #
#     Use only what you need, and delete VMs when you no longer need them.    #
# Only scan from scan VMs: Only perform active measurements from VMs that     #
#     have been setup for scanning (scan VM type).                            #
#                                                                             #
# For more information, see:                                                  #
#     https://measurement.network/policies/privacy-policy/                    #
# https://measurement.network/policies/abuse/                                 #
#                                                                             #
...
###############################################################################

```

#### GPU VMs

```
# This VM has a share of 1GB from an NVIDIA M40. CUDA12.2.0 is installed.     #
# To test that CUDA is available, you can run the following commands:         #
#                                                                             #
#             cuda-bandwidthTest                                              #
#             cuda-deviceQuery                                                #
#             cuda-deviceQueryDrv                                             #
#             cuda-topologyQuery                                              #
#                                                                             #
```

#### SCAN VMs

```
# This VM is configured for evaluating artifacts that contain active          #
# network measurements. For this purpose, a webserver runs on port 80,        #
# redirecting access to:                                                      #
#     https://measurement.network/about/current-artifact-evaluations          #
# Do not interfere with this webserver or change its configuration. If you    #
# need the ability to run your own webserver on tcp/80, please write an email #
# to: contact@measurement.network                                             #
#                                                                             #
```

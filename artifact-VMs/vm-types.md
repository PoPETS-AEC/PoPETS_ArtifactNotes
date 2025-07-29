# VM Types
This page lists the types of VMs which we want to use.

## Linux

#### Distributions

Please tick the distributions you think we need.

- [ ] Debian 11
- [ ] Debian 12
- [ ] Ubuntu 20.04
- [ ] Ubuntu 22.04
- [ ] Ubuntu 20.04 - Desktop
- [ ] Ubuntu 22.04 - Desktop
- [ ] Alpine Linux 3.14
- [ ] Alpine Linux 3.15
- [ ] Alpine Linux 3.16
- [ ] Alpine Linux 3.17

#### Base Images

Please tick the image types we should have available:

- [ ] Base (clean system, 8GB of memory, 4 cores, 50gb disk)
- [ ] Large Compute (clean system, 64GB of memory, 16 cores, 50GB Disk)
- [ ] Large Storage (clean System, 8GB of memory, 4 cores, 500GB Disk)


#### Flavors
Select which flavors should be available for each of the dist/base combinations above:

- [ ] Docker (Docker preinstalled)
- [ ] GPU (Cuda 12.2.0, Nvidia M40 or K80 1GB)
- [ ] Scanning (Setup with probe attribution in a dedicated scanning network)
- [ ] Email (Configured for sending and receiving emails on a unique domain, with webif)



## Windows

#### Notes
This is difficult licensing wise. Does somebody know someone over at MS who
might be able to help with that?

## Other
Are there any other OSes that are needed?

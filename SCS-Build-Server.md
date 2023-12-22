# Setting up build environment

## Prerequisites

- linux server (ubuntu/debian or other)
- at least 300 GB disk space
- GIT, python3
- Docker (version >= 24)
- KVM virtualization support
- good hardware

## Setup

```shell
# clone GIT repository
git clone git@github.com:SovereignCloudStack/sonic-buildimage.git

# add python libraries
cd sonic-buildimage
python3 -m venv .venv
source .venv/bin/activate
pip3 install --user j2cli

# initialize submodule
make init

# create subdirectories (otherwise build fails)
sudo mkdir -p /vcache/sonic-slave-bullseye/web
sudo chmod -R 777 /vcache

# adjust configuration in `rules/config`
# edit file ...

# prepare build
make configure PLATFORM=broadcom # PLATFORM=vs for GNS3

# build step
time make INSTALL_DEBUG_TOOLS=y SONIC_BUILD_JOBS=8 target/sonic-broadcom.bin
```

The build process may take several hours, at the end if no errors occur the final image will be located under `target/sonic-broadcom.bin`. The image version is written in `target/sonic-broadcom.bin.log`.


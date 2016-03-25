FROM quay.io/stackstorm/rpmbuildpack-deps:fedora23-curl

# procps is very common in build systems, and is a reasonably small package
RUN yum makecache && yum -y \
    bzr \
    git \
    mercurial \
    openssh \
    subversion \
    \
    procps-ng

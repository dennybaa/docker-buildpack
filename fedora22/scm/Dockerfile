FROM quay.io/dennybaa/rpmbuildpack-deps:fedora22-curl

# procps is very common in build systems, and is a reasonably small package
RUN yum makecache && yum -y install \
    bzr \
    git \
    mercurial \
    openssh \
    subversion \
    \
    procps-ng

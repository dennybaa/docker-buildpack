FROM quay.io/stackstorm/rpmbuildpack-deps:centos7-curl

# procps is very common in build systems, and is a reasonably small package
RUN yum makecache && yum -y \
    bzr \
    git \
    mercurial \
    openssh \
    subversion \
    \
    procps-ng

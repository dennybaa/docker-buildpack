# rpmbuildpack-deps

This is a templated clone of https://github.com/docker-library/buildpack-deps. It uses absolutely the same tools and libraries as its counterpart, with the only difference that it is intended to build images for centos and fedora.

# Automated containers build (quay.io)

## Update Dockerfiles

First please install [docker-citools](https://github.com/dennybaa/docker-citools), which has `docker-template.py` update tool. As the repository cloned and installed, say it, to your home directory, we can use `docker-template.py` which will update **Dockerfiles**.

The order is significant during later sequential build of containers, so we will write and preserve updated **Dockerfiles** list into `updated-dockerfiles` file. As soon commit happens, CirclCi will read this file and invoke build for the updated containers in the given order.

Run, the following command:

```
# depends on where your docker-citools is cloned
# Mind that curl scm _default is the order required on build.
~/docker-citools/docker-template.py -q -- curl scm _default | tee updated-dockerfiles
```

## Commit and push changes

Just commit and push changes, the rest CircleCi will do, namely it will invoke build of the updated containers in [quay.io](https://quay.io).

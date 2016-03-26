[![Docker Repository on Quay](https://quay.io/repository/stackstorm/rpmbuildpack-deps/status "Docker Repository on Quay")](https://quay.io/repository/stackstorm/rpmbuildpack-deps)
[![Circle CI](https://circleci.com/gh/dennybaa/docker-rpmbuildpack-deps.svg?style=shield)](https://circleci.com/gh/dennybaa/docker-rpmbuildpack-deps)

# rpmbuildpack-deps

This is a templated clone of https://github.com/docker-library/buildpack-deps. It uses absolutely the same tools and libraries as its counterpart, with the only difference that it is intended to build images for centos and fedora.

# Automated containers build (quay.io)

Build of docker images happens in two phases:

 - First circle ci build happens, it actually doesn't perform any tests or builds itself, but rather just figures out which dockerfiles have been updated and handles build operation to Quay.io.
 - Quay.io executes container builds. These builds happen in order (by variants) which is curl -> scm -> _default.

## Update Dockerfiles

First please install [docker-citools](https://github.com/dennybaa/docker-citools), which has `docker-template.py` update tool. As the repository cloned and installed, say it, to your home directory, we can use `docker-template.py` which will update **Dockerfiles**.

Run, the following command:

```
# Depends on where your docker-citools is cloned
~/docker-citools/docker-template.py
```

## Commit and push changes

Just commit and push changes, the rest CircleCi will do, namely it will invoke build of the updated containers in [quay.io](https://quay.io).

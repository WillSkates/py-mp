#!/bin/bash

if [ "$(podman images | grep "py-mp")" == "" ]; then
    ./build
fi

podman run --rm -ti -w "/work" -v "${PWD}:/work" py-mp $@

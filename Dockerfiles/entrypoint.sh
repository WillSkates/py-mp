#!/bin/bash

if [ "${PWD}" == "/work" ]; then
    INSTALL_REQS="False"

    if [ ! -d ".venv" ]; then
        python3 -m venv .venv
        INSTALL_REQS="True"
    fi

    source .venv/bin/activate

    if [ "${INSTALL_REQS}" == "True" ]; then
        pip install -r requirements.txt
    fi
fi

$@

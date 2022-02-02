#!/usr/bin/env bash

cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")" || exit 1

PYTHONPATH="$(pwd)"
export PYTHONPATH

#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="$(realpath "${HERE}/..")"

pushd "${ILLUD}" > /dev/null
trap "popd > /dev/null" EXIT

source "${ILLUD}/scripts/library/venv.sh"
use_venv "developer" frozen_developer_requirements.txt

python3 -m yapf -i -r .
python3 -m isort .

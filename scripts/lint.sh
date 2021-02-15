#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="$(realpath "${HERE}/..")"

pushd "${ILLUD}" > /dev/null
trap "popd > /dev/null" EXIT

source "${ILLUD}/scripts/library/venv.sh"
use_venv "test" frozen_test_requirements.txt

python3 -m pylint illud tests

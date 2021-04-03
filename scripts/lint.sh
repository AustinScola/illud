#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="$(realpath "${HERE}/..")"

cd "${ILLUD}"

source "${ILLUD}/scripts/library/venv.sh"
use_venv "test" frozen_test_requirements.txt

find . -path ./venvs -prune -false -o -name "*.py" | xargs python3 -m pylint -j 0

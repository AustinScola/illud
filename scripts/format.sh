#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="$(realpath "${HERE}/..")"

cd "${ILLUD}"

source "${ILLUD}/scripts/library/venv.sh"
use_venv "developer" frozen_developer_requirements.txt

source "${ILLUD}/scripts/library/cpus.sh"
NUMBER_OF_CPUS="$(get_number_of_cpus)"

python3 -m yapf --parallel -i -r .
python3 -m isort --jobs "${NUMBER_OF_CPUS}" .

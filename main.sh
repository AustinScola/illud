#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="${HERE}"

cd "${ILLUD}"

source "${ILLUD}/scripts/library/venv.sh"
use_venv main frozen_requirements.txt


python3 -m illud "$@"

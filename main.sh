#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="${HERE}"

source "${ILLUD}/scripts/library/venv.sh"
use_venv main frozen_requirements.txt

PYTHONPATH="${ILLUD}" python3 -m illud "$@"

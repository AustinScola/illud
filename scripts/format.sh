#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="$(realpath "${HERE}/..")"

pushd "${ILLUD}" > /dev/null
trap "popd > /dev/null" EXIT

find . -name "*.py" | xargs python3 -m yapf -i

find . -name "*.py" | xargs python3 -m isort -i

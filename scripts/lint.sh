#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ILLUD="$(realpath "${HERE}/..")"

pushd "${ILLUD}" > /dev/null
trap "popd > /dev/null" EXIT

python3 -m pylint illud tests

#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"

pushd "${HERE}" > /dev/null
trap "popd > /dev/null" EXIT

./format.sh

./lint.sh

./test.sh

./type_check.sh

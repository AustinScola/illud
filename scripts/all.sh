#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"

cd "${HERE}"

./format.sh

./lint.sh

./test.sh

./type_check.sh

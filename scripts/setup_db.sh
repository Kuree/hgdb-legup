#!/usr/bin/bash

set -xe

# detect the root dir
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT="$(dirname "${ROOT}")"

# use mysql docker
# use the same default password as legup mysql
docker run --name legup -e MYSQL_ROOT_PASSWORD=letmein -v "${ROOT}":/hgdb-legup -p 3306:3306 -d mysql

# untar the data file and then import it to mysql
tar xzf ${ROOT}/tests/vectors/data.tar.gz -C "${ROOT}"

#!/bin/sh

# The shell will terminate the script's execution when a command fails.
set -e

# check my POSTGRES DB
wait_plsql.sh

collectstatic.sh
migrate.sh
runserver.sh
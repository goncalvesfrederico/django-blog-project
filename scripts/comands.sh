#!/bin/sh

# The shell will terminate the script's execution when a command fails.
set -e

# check my POSTGRES DB
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSGRES_PORT) ..." &
    sleep 0.1
done

echo "🟢 Postgres Database Started Successfully ($POSTGRES_HOST $POSTGRES_PORT)"

python manage.py collectstatic
python manage.py migrate
python manage.py runserver
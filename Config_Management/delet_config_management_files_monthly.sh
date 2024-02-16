#!/bin/bash

PATH_DIR="/home/users/configfiles/routers

# This delets all the files in that directory whose last modification date is more than 30 days.
find "${PATH_DIR}" -f -mtime +30 -delete

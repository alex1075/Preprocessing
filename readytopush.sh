#! /bin/sh

echo '[INFO] Cleaning up temp files...'
find . -name "*.pyc" -exec git rm -f "{}" \;


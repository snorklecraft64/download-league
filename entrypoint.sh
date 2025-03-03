#!/bin/bash

echo "=========="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace

python3 /usr/bin/download_league.py

git add -A
git commit -m "Download Excel Sheets"
git push --set-upstream origin main

echo "=========="
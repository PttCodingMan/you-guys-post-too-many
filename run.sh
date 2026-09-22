#!/bin/bash
cd "$(dirname "$0")"

. ptt.sh

git pull

uv pip install -U -r requirements.txt --python .venv/bin/python

if .venv/bin/python .src/main.py;
then
	git add -A

	timestamp=$( date +"%Y-%m-%d %T" )
	git commit -m "Auto update at $timestamp"
	git push
fi

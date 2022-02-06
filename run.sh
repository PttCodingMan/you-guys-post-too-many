
sh ptt.sh

git pull

python3 .src/main.py

git add -A

timestamp=$( date +"%Y-%m-%d %T" )
git commit -m "Auto update at $timestamp"
git push

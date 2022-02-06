
. ptt.sh

git pull

if python3 .src/main.py;
then
	git add -A

	timestamp=$( date +"%Y-%m-%d %T" )
	git commit -m "Auto update at $timestamp"
	git push
fi

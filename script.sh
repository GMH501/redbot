set -exu
# -e : Exit immediately if a command exits with a non-zero status
# -x : Print commands and their arguments as they are executed
# -u : Treat unset variables as an error when substituting
python3 redbot.py
exit ${PIPESTATUS[0]}
#!bin/sh
# UPATH=/usr/local/bin
UPATH=/opt/dev/shunia/flask-apps/writtings/venv/bin
UWSGI=$UPATH/uwsgi
LOGTO=/var/log/uwsgi/emperor.log

$UWSGI --master --emperor /etc/uwsgi/vassals --die-on-term --logto $LOGTO

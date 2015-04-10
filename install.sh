#!/bin/bash
# python
if [ ! hash python 2>/dev/null ]; then
	exit
fi

# pip
if [ ! hash pip 2>/dev/null ]; then
	wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
	python /tmp/get-pip.py
fi

#   pip install
pip install -r requirements.txt

# virtual env
if [ ! -d "venv" ]; then
	virtualenv venv
fi
. venv/bin/activate

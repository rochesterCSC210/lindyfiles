#!/usr/bin/python

import cgi
import cgitb
import os
import sqlite3
import Cookie
from datetime import datetime


def do_err():
	print "Content-type: text/html"
	print
	print "User not recognized."
	print "Only logged-in users can view the message board."
	exit(1)

def clear():
	with open("message_board.txt", "w") as f:
		f.write("")

def add_msg(new_message, email):
	with open("message_board.txt", "a") as f:
		msg = str( (new_message, email, str(datetime.now())) )
		f.write(msg)
		f.write("\n")
		f.close()

cgitb.enable()
form = cgi.FieldStorage()
new_message = form['stuff'].value
clear = form['clear'].value
conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
cur = conn.cursor()

cookie_string = os.environ.get('HTTP_COOKIE')
if not cookie_string:
	do_err()

try:
	ck = Cookie.SimpleCookie(cookie_string)
	sessid = ck['sessid'].value
	cur.execute("SELECT email FROM users WHERE sessid = ?", (sessid,))
	results = cur.fetchone()
	email = results[0]
except:
	do_err()

if clear:
	clear()
else:
	add_msg(new_message, email)

s = ''
with open("message_board.txt", "r+") as f:
	for line in f:
		s += line + '\n'

print "Content-type: text/html"
print
print s

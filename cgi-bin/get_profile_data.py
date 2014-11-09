#!/usr/bin/python

import cgi
import cgitb
import os
import sqlite3
import Cookie

def do_err(s):
	print "Content-type: text/html"
	print
	print s
	exit(1)

def main():

	cgitb.enable()
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	c = conn.cursor()
	ck_string = os.environ.get('HTTP_COOKIE')
	if not ck_string:
		do_err("User not logged in.")

	try:
		ck = Cookie.SimpleCookie(cookie_string)
		sessid = ck['sessid'].value
		c.execute("SELECT (username, password, fname, email, picture, leader, follower) FROM users WHERE sessid = ?", (sessid,))
		result = c.fetchone()[0]
	except:
		do_err("User not recognized.")

	print "Content-type: text/html"
	print
	for field in result:
		print field + '\t'

if __name__ == "__main__":
	main()
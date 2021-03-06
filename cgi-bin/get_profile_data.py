#!/usr/bin/python

import cgi
import cgitb
import os
import sqlite3
import Cookie

def do_err(s):
	print "Content-type: text/html"
	print
	print "ERROR:",
	print s
	exit(1)

def main():

	cgitb.enable()
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	cur = conn.cursor()
	ck_string = os.environ.get('HTTP_COOKIE')
	if not ck_string:
		do_err("User not logged in.")
		
	try:
		form = cgi.FieldStorage()
		email = form['email'].value
		cur.execute("SELECT username, fname, email, picture, leader, follower FROM users WHERE email = ?", (email,))
		result = cur.fetchone()
		if result is None:
			do_err("Email does not belong to any user.")
		print "Content-type: text/html"
		print
		for field in result:
			print str(field) + '\t'
		exit(0)
	except KeyError:
		pass

	try:
		ck = Cookie.SimpleCookie(ck_string)
		sessid = ck['sessid'].value
		cur.execute("SELECT username, fname, email, password, picture, leader, follower FROM users WHERE sessid = ?", (sessid,))
		result = cur.fetchone()
		print "Content-type: text/html"
		print
		for field in result:
			print str(field) + '\t'
	except:
		do_err("User not recognized.")


if __name__ == "__main__":
	main()

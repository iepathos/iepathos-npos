#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Written by Glen Baker - iepathos@gmail.com
#
#
# I am a coder, writer, musician and lover follow me @iepathos
#

import MySQLdb as mdb
import sys
import os


def main():
	# connect to mysql db - ( host, user, pass, db )
	con = mdb.connect('localhost', 'iepathos', 'pathospass', 'iepathos');
	
	# Download IRS Tax-Exempt NPO's list
	# irsnpos = os.system('wget http://apps.irs.gov/app/eos/forwardToPub78Download.do')
	# skip first 2 blank lines ( i just deleted them )
	# open npo txt IRS http://apps.irs.gov/app/eos/forwardToPub78Download.do
	lines = open('data-download-pub78.txt', 'r').readlines()
	
	# Information in format: ein | name | city | state | - | United States |
	for line in lines:
		npodata = line.split('|') # split each line along the '|'
		#ein = npodata[0] # Electronic Identification Number - IRS assigned id number	
		#name = npodata[1] # Name of Non-Profit Organization
		#city = npodata[2]
		#state = npodata[3]
		# npodata[4] is just '-'
		country = npodata[5] 
		d = dict(ein = npodata[0], name = npodata[1], city = npodata[2], state = npodata[3], country = npodata[5], is_active = '1')
		print('Inserting ' + npodata[1] + ' into the database')
		with con:
			cur = con.cursor()
			# Insert data into table
			
			cur.execute("""
				REPLACE INTO npos_npo(ein, name, city, state, country) 
				VALUES(%(ein)s, %(name)s, %(city)s, %(state)s, %(country)s)					
				""", d)
			cur.execute("REPLACE INTO npos_npo(is_active) VALUES('1')")
				
	con.close()

if __name__ == '__main__':
	main()

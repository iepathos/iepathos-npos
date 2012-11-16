# iepathos-npos uses: Django 1.4.2, South, MySQL and Python scripting.
### Written by Glen Baker - iepathos@gmail.com <a href="http://coderwall.com/iepathos"><img src="http://api.coderwall.com/iepathos/endorsecount.png" /></a>

#### Django app 'npos' creates a basic models for non-profit organizations based on the information given by the irs.  Includes: electronic identification number, name, city, state and country.

models.py holds all the information
admin.py allows for checking and editing npos

#### nposiepathos.py parses the list of tax exempt non-profit organizations, data-download-pub78.txt and write them into the MySQL database iepathos.

todo: Use threading to speed up MySQL writing.

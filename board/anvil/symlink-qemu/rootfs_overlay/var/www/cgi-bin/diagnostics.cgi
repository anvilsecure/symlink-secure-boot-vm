#!/usr/bin/env python3

import cgi
import cgitb
import subprocess
import requests

cgitb.enable()

print("Content-Type: text/html")
print()

print("<html>")
print("<head>")
print("<title>Diagnostics</title>")
print("</head>")

print("<body>")

form = cgi.FieldStorage()

url = ""
if "url" in form:
	url = form["url"].value


print('<h2>Diagnostics Upload</h2>')
print('<form method="post" enctype="multipart/form-data">')
print('<label>Upload URL:</label>')
print('<input name="url" value="{}" size="75"/>'.format(url))
print('<input type="submit" name="action" value="Submit"/>')
print('</form>')

if "action" in form and url != "":
	# build the diagnostic tar file by taring up the log folder
	result = subprocess.run(["tar", "-c", "/var/log/."], stdout=subprocess.PIPE)
	requests.post(url, data=result.stdout)

print("</body>")
print("</html>")

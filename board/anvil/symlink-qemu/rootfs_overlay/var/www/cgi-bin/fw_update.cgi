#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html")
print()

print("<html>")
print("<head>")
print("<title>Firmware update</title>")
print("</head>")

print("<body>")

form = cgi.FieldStorage()
if "file" not in form:
	print('<h2>Firmware Upload</h2>')
	print('<form method="post" enctype="multipart/form-data">')
	print('<label>Select firmware file:</label>')
	print('<input type="file" name="file"/>')
	print('<input type="submit" value="Submit"/>')
	print('</form>')
else:
	f = form["file"]
	o = open("/storage/fw_update/incoming.tgz", "wb")
	o.write(f.value)
	print("<h2>Firmware uploaded!</h2>")

print("</body>")
print("</html>")

#!/usr/bin/env python3

import cgi
import os
import urllib

cgi.logfile = "/var/log/cgi_logger"


qs = urllib.parse.unquote_plus(os.environ["QUERY_STRING"])
remote_addr = os.environ["REMOTE_ADDR"]


cgi.log("Received query %s from %s", qs, remote_addr)

print("Content-Type: text/html")
print()

print("""<html>
<head>
<title>Logger!</title>
</head>
<body>
Your query %s has been logged (source IP=%s)!
</body>
</html>
""" % (qs, remote_addr))


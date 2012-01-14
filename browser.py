#!/usr/bin/env python

#early beta
import os,glob
import cherrypy
from cherrypy.lib.static import serve_file

from jinja2 import Template

tmpl = (u'''\
<html>
<head><title>{{ variable|escape }}</title></head>
<body>

<a href="{{ previous_path }}">{{ previous_path }} </a>

<ul id="items">
</ul>
{% for value  in itemlist|sort %}
    <li><a href="{{ value }}">{{ value }} </a>  </li>
{% endfor %}
</body>
</html>''')
path = "/Users/fyelles"


def folderlist(path):
    return [current for current in glob.glob(os.path.join(path,'*'))]


class Main(object):
    def default(self,*args,**kwargs):
		mypath = False
		if args:
			mypath = "/"+"/".join(args)
			previous_path = "/"+"/".join(args[:-1])
		else:
			mypath = path
			previous_path = path
		#TODO: Verify path, can cause problem if user override the path ie: /etc/shadow
		if os.path.isdir(path):
			return Template(tmpl).render(variable=mypath,previous_path=previous_path,itemlist=folderlist(mypath))
		elif os.path.isfile(mypath):    
			return serve_file(mypath,"application/x-download")
		else:
			return "WTF",mypath

    default.exposed = True

cherrypy.quickstart(Main())
 

         
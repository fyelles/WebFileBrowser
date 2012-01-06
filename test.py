#!/usr/bin/env python

#early beta
import os,glob
import cherrypy
from jinja2 import Template

tmpl = (u'''\
<html>
<head><title>{{ variable|escape }}</title></head>
<body>
{% for value, key  in item_dict.iteritems()|sort %}
    {% if key == "folder" %}
       Folder {{ value }}  - {{ key }}<br>
    {% else %}
        {{ value }} -- {{ key }} <br>
        {% endif %}
{% endfor %}
</body>
</html>''')
path = "/Users/fyelles"


def folderlist(path):
    Mydict=dict()
    for current in glob.glob(os.path.join(path,'*')):
        if os.path.isdir(current):
            Mydict[current]='folder'
        if os.path.isfile(current):    
            Mydict[current]='file'
    return Mydict

class HelloWorld(object):
    def index(self):
        # return tmpl.render(variable='Value with <unsafe> data',item_list=[1, 2, 3, 4, 5, 6])
        return Template(tmpl).render(variable=path,item_dict=folderlist(path))

    index.exposed = True

cherrypy.quickstart(HelloWorld())
 
# path = "/Users/fyelles"
# for current in glob.glob(os.path.join(path,'*')):
#     if os.path.isdir(current):
#         print "\t %s" % (current)
#     if os.path.isfile(current):    
#     print "%s" % (current)
         
import subprocess
import json
import os
from string import Template  

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 

def get_file_content(filename):
    f = open(filename)
    data = f.read()
    f.close()
    return data

meta = json.loads(get_file_content("meta.json"))

content = ""

for part in meta:
    content += "\part{%s}" % part['name']
    for chapter in part["chapters"]:
        content += "\chapter{%s}" % chapter["name"]
        content += subprocess.check_output(["pandoc"] + [chapter["file"]] + ["-t", "latex"])

t = Template(get_file_content("template.tex"))

f = open('output.tex', 'w')
f.write(t.substitute({'body' : content}))
f.close()

os.system("xelatex output.tex")
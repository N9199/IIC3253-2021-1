#!/usr/bin/python3
import json
import os

from datetime import datetime
os.chdir(os.path.dirname(__file__))
with open("variables.json") as f:
    variables = json.load(f)
print(variables)
ls = list(map(lambda x: int(
    x[:-4]), filter(lambda x: x[-4:] == ".tex", os.listdir('../pdfs/Ayudantias'))))

variables['number'] = f"{max(ls, default=0)+1:02d}"
variables['curr_date'] = datetime.today().strftime('%Y-%m-%d')

with open("template") as template:
    out = template.read()
    for k, v in variables.items():
        if v == "":
            v = "\phantom{}"
        out = out.replace(f"${k}$", str(v))
    with open(f"../pdfs/Ayudantias/{variables['number']}.tex", 'w') as output:
        output.write(out)

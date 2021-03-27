import os
import re
from datetime import datetime

enunciados = list(map(lambda x: int(
    x[9:-4]), filter(lambda x: x[-4:] == ".pdf", os.listdir("../pdfs/Enunciados"))))
soluciones = list(map(lambda x: int(
    x[8:-4]), filter(lambda x: x[-4:] == ".pdf", os.listdir("../pdfs/Soluciones"))))

enunciados.sort()
soluciones.sort()
assert(len(enunciados) >= len(soluciones))
with open("../index.md") as f:
    curr = f.read()

re1 = re.compile("Enunciado\d\d\.pdf")
re2 = re.compile("Solucion\d\d\.pdf")
re3 = re.compile("\\\\subtitle\{.*\}")

curr_enunciados = set(map(lambda x: int(x[9:-4]), re1.findall(curr)))
curr_soluciones = set(map(lambda x: int(x[8:-4]), re2.findall(curr)))

# Note: index 6 for update date, indices in [9,len(curr)-3] are for display list
curr = curr.split('\n')
delta = []
out = []


j = 0
for i in range(len(enunciados)):
    while int(enunciados[i]) > int(soluciones[j]) and j+1 < len(soluciones):
        j += 1
    if int(enunciados[i]) not in curr_enunciados:
        delta.append(f"Enunciado {enunciados[i]:02d}")
    if int(soluciones[i]) not in curr_soluciones:
        delta.append(f"Solución {soluciones[i]:02d}")
    with open(f"../pdfs/Ayudantias/{enunciados[i]:02d}.tex") as f:
        temp1 = list(
            map(lambda x: x[10:-1], re3.findall(f.read())))[0]
    if enunciados[i] == soluciones[j]:
        temp = f"- Ayudantia {enunciados[i]:02d} ({temp1}) - [Enunciado](pdfs/Enunciados/Enunciado{enunciados[i]:02d}.pdf) - [Solución](pdfs/Soluciones/Solucion{soluciones[j]:02d}.pdf)"
    else:
        temp = f"- Ayudantia {enunciados[i]:02d} ({temp1}) - [Enunciado](pdfs/Enunciados/Enunciado{enunciados[i]:02d}.pdf)"
    out.append(temp)

curr[6] = f"Última actualización: {datetime.today().strftime('%m/%d')} ({', '.join(delta)})"
curr = curr[:10]+out+curr[-3:]

with open("../index.md", 'w') as f:
    f.write('\n'.join(curr))
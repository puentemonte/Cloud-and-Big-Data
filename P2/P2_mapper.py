import sys
import re

# por cada linea, nos quedamos con el link
# el formato de los logs es el siguiente:
# 64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846v
# ip idClient usernameClient time request status size
# si los separamos por espacios, conseguimos 10 items y necesitamos la que está en la posición 6 (que es la url)

for line in sys.stdin:
    data = line.strip().split(" ")

    if len(data) == 10:
        page = data[6]
        print(page + '\t' + '1')

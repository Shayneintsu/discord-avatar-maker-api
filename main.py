from avatar import Avatar
import json
from time import sleep
from cairosvg import svg2png
from constants import PATH_DAMA

path = PATH_DAMA

def writeHTML(a:Avatar=Avatar()):
    f = open("./tmp.html","w")
    html = a.generateHTML()
    f.write(html)
    f.close()

def writeSVG(a:Avatar=Avatar()):
    f = open("./tmp.svg","w")
    html = a.generateSVG()
    f.write(html)
    f.close()

with open('./data.json') as json_file:
    data = json.load(json_file)
""" for shape in data["shape"]:
    for eye in data["eye"]:
        t = Avatar(color="magenta",shape=shape,eyes=eye)
        write(t)
        sleep(0.5) """

a = Avatar()
a.generateRandom()
writeSVG(a)
writeHTML(a)

svg2png(open("./tmp.svg", 'rb').read(), write_to=open("./out.png", 'wb'),output_height=128,output_width=128,parent_height=128,parent_width=128)
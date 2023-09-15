import json
from htmlScoob import HTML
from svgScoob import SVG
import random
from rgbprint import Color

def to_rgb(clr:Color):
    return "rgb("+str(clr.r)+","+str(clr.g)+","+str(clr.b)+")"

class Avatar:

    def __init__(self,color:str="black",shape:str="base-shape",background:str="white",eyes:str="base-eyes"):
        self.shape = shape
        self.color = Color(color)
        self.background = background
        self.shape_eyes = eyes

    def generateRandom(self):
        with open('./data.json') as json_file:
            data = json.load(json_file)
        self.shape = random.choice(list(data["shape"].keys()))
        self.color = Color(r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))
        self.shape_eyes = random.choice(list(data["eye"].keys()))
        self.background = Color(r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))

    def generateHTML(self):
        with open('./data.json') as json_file:
            data = json.load(json_file)
        html = HTML()
        html.set_color(to_rgb(self.color))
        html.set_color_background(to_rgb(self.background))
        html.add_svg(data["shape"][self.shape])
        html.add_svg(data["eye"][self.shape_eyes])
        return str(html)
    
    def generateSVG(self):
        with open('./data.json') as json_file:
            data = json.load(json_file)
        svg = SVG()
        svg.set_color(to_rgb(self.color))
        svg.add_svg(data["shape"][self.shape])
        svg.add_svg(data["eye"][self.shape_eyes])
        return str(svg)
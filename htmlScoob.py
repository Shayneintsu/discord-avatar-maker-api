

class HTML:

    def __init__(self):
        self.style1 = None
        self.style2 = None
        self.body1 = None
        self.body2 = None

    def __str__(self):
        r = "<html><head><meta charset=\"utf-8\"><style>"
        r += "svg{width:128;height:128;}"
        r += self.style1
        r += self.style2
        r += "</style></head><body>"
        r += self.body1
        r += self.body2
        r += "</body></html>"
        return r
    
    def set_color(self, color:str):
        self.style1 = ".shape{fill:"+color+";}"

    def set_color_background(self, color:str):
        self.style2 = "svg{background-color:"+color+";}"

    def add_svg(self, svg:str):
        if not self.body1:
            self.body1 = svg
        elif not self.body2:
            self.body2 = svg
        else:
            self.body1 = svg
            self.body2 = None


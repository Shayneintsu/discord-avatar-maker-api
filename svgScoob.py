

class SVG:

    def __init__(self):
        self.style1 = None
        self.body1 = None
        self.body2 = None

    def __str__(self):
        r = f"<g width=\"128px\" height=\"128px\" {self.style1} >"
        r += self.body1
        r += self.body2
        r += "</g>"
        return r
    
    def set_color(self, color:str):
        self.style1 = f"fill=\"{color}\""

    def add_svg(self, svg:str):
        if not self.body1:
            self.body1 = svg
        elif not self.body2:
            self.body2 = svg
        else:
            self.body1 = svg
            self.body2 = None


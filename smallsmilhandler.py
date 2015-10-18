"""
idea: crear una lista con etiquetas y diccionarios
"""

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.lista = []
        self.root = {}
        self.reg = {}
        self.img = {}
        self.aud = {}
        self.text = {}

    def startElement(self, etiqueta, attrs):

        if etiqueta == 'root-layout':
            self.lista.append("root-layout")
            self.root["width"] = attrs.get('width', "")
            self.root["height"] = attrs.get('height', "")
            self.root["background"] = attrs.get('background-color', "")
            self.lista.append(self.root)
        elif etiqueta == 'region':
            self.lista.append("region")
            self.reg["id"] = attrs.get('id', "")
            self.reg["top"] = attrs.get('top', "")
            self.reg["bottom"] = attrs.get('bottom', "")
            self.reg["left"] = attrs.get('left', "")
            self.reg["right"] = attrs.get('right', "")
            self.lista.append(self.reg)
        elif etiqueta == 'img':
            self.lista.append("img")
            self.img["src"] = attrs.get('src', "")
            self.img["region"] = attrs.get('region', "")
            self.img["begin"] = attrs.get('begin', "")
            self.img["dur"] = attrs.get('dur', "")
            self.lista.append(self.img)
        elif etiqueta == 'audio':
            self.lista.append("audio")
            self.aud["src"] = attrs.get('src', "")
            self.aud["begin"] = attrs.get('begin', "")
            self.aud["dur"] = attrs.get('dur', "")
            self.lista.append(self.aud)
        elif etiqueta == 'textstream':
            self.lista.append("textsream")
            self.text["src"] = attrs.get('src', "")
            self.text["region"] = attrs.get('region', "")
            self.lista.append(self.text)

    def get_tags(self):
        return self.lista
if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))

    listatotal = cHandler.get_tags()
    print(listatotal)

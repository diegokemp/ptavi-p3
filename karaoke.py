from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import json
import urllib.request


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.lista = []
        self.listaurl = []
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
            self.root["background-color"] = attrs.get('background-color', "")
            self.lista.append(self.root)
            self.root = {}
        elif etiqueta == 'region':
            self.lista.append("region")
            self.reg["id"] = attrs.get('id', "")
            self.reg["top"] = attrs.get('top', "")
            self.reg["bottom"] = attrs.get('bottom', "")
            self.reg["left"] = attrs.get('left', "")
            self.reg["right"] = attrs.get('right', "")
            self.lista.append(self.reg)
            self.reg = {}
        elif etiqueta == 'img':
            self.lista.append("img")
            self.img["src"] = attrs.get('src', "")
            self.listaurl.append(self.img["src"])
            self.img["region"] = attrs.get('region', "")
            self.img["begin"] = attrs.get('begin', "")
            self.img["dur"] = attrs.get('dur', "")
            self.lista.append(self.img)
            self.img = {}
        elif etiqueta == 'audio':
            self.lista.append("audio")
            self.aud["src"] = attrs.get('src', "")
            self.listaurl.append(self.aud["src"])
            self.aud["begin"] = attrs.get('begin', "")
            self.aud["dur"] = attrs.get('dur', "")
            self.lista.append(self.aud)
            self.aud = {}
        elif etiqueta == 'textstream':
            self.lista.append("textstream")
            self.text["src"] = attrs.get('src', "")
            self.listaurl.append(self.text["src"])
            self.text["region"] = attrs.get('region', "")
            self.lista.append(self.text)
            self.text = {}

    def get_tags(self):
        return self.lista

    def get_url(self):
        return self.listaurl
        
if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("Usage: python3 karaoke.py file.smil")
    etiquetas = ["root-layout","region","img","audio","textstream"]
    listatotal = cHandler.get_tags()
    listaurls = cHandler.get_url()
    for url in listaurls:
        print("---------")
        trueurl = url.split("//")
        print(trueurl)
        if trueurl == "http:":
            local_File = urllib.urlretrieve(url)
            print(local_file)
    archivo = open("karaoke.json","w")
    datjson = json.dump(listatotal, archivo)
    final = ""
    for elemento in listatotal:
        if elemento in etiquetas:
            if final == "":
                final = final + elemento + "\t"
            else:
                final = final + "\n"
                final = final + elemento + "\t"
        elif elemento != []:
            for key in elemento.keys():
                if elemento[key] != "":
                    final = final + key + '="' + elemento[key] + '"\t'
    print(final)

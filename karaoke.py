from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import json
import urllib.request
from smallsmilhandler import SmallSMILHandler #importa solo la clase


class KaraokeLocal():

    def __init__(self, fichero):

        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        try:
            parser.parse(open(fichero))
        except FileNotFoundError:
            sys.exit("Usage: python3 karaoke.py file.smil")

        self.listatotal = cHandler.get_tags()
        self.listaurls = cHandler.get_url()

    def __str__(self):
        etiquetas = ["root-layout","region","img","audio","textstream"]
        final = ""
        for elemento in self.listatotal:
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

    def to_json(self):
        archivo = open("karaoke.json","w")
        datjson = json.dump(self.listatotal, archivo)
        print("Elemento json creado")

    def do_local(self):
        for url in self.listaurls:
            trueurl = url.split("//")
            if trueurl[0] == "http:":
                localfinder = url.split("/")
                acortada = urllib.request.urlretrieve(url,"/tmp/" + localfinder[4])
                print("Descargando en /tmp/: " + localfinder[4])
        
        
if __name__ == "__main__":

    fichero = sys.argv[1]
    karaobj = KaraokeLocal(fichero)
    karaobj.do_local()
    karaobj.__str__()
    karaobj.to_json()

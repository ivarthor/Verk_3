from sys import argv
import bottle
from bottle import *

@route("/")
def index():
    return """
        <h2>Verkefni 3</h2
        <p><a href="/a">Liður A</a></p>
        <p><a href="/b">Liður B</a></p>
    """

###################
# VERKEFN 3 LIÐUR A
###################

@route("/a")
def index():
    return template("temp-a.tpl")

@route("/sida/<kt>")
def sida(kt):
    return template("temp-kt.tpl", kt = kt)

###################
# VERKEFN 3 LIÐUR B
###################

frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is"]]


@route("/b")
def index():
    return template("index.tpl", frett = frettir)


@route("/frett/<id:int>")
def index(id):
    return template("frett.tpl", frett = frettir[id], nr = id)

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root = "./static")

###############################################

@error(404)
def error404(error):
    return "ERROR"


bottle.run(host="0.0.0.0",port=argv[1])
#bottle.run(host="localhost", port=7000, debug=True)

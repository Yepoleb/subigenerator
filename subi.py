import random
import string
import flask

vowels = "aeiou"
consonants = list(set(string.ascii_lowercase) - set(vowels))

def subify(subi):
    base_subi = list(subi)
    r = random.random()
    if r <= 0.3:
        change = 1
    else:
        change = 2

    for _ in range(change):
        character_i = random.randrange(0, len(base_subi))
        if base_subi[character_i] in vowels:
            choose_set = vowels
        else:
            choose_set = consonants
        base_subi[character_i] = random.choice(choose_set)
        
    return "".join(base_subi)

if __name__ == "__main__":
    for _ in range(20):
        print(subify("subi"))

app = flask.Flask(__name__)
@app.route("/")
def index():
    subis = [subify("subi") for i in range(20)]
    return flask.render_template("subi.html", subis=subis)

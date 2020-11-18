import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route("/", methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route("/books", methods=['GET'])
def api_all():
    return jsonify({'books': books})

@app.route("/books/<int:id>", methods=['GET'])
def api_id(id):
    return jsonify({"Books" : books[id]})

@app.route("/books",methods=['post'])
def Create():
    json_data = request.get_json()
    #id = json_data['id']
    #title = json_data['title']
    #author = json_data['author']
    #first_sentence = json_data['first_sentence']
    #published = json_data['published']
    books.append(json_data)
    return jsonify(books)

@app.route("/books/<string:title>",methods=['PUT'])
def update(title):
    t = [book for book in books if book['title']==title]
    t[0]['title']=request.json['title']
    return jsonify({"books":books})


@app.route("/books/<string:title>",methods=['DELETE'])
def delete(title):
    t = [book for book in books if book['title']==title]
    books.remove(t[0])
    return jsonify({"books":books})


app.run()

# get - /books
# get - /
# get - /books/{id_number}
# post - /books
# put - /books/{title}
# delet - /books/{title} 
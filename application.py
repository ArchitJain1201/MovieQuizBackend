from flask import Flask, request
import json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    option1 = db.Column(db.String(120), primary_key=True)
    option2 = db.Column(db.String(120), primary_key=True)
    option3 = db.Column(db.String(120), primary_key=True)
    option4 = db.Column(db.String(120), primary_key=True)
    actor = db.Column(db.String(120), primary_key=True)
    img_url = db.Column(db.String(320), primary_key=True)
    movie_by = db.Column(db.String(120), primary_key=True)
    answer = db.Column(db.String(120), primary_key=True)

    def __repr__(self) -> str:
        return super().__repr__()

@app.route('/')
def index():
    return 'hello'

@app.route('/movie')
def get_movieInfo():
    movieInfos = Movie.query.all()
    output = []
    for movie in movieInfos:
        movie.name = movie.name.replace(u"\u00A0", " ")
        movie_data = {
            'name': movie.name,
            'option1': movie.option1,
            'option2': movie.option2,
            'option3': movie.option3,
            'option4': movie.option4,
            'actor': movie.actor,
            'img_url': movie.img_url,
            'movie_by': movie.movie_by,
        }
        output.append(movie_data)
    return {"movieInfo": output}

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

@app.route('/movie',methods=['POST'])
def checkAnswer():
    response = Movie(
        name=request.json['name'],
        answer=request.json['answer']
    )
    print(response.name)
    # movieInfos = Movie.query.all()
    # for movie in movieInfos:
    #         if response.name==movie.name:
    #             print('Movie name found')
    #             if response.answer==movie.answer:
    #                 return True
    #             else: 
    #                 return False
    # print("not Found")
    return False

# Fill the Sql database
# write Script to fill the database
# write funtion to randomly take 10 movies
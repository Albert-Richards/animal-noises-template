from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Animals(db.Model):
	entry_no = db.Column(db.Integer, primary_key=True)
	animal_entry = db.Column(db.String(50), nullable=False)

db.create_all()

@app.route('/')
def home():
    animal = requests.get('http://animal_api:5000/get_animal')
    noise = requests.post('http://animal_api:5000/get_noise', data=animal.text)
    response = f"The {animal.text} goes {noise.text}"
    db.session.add(Animals(animal_entry=response)) 
    db.session.commit()
    history = Animals.query.order_by(Animals.entry_no.desc()).limit(5).all()
    return render_template('index.html', history=history, animal=animal.text, noise=noise.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
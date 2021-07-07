from flask import Flask, render_template
import requests

app = Flask(__name__)

# home route here
@app.route('/')
def home():
    animal = requests.get('http://animal_api:5000/get_animal')
    noise = requests.post('http://animal_api:5000/get_noise', data=animal.text)
    #history = Animals.query.order_by(Animals.id.desc()).limit(5).all()
    return render_template('index.html', animal=animal.text, noise=noise.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
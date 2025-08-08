from flask import Flask
from flask_cors import CORS

from src.routes.animal_route import animal_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(animal_bp)



if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
from flask import Flask, request, jsonify, render_template
from src.utils.ask_question_to_pdf import ask_question_to_pdf
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dark_mode = db.Column(db.Boolean, default=False)


# Ensure tables are created
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")





@app.route("/prompt", methods=["POST"])
def prompt():
    # Call your function for processing the prompt
    response = jsonify({"answer": ask_question_to_pdf(request.form["prompt"])})
    return response


@app.route("/set-preference", methods=["POST"])
def set_preference():
    dark_mode = request.form.get('dark_mode') == 'true'
    # Upsert the dark mode preference (insert or update)
    user_preference = UserPreference.query.first()  
    if user_preference:
        user_preference.dark_mode = dark_mode
    else:
        user_preference = UserPreference(dark_mode=dark_mode)
        db.session.add(user_preference)
    db.session.commit()
    return jsonify({"message": "Preference saved"})


@app.route("/get-preference", methods=["GET"])
def get_preference():
    user_preference = UserPreference.query.first()  
    if user_preference:
        return jsonify({"dark_mode": user_preference.dark_mode})
    else:
        return jsonify({"dark_mode": False})

@app.route('question',methods=['POST'])
def generate_question():
    course_content=chunks[0]
    return {'answer':ask_question_to_pdf("Pose moi une question et dis moi si ma réponse est juste sur le cours suivant :" + course_content}

if __name__ == "__main__":
    app.run(debug=True)

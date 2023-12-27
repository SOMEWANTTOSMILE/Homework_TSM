from flask import Flask, render_template, request, jsonify
from app import Intake, engine
from sqlalchemy.orm import Session


app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def user_intake():
    if request.method == 'POST':
        user_name = request.form['user']
        food = request.form['food']
        weight = request.form['weight(grams)']
        proteins = request.form['proteins']
        fats = request.form['fats']
        carbohydrates = request.form['carbohydrates']
        intake = {
            "user_name": user_name,
            "food": food,
            "weight": weight,
            "proteins": proteins,
            "fats": fats,
            "carbohydrates": carbohydrates
        }
        print(intake)
        with Session(engine) as db:
            intake = Intake(user_name=user_name, food=food, weight=weight, proteins=proteins, fats=fats,
                            carbohydrates=carbohydrates)
            db.add(intake)
            db.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5400, debug=True)
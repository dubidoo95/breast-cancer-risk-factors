from flask import Flask, render_template, request
import joblib
import pandas as pd

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/input')
    def user_input():
        return render_template('input.html')

    @app.route('/output', methods=['POST'])
    def user_output():
        result = request.form
        df = pd.DataFrame(result, index=[0])
        df = df[['age_group_5_years', 'race_eth', 'first_degree_hx', 'age_menarche',
                'age_first_birth', 'BIRADS_breast_density', 'current_hrt', 'menopaus',
                'bmi_group', 'biophx', 'breast_cancer_history']]
        model = joblib.load('./flask_app/project3_model.pkl')
        y_pred = model.predict(df)
        return render_template("output.html", result=y_pred)
    return app
# if __name__ == "__main__":
#     app.run(debug=True)
    

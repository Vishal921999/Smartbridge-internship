import flask
import pandas as pd
from joblib import dump, load


with open(f'random.save', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        Cement = flask.request.form['Cement']
        BlastFurnaceSlag = flask.request.form['BlastFurnaceSlag']
        FlyAsh = flask.request.form['FlyAsh']
        Water =flask.request.form['Water']
        Superplasticizer = flask.request.form['Superplasticizer']
        CoarseAggregate = flask.request.form['CoarseAggregate']
        FineAggregate = flask.request.form['FineAggregate']
        Age = flask.request.form['Age']

        input_variables = pd.DataFrame([[Cement, BlastFurnaceSlag, FlyAsh, Water, Superplasticizer, CoarseAggregate,FineAggregate,  Age]],
                                       columns=['Cement', 'BlastFurnaceSlag', 'FlyAsh', 'Water', 'Superplasticizer',
                                                'CoarseAggregate', 'FineAggregate', 'Age'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('index.html', original_input={'Cement': Cement, 'BlastFurnaceSlag': BlastFurnaceSlag, 'FlyAsh': FlyAsh, 'Water': Water, 'Superplasticizer': Superplasticizer, 'CoarseAggregate': CoarseAggregate, 'FineAggregate': FineAggregate, 'Age': Age},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
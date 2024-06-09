from flask import Flask
import matplotlib
matplotlib.use('Agg')
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import os       # Python < 3.4

app = Flask(__name__)

@app.route('/')

def index():
    
    data = pd.read_csv('AirPassengers.csv')
    data['Month'] = pd.to_datetime(data['Month'])

    data.columns = ['Month','Passengers']
    data['Month'] = pd.to_datetime(data['Month'], format='%Y-%m')
    data = data.set_index('Month')
    data.head(12)
    decomposition = sm.tsa.seasonal_decompose(data.Passengers, model='multiplicative')
    a = decomposition.seasonal
    a.plot()
    try:
        os.remove('foo.png')
    except OSError:
        pass
    plt.savefig('foo.png')
    return "Hello!"

if __name__ =="__main__":
    # app. run(debug=True)
    app.run(host='0.0.0.0', port=3001)
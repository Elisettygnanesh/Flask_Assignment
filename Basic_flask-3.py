from flask import Flask, render_template, request
import requests
app=Flask(__name__)

@app.route("/")
def open_app():
    return render_template('Basic_flask-3.html')

@app.route("/climateapp",methods=['POST'])
def climate_app():
    url="https://api.openweathermap.org/data/2.5/weather"
    params={'lat':request.form.get('lat'),'lon':request.form.get('lon'),'appid':request.form.get('appid')}
    response=requests.get(url,params=params)
    data=response.json()
    return f"Data:{data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8002)
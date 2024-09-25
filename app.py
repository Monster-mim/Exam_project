from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def weather():
    # Статичні дані (або API виклик для реальних даних)
    weather_data = {
        'city': 'Kyiv',
        'temperature': '25°C',
        'description': 'Sunny'
    }
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


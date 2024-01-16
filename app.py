from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api_endpoint', methods=['POST'])
def api_endpoint():
    data = request.json  # Получение данных из тела запроса (ожидается в формате JSON)
    
    # Обработка полученных данных
    # ...

    # Отправка ответа клиенту
    response_data = {'message': 'Данные успешно получены!'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4747, debug=True)

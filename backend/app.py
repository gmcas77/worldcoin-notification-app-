from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/send-notification", methods=["POST"])
def send_notification():
    data = request.json
    message = data.get("message")

    # Aquí tu endpoint de notificaciones de Worldcoin (dummy ahora)
    url = "https://api.worldcoin.org/notifications"

    payload = {
        "app_id": "app_7686f9027d3e3c0b53d987a3caf1e111",
        "title": "Notificación desde tu app",
        "body": message
    }

    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return jsonify({"status": "enviado", "response": response.json()}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)

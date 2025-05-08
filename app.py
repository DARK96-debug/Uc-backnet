from flask import Flask, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # frontenddan so‘rovlar uchun

BOT_TOKEN = "7714554918:AAHriVJ-tTmiUBbmABYJIaDnDiYDcejlMz4"
ADMIN_ID = "7098943602"  # sizning Telegram ID

@app.route('/')
def home():
    return "Bot backend ishlayapti!"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    pubg_id = data.get('pubg_id')
    nickname = data.get('nickname')
    telegram = data.get('telegram')
    uc = data.get('uc')

    message = f"Yangi UC buyurtma:\n\nPUBG ID: {pubg_id}\nNickname: {nickname}\nTelegram: @{telegram}\nUC: {uc}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": ADMIN_ID,
        "text": message
    }
    requests.post(url, json=payload)

    return {"status": "success"}

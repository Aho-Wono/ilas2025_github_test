import os
from dotenv import load_dotenv
import chatgpt
from pathlib import Path
import requests

dir = Path(__file__).parent # 親フォルダを取得

load_dotenv(f"{dir}/.env")
chatbot = chatgpt.ChatBot(api_key = os.environ.get("OPENAI_API_KEY"))

with open(f"{dir}/system_setting.txt", "r", encoding="utf-8") as f:
    system_setting = f.read()

chatbot.set_system_setting(system_setting) #ChatGPTに最初の命令文を設定する


while True:
    prompt = input("お住いの地域を入力してください：")
    message = chatbot.chat("地名：" + prompt)
    print(message)
    url = f"https://weather.tsukumijima.net/api/forecast/city/{message}"

    try: 
        data = requests.get(url).json() # json形式でデータを取得する
        print(data)




        break
    except Exception as e:
        print(f"想定外のエラーが発生しました。 {e}\nもう一度適切な地名を入力してください。")



print("プログラム終了")
import time
import requests

URL = "https://verificador-pod.onrender.com/"
INTERVALO = 600  # 10 minutos en segundos

while True:
    try:
        print("⏳ Haciendo ping a la app...")
        response = requests.get(URL)
        print(f"✅ Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    time.sleep(INTERVALO)

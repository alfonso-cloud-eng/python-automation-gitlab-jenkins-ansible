import os
import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler
from slack_sdk.webhook import WebhookClient

# Define los símbolos de las acciones
STOCKS = ["GOOGL", "AMZN", "META", "MSFT"]

# Obtén la URL del webhook desde una variable de entorno
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
if not SLACK_WEBHOOK_URL:
    raise ValueError("Debes definir la variable de entorno SLACK_WEBHOOK_URL con la URL de tu webhook de Slack")

# Inicializa el cliente del webhook de Slack
slack_client = WebhookClient(SLACK_WEBHOOK_URL)

def obtener_datos_acciones():
    mensajes = []
    for symbol in STOCKS:
        ticker = yf.Ticker(symbol)
        # Obtén datos del día actual con intervalos de 1 minuto
        data = ticker.history(period="1d", interval="1m")
        if data.empty:
            mensajes.append(f"{symbol}: No se pudieron obtener datos.")
            continue

        # Selecciona la última fila para el precio más reciente
        ultimo_dato = data.iloc[-1]
        precio_actual = ultimo_dato['Close']
        # Calcula la variación diaria usando el precio de apertura
        precio_apertura = data.iloc[0]['Open']
        variacion = ((precio_actual - precio_apertura) / precio_apertura) * 100

        mensaje = f"*{symbol}*\nPrecio actual: ${precio_actual:.2f}\nVariación diaria: {variacion:+.2f}%"
        mensajes.append(mensaje)
    return "\n\n".join(mensajes)

def enviar_mensaje_slack(texto):
    response = slack_client.send(text=texto)
    if response.status_code != 200:
        print(f"Error al enviar el mensaje a Slack: {response.status_code}, {response.body}")
    else:
        print("Mensaje enviado correctamente a Slack.")

def tarea_slack():
    texto = obtener_datos_acciones()
    enviar_mensaje_slack(texto)

def tarea_terminal():
    texto = obtener_datos_acciones()
    # Imprime en la terminal el resultado
    print("Datos de acciones (actualizados cada minuto):")
    print(texto)
    print("-" * 50)

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # Programa la tarea para enviar mensaje a Slack cada minuto
    scheduler.add_job(tarea_slack, 'interval', seconds=5)
    # Programa la tarea para imprimir en la terminal cada 5 segundos
    scheduler.add_job(tarea_terminal, 'interval', seconds=5)
    print("Scheduler iniciado. Presiona Ctrl+C para detener.")
    scheduler.start()

#Subscriber
import paho.mqtt.client as mqtt
def on_message(c,u,msg):
    print(f"Ricevuto:{msg.payload.decode()}")
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)
client.subscribe("smartconnect/lezione1")
client.on_message = on_message
client.loop_forever()
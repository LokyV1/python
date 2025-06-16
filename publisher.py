#publisher
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "smartconnect/lezione1"
client = mqtt.Client()
client.connect(broker, 1883)
client.publish(topic, "Temperatura: 22C")
client.disconnect()
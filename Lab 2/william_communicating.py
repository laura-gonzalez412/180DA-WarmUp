import paho.mqtt.client as mqtt
clientID = "Laura"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("user1touser2")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, msg):
    message_payload = msg.payload.decode()
    print('\n')
    print("Received message " + message_payload)

client = mqtt.Client(client_id=clientID) # creating this client


client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect_async("mqtt.eclipseprojects.io")

client.loop_start()

while True:
    message = input("Enter your message: ")
    print('\n')
    client.publish("fromuser2touser1", "from " + clientID + ": " + message)



client.loop_stop()
client.disconnect()

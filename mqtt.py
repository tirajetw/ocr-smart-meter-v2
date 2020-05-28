import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

Connected = False   #global variable for the state of the connection
 
broker_address= "202.28.244.147"  #Broker address
port = 1883                         #Broker port
user = "test04"                    #Connection username
password = "df367"            #Connection password
topic = "test04/a"
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
def pubMQTT(data):
    client.publish(topic,data)
    print("send MQTT")

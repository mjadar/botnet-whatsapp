import whatsapp
import sys



try:
    wtsp = whatsapp.WtspBot()
    contact    = 'Your Contact Name'
    msg        = 'Your Message here'
    repetition = 30
    wtsp.send_msg_to(contact,msg, repetition)
except Exception:
    sys.exit()
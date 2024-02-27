import time
import requests
from win11toast import toast
import tkinter as tk
from tkinter import simpledialog


ROOT = tk.Tk()
ROOT.geometry("500x200")
ROOT.withdraw()

USER_INP = simpledialog.askstring(title="", prompt="Inform the sedex code: ")
obj_code = USER_INP
canEnd = False
prev = ""

while canEnd == False:
    data = requests.get("https://rastreamento.correios.com.br/app/dataMaxima.php?objeto="+ obj_code +"&tipoPostal=N").json()
    if data["descricaoUltimoEvento"] != prev:
        toast('Pedido '+ obj_code, 'Status atualizado: '+ data["descricaoUltimoEvento"])
    prev = data["descricaoUltimoEvento"]
    if prev == "Entregue":
        canEnd = True
    else:
        time.sleep(120)
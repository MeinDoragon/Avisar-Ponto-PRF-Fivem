import psutil
import time
from tkinter import messagebox, Tk

def check_fivem():
    fivem_running = False
    for proc in psutil.process_iter():
        try:
            if "FiveM_b2699_GTAProcess.exe" in proc.name():
                fivem_running = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return fivem_running

root = Tk()
root.withdraw()

while True:
    if not check_fivem():
        messagebox.showinfo("Atenção", "Fivem não aberto!")
        time.sleep(10)
    else:
        while check_fivem():
            time.sleep(5)
        messagebox.showinfo("Atenção", "Não esqueça de fechar seu ponto no Discord!")
        root.destroy()
        break

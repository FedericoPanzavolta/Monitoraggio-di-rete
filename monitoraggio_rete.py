"""
Federico Panzavolta
Matricola: 0001077805

MONITORAGGIO DI RETE

"""

import os
import platform
import subprocess
import time

def ping_host(host):
    """
    Pingo un Host e ritorno 'True' se questo è raggiungibile, 'False' altrimenti
    """
    # Determino i comandi da usare in base al sistema operativo utilizzato sulla macchina
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", host]
    else:
        command = ["ping", "-c", "1", host]
    
    try:
        output = subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False

def monitor_hosts(hosts, interval=5):
    """
    Monitoro una lista di Host, pingandole ad intervalli regolari
    """
    while True:
        print("Controllo lo stato dell'Host...")
        for host in hosts:
            is_online = ping_host(host)
            status = "online" if is_online else "offline"
            print(f"Host {host} è {status}")
        print("Sleeping for {} seconds...".format(interval))
        time.sleep(interval)

def main():
    # Chiedo all'utente di inserire la lista di Host da monitorare separati da uno spazio bianco
    hosts = input("Inserire l'indirizzo IP degli Host da monitorare, separati da spazzi: ").split()

    # Chiedo all'utente di inserire l'intervallo tra un controllo e l'altro
    interval = int(input("Inserire l'intervallo di tempo tra un controllo e l'altro (in secondi): "))

    monitor_hosts(hosts, interval)

if __name__ == "__main__":
    main()

import socket
from concurrent.futures import ThreadPoolExecutor

def escanear_puerto(ip, puerto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            print("Puerto {puerto} está abierto.")
            return puerto, True
        else:
            return puerto, False
    except Exception as e:
        print(f"[!]Error conecntadose al puerto {puerto}: {e}")
        return puerto, False
    finally:
        sock.close()

def escanear_puertos(ip, rango_puerto):
    puertos_abiertos = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        resultados = executor.map(lambda puerto: escanear_puerto(ip, puerto), rango_puerto)
        for puerto, esta_abierto in resultados:
            print(f"Puerto {puerto} inaccesible.")
            if esta_abierto:
                puertos_abiertos.append(puerto)
    return puertos_abiertos

if __name__ == '__main__':
    ip_objetivo = input("Ingrese la IP que desea escanear: ")
    rango_puerto = range(1, 65536)
   
    puertos_abiertos = escanear_puertos(ip_objetivo, rango_puerto)
 
    if puertos_abiertos:
        print(f"Puertos abiertos en {ip_objetivo}: {puertos_abiertos}")
    else:
        print(f"[!]No se encontraron puertos abiertos en {ip_objetivo}")
        
        

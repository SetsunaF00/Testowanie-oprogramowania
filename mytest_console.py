import argparse
import os
import sys
import platform
import subprocess
import psutil

def get_bios_version():
    if platform.system() == 'Windows':
        try:
            bios_info = subprocess.check_output('systeminfo | findstr /C:"BIOS Version"', shell=True, text=True)
            print(bios_info)
        except subprocess.CalledProcessError as e:
            print(f"Błąd: {e}")
    else:
        print("Ta funkcja jest dostępna tylko na systemie Windows.")

def get_ipv4_info():
    try:
        ipconfig_result = subprocess.check_output('ipconfig', shell=True, encoding='cp850', errors='replace')
        print("Informacje o IPv4:\n" + ipconfig_result)
    except subprocess.CalledProcessError as e:
        print(f"Błąd: {e}")

def check_proxy():
    if platform.system() == 'Windows':
        try:
            proxy_info = subprocess.check_output('netsh winhttp show proxy', shell=True, text=True)
            print(proxy_info)
        except subprocess.CalledProcessError as e:
            print(f"Błąd: {e}")
    else:
        print("Ta funkcja jest dostępna tylko na systemie Windows.")

def get_host_name():
    host_name = platform.node()
    print(f"Host Name: {host_name}")


def get_system_info():
    system_info = f"System: {platform.system()} {platform.release()}\n"
    system_info += f"Liczba rdzeni CPU: {psutil.cpu_count(logical=False)}\n"

    # Dodajemy obsługę różnych systemów operacyjnych
    if platform.system() == 'Windows':
        try:
            ram_info = round(psutil.virtual_memory().total / (1024. ** 3), 2)
            system_info += f"Pamięć RAM: {ram_info} GB"
        except Exception as e:
            system_info += f"Błąd pobierania informacji o pamięci RAM: {e}"
    else:
        system_info += "Pamięć RAM: Niedostępna na tym systemie."

    # Zapisujemy wynik do zmiennej
    result = f"Informacje systemowe: {system_info}\n"
    # Dekodujemy wynik z cp1250 (może być inny, w zależności od systemu)
    decoded_result = result.encode('cp1250').decode('utf-8')

    # Wydrukuj zdekodowany wynik
    sys.stdout.write(decoded_result)

# Dodatkowe informacje, aby pomóc w zrozumieniu problemu
print(f"Kodowanie znaków w sys.stdout: {sys.stdout.encoding}")

def main():
    parser = argparse.ArgumentParser(description="Aplikacja do sprawdzania informacji o komputerze i połączeniu sieciowym")
    parser.add_argument("action", help="Działanie do wykonania (ipv4, proxy, bios, hostname)")

    args = parser.parse_args()

    if args.action == "ipv4":
        get_ipv4_info()
    elif args.action == "proxy":
        check_proxy()
    elif args.action == "bios":
        get_bios_version()
    elif args.action == "hostname":
        get_host_name()
    elif args.action == "system":
        get_system_info()
    else:
        print("Nieznane polecenie. Dostępne polecenia: ipv4, proxy, bios, hostname, system")

if __name__ == "__main__":
    main()

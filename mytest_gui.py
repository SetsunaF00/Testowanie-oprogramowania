import sys
import subprocess
import platform
import netifaces
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

class MyTestApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyTest")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.text_view = QTextEdit()
        self.layout.addWidget(self.text_view)

        self.button_ipv4 = QPushButton("Moje IPv4")
        self.button_proxy = QPushButton("Sprawdź Proxy")
        self.button_system_info = QPushButton("Informacje o systemie")
        self.button_bios = QPushButton("Wersja BIOS")
        self.button_host_name = QPushButton("Host Name")

        self.layout.addWidget(self.button_ipv4)
        self.layout.addWidget(self.button_proxy)
        self.layout.addWidget(self.button_system_info)
        self.layout.addWidget(self.button_bios)
        self.layout.addWidget(self.button_host_name)

        self.central_widget.setLayout(self.layout)

        self.button_ipv4.clicked.connect(self.get_ipv4_info)
        self.button_proxy.clicked.connect(self.check_proxy)
        self.button_system_info.clicked.connect(self.get_system_info)
        self.button_bios.clicked.connect(self.get_bios_version)
        self.button_host_name.clicked.connect(self.get_host_name)

    def get_ipv4_info(self):
        try:
            ipv4_info = "Informacje o IPv4:\n"
            interfaces = netifaces.interfaces()
            for interface in interfaces:
                addresses = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addresses:
                    for addr in addresses[netifaces.AF_INET]:
                        ipv4_info += f"Interfejs: {interface}\n"
                        ipv4_info += f"Adres IPv4: {addr['addr']}\n"
            self.text_view.setPlainText(ipv4_info)
        except Exception as e:
            self.text_view.setPlainText(f"Błąd: {e}")

    def check_proxy(self):

        if platform.system() == 'Windows':
            try:
                proxy_info = subprocess.check_output('netsh winhttp show proxy', shell=True, text=True)
                self.text_view.setPlainText(f"PROXY: {proxy_info}")
            except subprocess.CalledProcessError as e:
                self.text_view.setPlainText(f"Błąd: {e}")
        else:
            self.text_view.setPlainText(f"Ta funkcja jest dostępna tylko na systemie Windows.")

    def get_system_info(self):
        system_info = f"System: {platform.system()} {platform.release()}\n"
        system_info += f"Liczba rdzeni CPU: {psutil.cpu_count(logical=False)}\n"
        system_info += f"Pamięć RAM: {round(psutil.virtual_memory().total / (1024. ** 3), 2)} GB"
        self.text_view.setPlainText(f"Informacje systemowe: {system_info}")

    def get_bios_version(self):

        if platform.system() == 'Windows':
            try:
                bios_info = subprocess.check_output('systeminfo | findstr /C:"BIOS Version"', shell=True, text=True)
                self.text_view.setPlainText(f"BIOS Version: {bios_info}")
            except subprocess.CalledProcessError as e:
                self.text_view.setPlainText(f"Błąd: {e}")
        else:
            self.text_view.setPlainText(f"Ta funkcja jest dostępna tylko na systemie Windows.")

    def get_host_name(self):
        host_name = platform.node()
        self.text_view.setPlainText(f"Host Name: {host_name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyTestApp()
    window.show()
    sys.exit(app.exec_())

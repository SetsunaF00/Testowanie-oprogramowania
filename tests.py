import subprocess
import unittest

class MyTestAutomation(unittest.TestCase):

    def test_ipv4_info(self):
        command = "python mytest_console.py ipv4"
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            self.assertIn("IPv4", result)
        except subprocess.CalledProcessError as e:
            self.fail(f"Test failed with error: {e}")

    def test_proxy_check(self):
        command = "python mytest_console.py proxy"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn("proxy settings", result.lower())  # Sprawdzamy, czy wynik zawiera informacje o ustawieniach proxy

    def test_bios_version(self):
        command = "python mytest_console.py bios"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn("BIOS", result)

    def test_host_name(self):
        command = "python mytest_console.py hostname"
        result = subprocess.check_output(command, shell=True, text=True)
        self.assertIn("Host Name", result)

    def test_system_info(self):
        try:
            result = subprocess.check_output('python mytest_console.py system', shell=True, text=True)
            print(result)  # Wyświetlenie wyniku dla lepszej diagnozy
            self.assertIn("Informacje systemowe", result)  # Sprawdzenie, czy oczekiwany tekst jest obecny w wyniku
        except subprocess.CalledProcessError as e:
            print(f"Błąd: {e}")
            self.fail(f'Test failed with error: {e}')

if __name__ == '__main__':
    unittest.main()

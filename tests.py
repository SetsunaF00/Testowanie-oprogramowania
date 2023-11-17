import subprocess
import unittest
from mytest_console import get_system_info
import sys

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

    class MyTestAutomation(unittest.TestCase):

        def test_system_info(self):
            try:
                # Run the function and capture the result
                result = subprocess.run('python mytest_console.py system', shell=True, capture_output=True, text=True,
                                        check=True)

                # Decode the result using UTF-8
                decoded_result = result.stdout.encode('utf-8', errors='replace').decode(sys.stdout.encoding,
                                                                                        errors='replace')

                # Print the decoded result
                sys.stdout.write(decoded_result)

                # Check if the expected text is present in the result
                self.assertIn("Informacje systemowe", decoded_result)

            except subprocess.CalledProcessError as e:
                # In case of an error, print error information
                print(f"Błąd: {e}")
                print(f"Output błędu: {e.stdout}")
                print(f"Output stderr błędu: {e.stderr}")
                # Fail the test
                self.fail(f'Test failed with error: {e}')


if __name__ == '__main__':
    unittest.main()

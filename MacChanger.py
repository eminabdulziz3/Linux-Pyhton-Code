import subprocess

while True:

    connection = input("Enter the connection interface (eth0 or wlan0): ")

    if connection == "eth0":
        interface = "eth0"
        mac_adresse = "--random"
        break
    elif connection == "wlan0":
        interface = "wlan0"
        mac_adresse = "--random"
        break
    else:
        print("Invalid interface. Please enter eth0 or wlan0!!!")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["macchanger", mac_adresse, interface])
subprocess.call(["ifconfig", interface, "up"])
print("MAC address for {} changed successfully.".format(interface))

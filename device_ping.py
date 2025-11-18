import csv
import subprocess

def main(ip):

    if subprocess.os.name == "nt":
        param = "-n"
    else:
        param = "-c"

    command = ["ping", param, "1", ip]

    result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if result == 0:
        return True
    else:
        return False


def ip_add():

    devices = []

    with open("ip_address.txt") as file:
        reader = csv.reader(file)

        for row in reader:
            if row == []:
                continue

            ip = row[0]
            ip = ip.strip()

            is_up = ping(ip)

            if is_up == True:
                status = "UP"
            else: 
                status = "DOWN"

            devices.append([ip, status])

            print(f"{ip} is {status}")

if __name__=="__main__":
    main()

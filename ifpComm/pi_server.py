import socket
import subprocess
import os

if __name__=="__main__":
    if not os.path.isdir(os.getcwd()+"/check_mitm"):
        os.mkdir("check_mitm")
    path = os.getcwd() + "/check_mitm/"
    UDP_IP_ADDRESS = "192.168.0.136"
    UDP_PORT_NO = 6789
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    while True:
        data, addr = serverSock.recvfrom(1024)
        data = data.decode("utf-8")
        data = data.split("IP: ")
        ip = data[1].split(" ")[0]
        received_data = data[0]
        f = open(path + ip + ".json", "w")
        f.write(received_data)
        f.close()
        print("Message: " + ip)

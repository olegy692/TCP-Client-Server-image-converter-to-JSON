import base64
import socket
from json import dumps

imagename = 'C:\\Users\\olegs\\Desktop\\test.jpg'

# or for one image

with open(imagename, "rb") as images:  # for 1 image
    imagesToString = base64.b64encode(images.read())  # encode image to bytes

    base64_string = imagesToString.decode("utf-8")  # decode bytes to utf-8 string

    raw_data = {"image1": base64_string}  # dictionary

    json_data = dumps(raw_data)  # encoding data to json

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((socket.gethostname(), 12000))

clientSocket.send(json_data.encode())





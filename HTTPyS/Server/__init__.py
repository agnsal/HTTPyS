# coding : utf-8

'''
Copyright 2019 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''


from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import ssl
from time import time

from Controller import Controller
from configs import callbacks


class RequestHandler(BaseHTTPRequestHandler):
    __POSTCallback = callbacks['POST']
    __GETCallback = callbacks['GET']
    __controller = Controller()

    def send_response(self, responseCode, headerKeyword="", headerValue=""):
        """ Customized header """
        responseCode = int(responseCode)
        self.log_request(responseCode)
        self.send_response_only(responseCode)

    def do_GET(self):
        print("Hey, we have a GET Request!")  # Test
        print(self.path)  # Test
        result = self.__controller.manageGET(self.path)
        print(result) # Test
        if result["resource"] is None:
            self.send_error(404, "File Not Found: " + self.path)
        else:
            self.send_response(200)
            self.send_header("Content-type", result["Content-type"])
            self.send_header("Content-length", str(len(result["resource"])))
            self.end_headers()
            self.wfile.write(result["resource"])
        if self.__GETCallback:
            self.__GETCallback(self.path)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        receivedObj = self.rfile.read(content_length).decode('utf8').replace("'", '"').split("&")
        for i in range(0, len(receivedObj)):
            receivedObj[i] = receivedObj[i].split("=")
        receivedObj = dict(receivedObj)
        print("Hey, we have a POST Request!")  # Test
        print(str(receivedObj))  # Test
        self.__controller.managePOST(receivedObj=receivedObj)
        self.send_response(200)
        self.send_header('Date: ', self.date_time_string())
        self.end_headers()
        if self.__POSTCallback:
            self.__POSTCallback(receivedObj)

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class Server:
    __serverName = None
    __IPAddress = None
    __port = None
    __certificateFilePath = None
    __keyFilePath = None
    __handler = None

    def __init__(self, serverName="", IPAddress="", portNumber=443, certificateFilePath=None, keyFilePath=None):
        self.__serverName = str(serverName)
        self.__IPAddress = str(IPAddress)
        self.__port = int(portNumber)
        self.__certificateFilePath = str(certificateFilePath)
        self.__keyFilePath = str(keyFilePath)
        self.__handler = RequestHandler

    def setServerName(self, newServerName):
        self.__serverName = str(newServerName)

    def getServerName(self):
        return self.__serverName

    def setIPAddress(self, newIPAddress):
        self.__IPAddress = str(newIPAddress)

    def getIPAddress(self):
        return self.__IPAddress

    def setPortNumber(self, newPortNumber):
        self.__port = int(newPortNumber)

    def getPortNumber(self):
        return self.__port

    def setCertificateFilePath(self, newCertificateFilePath):
        self.__certificateFilePath = str(newCertificateFilePath)

    def getCertificateFilePath(self):
        return self.__certificateFilePath

    def setKeyFilePath(self, newKeyFilePath):
        self.__keyFilePath = str(newKeyFilePath)

    def runHTTPS(self, resourcePath):
        httpd = ThreadingSimpleServer((self.__IPAddress + str(resourcePath), self.__port), self.__handler)
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=self.__keyFilePath,
                                       certfile=self.__certificateFilePath, server_side=True)
        try:
            print("HTTPS Server " + self.__serverName + " running - " + str(time()))
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print("HTTPS Server " + self.__serverName + " stopped - " + str(time()))


    def runHTTP(self, resourcePath):
        httpd =ThreadingSimpleServer((self.__IPAddress + str(resourcePath), self.__port), self.__handler)
        try:
            print("HTTP Server " + self.__serverName + " running - " + str(time()))
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print("HTTP Server " + self.__serverName + " stopped - " + str(time()))

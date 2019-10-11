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


import requests


class Client:
    __clientName = None
    __useSSL = None

    def __init__(self, clientName="", useSSL=False):
        self.__clientName = str(clientName)
        self.__useSSL = bool(useSSL)

    def setClientName(self, newClientName):
        self.__clientName = str(newClientName)

    def getClientName(self):
        return self.__clientName

    def setUseSSL(self, newUseSSL):
        self.__useSSL = bool(newUseSSL)

    def getUseSSL(self):
        return self.__useSSL

    def GETRequest(self, serverURL="https://localhost", resourceURL="", serverPort=8000):
        serverResponse = requests.get(str(serverURL) + ":" + str(int(serverPort)) + str(resourceURL), verify=self.__useSSL)
        return serverResponse

    def POSTrequest(self, serverURL="http://localhost", resourceURL="", serverPort=8000, objToPost={'key': 'value'}):
        serverResponse = requests.post(str(serverURL) + ":" + str(int(serverPort)) + str(resourceURL), data=objToPost)
        return serverResponse

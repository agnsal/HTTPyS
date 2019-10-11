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


import HTTPyS.Client as Client


serverURL = "http://localhost"
resourceURL = "/index.html"
serverPort = 8000
testClient = Client.Client(clientName="testClient", useSSL=False)
serverGetResponse = testClient.GETRequest(serverURL=serverURL, resourceURL=resourceURL, serverPort=serverPort)
print(serverGetResponse)
serverPostResponse = testClient.POSTrequest(serverURL=serverURL, resourceURL=resourceURL, serverPort=serverPort, objToPost={'msg': 'hello', 'type': 'text'})
print(serverPostResponse)

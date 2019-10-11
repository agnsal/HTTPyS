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


import HTTPyS.Server as Server


# First of all, you have to create self signed SSL certificate and key file for tests:
# https://sourceforge.net/projects/openssl/
#
# openssl req -newkey rsa:2048 -nodes -keyout privkey.pem -x509 -days 36500 -out certificate.pem -subj "/O=CompanyTest/CN=testName/emailAddress=test@email.com"

def callback(value):
    print("Callback value: " + str(value))

testServer = Server.Server(IPAddress="localhost", portNumber=8000,
                           certificateFilePath="./SSLFiles/certificate.pem", keyFilePath="./SSLFiles/privkey.pem")
testServer.runHTTP("")



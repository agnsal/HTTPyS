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


from os import path

from configs import cssFilesRoot, jsFilesRoot, jsonFilesRoot, imgFilesRoot, actionsForPOST
from View import View

class Controller:
    __cssFilesRoot = None
    __jsFilesRoot = None
    __jsonFilesRoot = None
    __imgFilesRoot = None
    __View = None

    def __init__(self):
        assert path.isdir(cssFilesRoot)
        assert path.isdir(jsFilesRoot)
        assert path.isdir(jsonFilesRoot)
        assert path.isdir(imgFilesRoot)
        self.__cssFilesRoot = cssFilesRoot
        self.__jsFilesRoot = jsFilesRoot
        self.__jsonFilesRoot = jsonFilesRoot
        self.__imgFilesRoot = imgFilesRoot
        self.__View = View()

    def manageGET(self, reqPath=""):
        reqPath = str(reqPath)
        fileName = str(reqPath).split("/")[-1].split("?")[0]
        if ".css" in fileName:
            ct = "text/css"
            resource = self.takeResourceFile(root=self.__cssFilesRoot, fileName=fileName, mode="rb")
        elif ".json" in fileName:
            ct = "application/javascript"
            resource = self.takeResourceFile(root=self.__jsonFilesRoot, fileName=fileName, mode="rb")
        elif ".js" in fileName:
            ct = "application/javascript"
            resource = self.takeResourceFile(root=self.__jsFilesRoot, fileName=fileName, mode="rb")
        elif ".ico" in fileName or ".png" in fileName or ".jpeg" in fileName:
            ct = "image/x-icon"
            resource = self.takeResourceFile(root=self.__imgFilesRoot, fileName=fileName, mode="rb")
        else:
            ct = "text/html"
            resource = self.__View.takeView(fileName)
        return {"Content-type": ct, "resource": resource}

    def takeResourceFile(self, root="", fileName="", mode="rb"):
        resourcePath = root + fileName
        if path.isfile(resourcePath):
            resFile = open(resourcePath, mode)
            resource = resFile.read()
            resFile.close()
            return resource
        else:
            return None

    def managePOST(self, receivedObj):
        # Put here your code to manage post data
        '''
        if actionsForPOST[receivedObj["request"]] and actionsForPOST[receivedObj["request"]]["action"]:
            actionsForPOST[receivedObj["request"]]["action"](receivedObj)
        '''

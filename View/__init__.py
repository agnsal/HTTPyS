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
from mako.template import Template  # You can use another template engine, if you prefer

from configs import templatesRoot, templates

class View:
    __templatesRoot = None
    __templates = None

    def __init__(self):
        self.__templatesRoot = templatesRoot
        self.__templates = templates

    def takeView(self, fileName):
        return self.render(fileName)

    def render(self, fileName):
        print(fileName)
        dataToPass = None
        if templates[fileName]["model"]:
            dataToPass = templates[fileName]["model"]
        resourcePath = templatesRoot + templates[fileName]["name"]
        if path.isfile(resourcePath):
            resFile = open(resourcePath, "rb")
            resource = resFile.read()
            resFile.close()
            return Template(resource).render(data=str(dataToPass)).encode()
        else:
            return None

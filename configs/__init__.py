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


import Models

templatesRoot = "static/templates/"
cssFilesRoot = "static/css/"
jsFilesRoot = "static/scripts/"
jsonFilesRoot = "static/json/"
imgFilesRoot = "static/img/"

templates = {
    "index.html": {
        "name": "index.html",
        "model": Models.IndexViewModel,
    },
    "index": {
            "name": "index.html",
            "model": [],
        },
    "/": {
            "name": "index.html",
            "model": [],
        },
    "": {
        "name": "index.html",
        "model": [],
    },
}

actionsForPOST = {
    # "fooRequest": Models.Example.save,
}

def callbackTest(self, value):
    print("I'm the callbackTest!!! " + str(value))

callbacks = {
    "POST": callbackTest,
    "GET": callbackTest,
}

# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import webbrowser

_MARKDOWN_PREVIEW_EXAMPLE = """## Markdown Example

**Bold** and *italic* text.

A code block:
```python
def greet(name):
    return "Hello " + name
```
"""


def _build_markdown_preview(query):
    if query:
        return query + "\n\n---\n\n" + _MARKDOWN_PREVIEW_EXAMPLE
    return _MARKDOWN_PREVIEW_EXAMPLE


class HelloWorld(FlowLauncher):

    def query(self, query):
        return [
            {
                "Title": "Hello World, this is where title goes. {}".format(('Your query is: ' + query , query)[query == '']),
                "SubTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher"]
                },
            },
            {
                "Title": "This has a markdown preview with visibility set to \"always\"",
                "SubTitle": "PreviewVisibility: always, ContentType: markdown",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": _build_markdown_preview(query)
                },
                "PreviewVisibility": "always"
            },
            {
                "Title": "This has a markdown preview with visibility set to \"optional\"",
                "SubTitle": "PreviewVisibility: optional (default), ContentType: markdown",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": _build_markdown_preview(query)
                },
                "PreviewVisibility": "optional"
            },
            {
                "Title": "This has a markdown preview with visibility set to \"never\"",
                "SubTitle": "PreviewVisibility: never, ContentType: markdown",
                "IcoPath": "Images/app.png",
                "Preview": {
                    "ContentType": "markdown",
                    "Description": _build_markdown_preview(query)
                },
                "PreviewVisibility": "never"
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    HelloWorld()

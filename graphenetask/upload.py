import requests

files = {
    'operations': (None, '{"query": "mutation ($file: Upload) { myUpload(fileIn: $file) { ok }}", "variables": { "file": null }}'),
    'map': (None, '{ "0": ["variables.file"]}'),
    '0': ('news.txt', open('news.txt', 'rb')),
}

response = requests.post('http://localhost:8000/graphql', files=files)
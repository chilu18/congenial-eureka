{"filter":false,"title":"s3.py","tooltip":"/s3.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":17,"column":23},"action":"insert","lines":["import requests","import json","from pprint import pprint","","","# Get payload from file.","with open('keywords.json', 'r') as f:","    payload = json.loads(f.read())","","response = requests.request(","    'POST',","    'https://data.oxylabs.io/v1/queries/batch',","    auth=('user', 'pass1'),","    json=payload,",")","","# Print prettified response.","pprint(response.json())"],"id":1}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"remove","lines":["r"],"id":2},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"remove","lines":["e"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"remove","lines":["s"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"remove","lines":["u"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":21},"action":"insert","lines":["uhellosafe"],"id":3}],[{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"remove","lines":["1"],"id":4},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"remove","lines":["s"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"remove","lines":["s"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"remove","lines":["a"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":35},"action":"insert","lines":["m5qjr2NMZh"],"id":5}]]},"ace":{"folds":[],"scrolltop":123,"scrollleft":0,"selection":{"start":{"row":12,"column":35},"end":{"row":12,"column":35},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1610290304110,"hash":"1d9506847708ab5da5a43a3e25b2586449b4cdb3"}
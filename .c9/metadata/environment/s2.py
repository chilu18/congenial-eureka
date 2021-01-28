{"filter":false,"title":"s2.py","tooltip":"/s2.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":20,"column":23},"action":"insert","lines":["import requests","from pprint import pprint","","","# Structure payload.","payload = {","    'source': 'universal',","    'url': 'https://stackoverflow.com/questions/tagged/python',","}","","# Get response.","response = requests.request(","    'POST',","    'https://realtime.oxylabs.io/v1/queries',","    auth=('user', 'pass1'),","    json=payload,",")","","# Instead of response with job status and results url, this will return the","# JSON response with results.","pprint(response.json())"],"id":1}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":61},"action":"remove","lines":["https://stackoverflow.com/questions/tagged/python"],"id":2}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":53},"action":"insert","lines":["https://www.offshore-mag.com/rigs-vessels"],"id":3}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["r"],"id":4},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["e"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["s"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["u"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":21},"action":"insert","lines":["uhellosafe"],"id":5}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["1"],"id":6},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["s"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["s"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["a"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":25},"end":{"row":14,"column":35},"action":"insert","lines":["m5qjr2NMZh"],"id":7}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":25},"end":{"row":13,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1610289146082,"hash":"73298b5dcf14c07b46e9dbfc67f79a78e254b08e"}
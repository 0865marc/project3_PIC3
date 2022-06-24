import requests

data = {
    "userId": 100,
    "id": 100,
    "title": "test_post",
    "body": "here comes the text"
  }

resp = requests.post("http://jsonplaceholder.typicode.com/posts/",data=data)
if resp.status_code != 201:
    raise Exception('POST /posts/{}'.format(resp.status_code))
print('Created task. ID: {}}'.format(resp.json()["id"]))

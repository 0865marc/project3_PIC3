import requests

resp = requests.get("http://jsonplaceholder.typicode.com/posts/")
if resp.status_code != 200:
    # This means something went wrong.
    raise Exception('GET /tasks/{}'.format(resp.status_code))
for element in resp.json():
    print(element)

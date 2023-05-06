import requests


class MyRequests:
    def __init__(self):
        self.url = "http://localhost:9000/"
        
    def return_format(self, res):
        return res.status_code, res.json(), res.json().get('data')
    
    def reqGet(self, path):
        res = requests.get(self.url+path)
        return self.return_format(res)
    
    def reqPost(self, path, body):
        res = requests.post(self.url+path, json=body)
        return self.return_format(res)
    
    def reqPut(self, path, body=None):
        if body:
            res = requests.put(self.url+path, json=body)
        else:
            res = requests.put(self.url+path)
        return self.return_format(res)
    
    def reqDel(self, path):
        res = requests.delete(self.url+path)
        return self.return_format(res)

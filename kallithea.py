#!c:/Python27/python.exe
#coding:utf-8
"""
  Author:  LICFACE --<licface@yahoo.com>
  Purpose: 
  Created: 11/21/2017
"""

import requests
import sys
import json

class kallithea(object):
    def __init__(self, host = '192.168.1.2:5000', api = None, debug = False, **kwargs):
        self.host = host
        self.debug = debug
        self.URL = 'http://%s/_admin/api' % host
        if not api:
            self.API = 'a4585aadb592539a63f9937ae4e203669163536d'
        else:
            self.API = api
        if kwargs:
            for i in kwargs:
                setattr(self, i, kwargs.get(i))
                
    def setAPI(self, API):
        self.API = API
        return self.API
    
    def getAPI(self):
        return self.API
    
    def setHost(self, host, port = 5000):
        self.host = host + ":" + str(port)
        return self.host
    
    def setURL(self, url):
        return self.URL
    
    def create_repo(self, reponame, host = '192.168.1.2:5000', pid = 200, owner = 'root', repo_type = 'git', description = '', private = True, clone_uri = None, landing_rev = ":tip", enable_downloads = True, enable_locking = True, enable_statistics = True, api = None):
        if not host:
            host = self.host
        if not host:
            sys.exit('NO HOST')
        if not api:
            api = self.API
        if not api:
            sys.exit("API NOT FOUND !")
        data = {
            'id' : str(pid),
            'api_key' : api,
            'method' :  "create_repo", 
            'args':     {
                'repo_name':reponame,
                'owner':owner,
                'repo_type':repo_type,
                'description':description,
                'private':private,
                'clone_uri':clone_uri,
                'landing_rev':landing_rev,
                'enable_downloads':enable_downloads,
                'enable_locking':enable_locking,
                'enable_statistics':enable_statistics, 
            } 
        }
        #data = json.loads(data)
        print "data =", data
        a = requests.post(self.URL, json = data)
        print "RESPONSE = [" + str(a.status_code) + "]", a.content
        return a.status_code
    
if __name__ == '__main__':
    c = kallithea()
    c.create_repo(sys.argv[1], pid= 200)
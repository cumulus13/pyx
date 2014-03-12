import os
import spyce

#--------------------------------------------------[ a hardcoded fake request ]
class TestRequest(spyce.spyceRequest):
    environment = {'QUERY_STRING': '',
            'REQUEST_METHOD': 'get'}
    headers = {}
    
    def env(self, name=None):
        if not name:
            return self.environment
        return self.environment[name]
    
    def getHeader(self, type=None):
        return self.headers[type]
    
    def getServerID(self):
        os.getpid()


#--------------------------------------------------[ a hardcoded fake response ]
class TestResponse(spyce.spyceResponse):
    returncode = spyce.spyceResponse.RETURN_OK
    out = ''
    err = ''
    headers = {}
    def write(self, s):
        self.out = self.out+s
    def writeErr(self, s):
        self.err = self.err+s
    def close(self):
        pass
    def clear(self):
        self.out = ''
    def sendHeaders(self):
        pass
    def clearHeaders(self):
        self.headers = {}
    def setContentType(self, content_type):
        self.headers['content-type'] = content_type
    def setReturnCode(self, code):
        self.returncode = code
    def addHeader(self, type, data, replace=0):
        self.headers[type] = data
    def flush(self, *args):
        pass
    def unbuffer(self):
        pass


#--------------------------------------------------[ invoking Spyce code ]
import spyceConfig
    
req = TestRequest()
resp = TestResponse()

spyceCode  = 'Hello, the following names are defined: "[[print dir(),]]", and '
spyceCode += 'these were the parameters passed: [[print (a, b, c, d)]]\n',

spyce.spyceStringHandler(
             req,
             resp,
             spyceCode,
             sig='a, b, c="asd", d=None',
             args=(1, 'two'),
             kwargs={'c': 'aa'},
             config=spyceConfig)
print resp.err
print resp.out

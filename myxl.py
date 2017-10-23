import requests
import json

class myxl(object):

    def __init__(self):
        url = 'http://my.xl.co.id/4gquotainfo/queryQuotaInfo'
        cookies = {
        		'BIGipServerPool_my.xl.co.id': '3515424428.20480.0000',
        		'PHPSESSID': 'g71m7t62olg9j5bvv1s3os9v57',
        		'TS01e86ff7': '0188f9583ec34cb5100ef7ab6eca8e67ab5a07288a7c7f3a0171c0de3aa8e977478fe4c7c6234ab297a81075c51d9310bca3cea3f770563e368b72d7575f16db4e670359a680383b0e3b2c0726f7bc6c1b40e76d093112cd90b6ea87c805482f10dd05b2519fcc3143fc87a7e77ec5fa1cd652f9f2',
        		'axisnet': 'eyJhIjoiMjg4NzY4MjUxOF9jNGUzMjc1Mzg0MS00IiwiYiI6IldXZGlWazFJWDBGb1NXTmFaWEl4UjJ4VWFVNTJhMEZxZWtwQlEyNXBPV0kyZWs0NFkxSjBTV3RuU1QwPSIsImMiOiJpZCIsImQiOiIxIn0=',
        		'kmsi_channel': 'desktop',
        		'kmsi_token': '2887682518_c4e32753841-4'
        		}
        	
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        self.req = requests.get(url, headers=hdr, cookies=cookies)

    def parser(self):
        print "parser -> self.reg.text ="
        print unicode(self.req.text).encode('utf-8')
        
        data = unicode(self.req.text).encode('utf-8')
        data = json.loads(data)
        # print "data       =", data
        # print "type(data) =", type(data)
        print "Nomor              :", data.get('nomor')
        print "Sisa Quota         :", data.get('sisa_quota'), "({0} %)".format(data.get('percent_sisa_quota'))
        print "Usage Unlimited    :", data.get('usage_unlimited')
        print "Usage Quota        :", 4500 - 891.28, "({0} %)".format(data.get('percent_usage'))
        print "Active             :", data.get('tgl_mulai')
        print "Berakhir           :", data.get('tgl_berakhir'), "({0} %)".format(data.get('percent_sisa_hari'))
        print "Total Hari         :", data.get('total_hari')
        print "Total Quota        :", data.get('total_quota')
        print "Total Paket Aktif  :", data.get('total_paket_aktif')
        print "Package 4G         :", data.get('isPackage4g')
        print "Unlimited          :", data.get('isUnlimited')
        print "Device SIM         :", data.get('is_device_sim')


if __name__ == '__main__':
    c = myxl()
    c.parser()

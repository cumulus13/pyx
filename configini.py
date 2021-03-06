import ConfigParser
import os
import traceback
import re
from collections import OrderedDict
cfg = ConfigParser.RawConfigParser(allow_no_value=True)
THIS_PATH = os.path.dirname(__file__)
configname = 'conf.ini'

class MultiOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            super(OrderedDict, self).__setitem__(key, value)

def get_config_file(filename=''):
    if os.path.isfile(filename):
        filecfg = filename
    else:
        fcfg = os.path.join(os.path.dirname(__file__), configname)
        if os.path.isfile(fcfg):
            filecfg = fcfg
        else:
            f = open(fcfg, 'w')
            f.close()
            filecfg = fcfg
    return filecfg

def read_config(section, option):
    filecfg = get_config_file()
    cfg.read(filecfg)
    data = cfg.get(section, option)
    return data
    
def read_config2(section, option, filename=''): #format ['aaa','bbb','ccc','ddd']
    cfg = ConfigParser.RawConfigParser(allow_no_value=True, dict_type=MultiOrderedDict) 
    if os.path.isfile(os.path.join(THIS_PATH, filename)):
        cfg.read([filename])
    else:
        filename = os.path.join(THIS_PATH, configname)
        cfg.read([filename])
    cfg = cfg.get(section, option)
    return cfg

def read_config3(section, option, filename=''): #format result: [[aaa.bbb.ccc.ddd, eee.fff.ggg.hhh], qqq.xxx.yyy.zzz]
    data = []
    cfg = ConfigParser.RawConfigParser(allow_no_value=True, dict_type=MultiOrderedDict) 
    if os.path.isfile(os.path.join(THIS_PATH, filename)):
        cfg.read([filename])
    else:
        filename = os.path.join(THIS_PATH, configname)
        cfg.read([filename])
    cfg = cfg.get(section, option)
    for i in cfg:
        if "," in i:
            d1 = str(i).split(",")
            d2 = []
            for j in d1:
                d2.append(str(j).strip())
            data.append(d2)
        else:
            data.append(i)
    return data

def read_config4(section, option, filename=''): #format result: [aaa.bbb.ccc.ddd, eee.fff.ggg.hhh, qqq.xxx.yyy.zzz]
    data = []
    cfg = ConfigParser.RawConfigParser(allow_no_value=True, dict_type=MultiOrderedDict) 
    if os.path.isfile(os.path.join(THIS_PATH, filename)):
        cfg.read([filename])
    else:
        filename = os.path.join(THIS_PATH, configname)
        cfg.read([filename])
    cfg = cfg.get(section, option)
    if not cfg == None:
        for i in cfg:
            if "," in i:
                d1 = str(i).split(",")
                for j in d1:
                    data.append(str(j).strip())
            else:
                data.append(i)
        return data
    else:
        return None

def read_config5(section, option, filename=''): #format result: {aaa:bbb, ccc:ddd, eee:fff, ggg:hhh, qqq:xxx, yyy:zzz}
    data = {}
    cfg = ConfigParser.RawConfigParser(allow_no_value=True, dict_type=MultiOrderedDict) 
    if os.path.isfile(os.path.join(THIS_PATH, filename)):
        cfg.read([filename])
    else:
        filename = os.path.join(THIS_PATH, configname)
        cfg.read([filename])
    cfg = cfg.get(section, option)
    for i in cfg:
        if "," in i:
            d1 = str(i).split(",")
            for j in d1:
                d2 = str(j).split(":")
                data.update({str(d2[0]).strip():int(str(d2[1]).strip())})
        else:
            for x in i:
                e1 = str(i).split(":")
                data.update({str(e1[0]).strip():int(str(e1[1]).strip())})
    return data

def read_config6(section, option, filename=''): #format result: {aaa:[bbb, ccc], ddd:[eee, fff], ggg:[hhh, qqq], xxx:[yyy:zzz]}
    data = {}
    cfg = ConfigParser.RawConfigParser(allow_no_value=True, dict_type=MultiOrderedDict) 
    if os.path.isfile(os.path.join(THIS_PATH, filename)):
        cfg.read([filename])
    else:
        filename = os.path.join(THIS_PATH, configname)
        cfg.read([filename])
    cfg = cfg.get(section, option)
    for i in cfg:
        if ":" in i:
            d1 = str(i).split(":")
            d2 = int(str(d1[0]).strip())
            for j in d1[1]:
                d3 = re.split("['|','|']", d1[1])
                d4 = str(d3[1]).strip()
                d5 = str(d3[-2]).strip()
                data.update({d2:[d4, d5]})
        else:
            pass    
    return data

def write_config(section, option, value, filename=''):
    if os.path.isfile(os.path.join(THIS_PATH, filename)):
        cfg.read([filename])
    else:
        filename = get_config_file()
        cfg.read([filename])
    try:
        cfg.set(section, option, value)
    except ConfigParser.NoSectionError:
        cfg.add_section(section)
        cfg.set(section, option, value)
    cfg_data = open(filename,'wb')
    cfg.write(cfg_data)   
    
def get_config(section, option, value=None):
    try:
        data = read_config(section, option)
    except ConfigParser.NoSectionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config(section, option)
    except ConfigParser.NoOptionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config(section, option)
    return data

def get_config2(section, option, value=None):
    try:
        data = read_config2(section, option)
    except ConfigParser.NoSectionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config2(section, option)
    except ConfigParser.NoOptionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config2(section, option)
    return data

def get_config3(section, option, value=None):
    try:
        data = read_config3(section, option)
    except ConfigParser.NoSectionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config3(section, option)
    except ConfigParser.NoOptionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config3(section, option)
    return data

def get_config4(section, option, value=''):
    try:
        data = read_config4(section, option)
    except ConfigParser.NoSectionError:
        #print "Error 1 =", traceback.format_exc()
        write_config(section, option, value)
        data = read_config4(section, option)
        #print "data 1 =", data
    except ConfigParser.NoOptionError:
        #print "Error 2 =", traceback.format_exc()
        write_config(section, option, value)
        data = read_config4(section, option)
        #print "data 2 =", data
    #print "DATA =", data
    return data

def get_config5(section, option, value=None):
    try:
        data = read_config5(section, option)
    except ConfigParser.NoSectionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config5(section, option)
    except ConfigParser.NoOptionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config5(section, option)
    return data

def get_config6(section, option, value=None):
    try:
        data = read_config6(section, option)
    except ConfigParser.NoSectionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config6(section, option)
    except ConfigParser.NoOptionError:
        print traceback.format_exc()
        write_config(section, option, value)
        data = read_config6(section, option)
    return data

def write_all_config(filename=''):
    pass

def read_all_config(filename='', section=None):
    filecfg = get_config_file(filename)
    cfg.read(filecfg)    
    data = {}
    dbank = []
    if section !=  None:
        for x in cfg.options(section):
            d = cfg.get(section, x)
            data.update({x:d})
        dbank.append([section,data])        
    else:    
        for i in cfg.sections():
            section.append(i)
            for x in cfg.options(i):
                d = cfg.get(i, x)
                data.update({x:d})
            dbank.append([i,data])
    print "dbank =",  dbank
    
def read_all_section(filename='', section='server'):
    filecfg = get_config_file(filename)
    cfg.read(filecfg)    
    dbank = []
    dhost = []
    for x in cfg.options(section):
        d = cfg.get(section, x)
        #data.update({x:d})
        dbank.append(d)
        if d:
            if ":" in d:
                data = str(d).split(":")
                host = str(data[0]).strip()
                port = int(str(data[1]).strip())
                dhost.append([host,  port])
    #print "dbank =",  dbank
    #print "dhost =",  dhost
    return [dhost,  dbank]
        
def test():
    filename = get_config_file()
    cfg.read(filename)
    data = cfg.sections()
    print cfg.get('router','host')
    print data
        
#if __name__ == "__main__":
 #   print read_config4('forward', 'router')
    #print read_config5('config', 'DICT_LIST_MONTH')
#    print read_all_section(section='server')
    
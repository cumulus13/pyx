
def test01(param1 = 'prm1', param2 = 'prm2', **kwargs):
    #print "kwargs test01 1 =", kwargs
    kwargs.update({'data1': 'data001',})
    print "kwargs test01 2 =", kwargs
    
def test02(**kwargs):
    kwargs.update({'data2': 'data002',})
    test01(**kwargs)
    
test02()
    
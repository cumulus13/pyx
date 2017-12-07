import psutil
import sys
from make_colors import make_colors

if str(sys.argv[1]).isdigit():
    p = psutil.Process(sys.argv[1])
    p.terminate()
else:
    data = {}
    n = 1
    for i in psutil.process_iter():
        if str(sys.argv[1]).lower() in i.name() or str(sys.argv[1]).lower() == i.name():
            data.update({
                n: {
                    'name': i.name(),
                    'pid': i.pid,
                },
            })
            n += 1
    if len(data) > 1:
        q = raw_input('There is %s process with name %s, select number terminate to [a[all] for terminate all process]: ')
        if str(q).strip().isdigit():
            if int(q) in data.keys():
                p = psutil.Process(int(data.get(int(q)).get('pid')))
                p.terminate()
    else:
        if data:
            p = psutil.Process(int(data.get(1).get('pid')))
            print make_colors('TERMINATE: ', 'lightwhite', 'lightred', color_type= 'colorama') + make_colors(str(sys.argv[1]), 'lightyellow') + make_colors(" [%s]" % str(data.get(1).get('pid')), 'lightred')
            p.terminate()
        else:
            print make_colors('NOT FOUND !', 'white', 'red', attrs= ['blink'])
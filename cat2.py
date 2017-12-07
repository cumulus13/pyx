def readme(data):
    with open(data) as f:
        g = f.readlines()
        for i in g:
            if i == '\n':
                print i
            elif i == '\n\n':
                i.replace('\n\n', '\n')
            elif i == '\r':
            	pass
            else:
                print str(g.index(i)) + ". " + i.strip()


if __name__ == '__main__':
    import sys
    readme(sys.argv[1])

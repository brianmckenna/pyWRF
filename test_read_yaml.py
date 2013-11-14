import yaml

stram = open("namelist.yml", "r")
docs = yaml.load_all(stram)
for doc in docs:
    for k,v in doc.items():
        print k
        for ks,vs in sorted(v.items()):
            print '\t%s_%s' % (k,ks)
            for i in vs:
                print '\t\t%s' % (i)
    print "\n",

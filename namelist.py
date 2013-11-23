import yaml

ymlfile = open("namelist.yml", "r")
documents = yaml.load_all(ymlfile)

namelist = {}

for document in documents:
	# sections
    for sname,s in document.items():
    	# parameters
    	parameters = {}
    	for pname, p in s.items():
            if not isinstance(p, dict):
                continue
            if not ('type' in p and 'description' in p):
                continue
            parameters[pname] = p['type'] # TODO: this will be the value, check type
        namelist[sname] = parameters
        #for ks,vs in sorted(v.items()):
        #    print '\t%s_%s' % (k,ks)
        #    for i in vs:
        #        print '\t\t%s' % (i)
    #print "\n",

print namelist
import logging as log
import yaml
import types

example = {
    'time_control': {
        'run_days': 1,
        'run_hours': 12,
        'run_minutes': 0,
        'run_seconds': 0,

        'start_year': 2013,
        'start_month': 11,
        'start_day': 25,
        'start_hour': 0,
        'start_minute': 0,
        'start_second': 0,

#        'tstart': 'int',    

        'end_year': 2013,
        'end_month': 11,
        'end_day': 26,
        'end_hour': 12,
        'end_minute': 0,
        'end_second': 0,

        'interval_seconds': 10800,

        'input_from_file': False,
#        'input_from_file': 1, # TypeError example
#        'fine_input_stream': 'int',

        'history_interval': 60,
        'frames_per_outfile': 1,

        'restart': False,
        'cycling': False,

        'restart_interval': 11520,
        'reset_simulation_start': False,

        'io_form_history': 2,
        'io_form_restart': 2,
        'io_form_input': 2,
        'io_form_boundary': 2, # -- also test 6

#        'frames_per_emissfile': 'int',
#        'io_style_emiss': 'int',

        'debug_level': 0,
        'diag_print': 0,

#        'all_ic_times': 'boolean',
#        'adjust_output_times': 'boolean'
#        'override_restart_timers': 'boolean',
#        'write_hist_at_0h_rst': 'boolean',

        'auxinput1_inname': 'met_em.d<domain>.<date>',
 
#        'auxhist2_outname': 'string',
#        'auxhist2_interval': 'int',
#        'io_form_auxhist2': 'int',
#        'frames_per_auxhist2': 'int',


#        'ignore_iofields_warning': 'boolean',
#        'iofields_filename': 'string',

    },
}

def schema(ymlfilename):

    ymlfile = open(ymlfilename, "r")
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
                if p['type'] == 'boolean':
                    parameters[pname] = bool # TODO: this will be the value, check type
                elif p['type'] == 'int':
                    parameters[pname] = int
                elif p['type'] == 'float':
                    parameters[pname] = float
                elif p['type'] == 'string':
                    parameters[pname] = basestring
                else:
                    continue
            namelist[sname] = parameters
            #for ks,vs in sorted(v.items()):
            #    print '\t%s_%s' % (k,ks)
            #    for i in vs:
            #        print '\t\t%s' % (i)
        #print "\n",
    return namelist

def check(n):
    ns = schema("namelist.yml")
    # sections
    for s,section in n.iteritems():
        for k,v in section.iteritems():
            log.debug('\t%s\t%s' % (k,v))
            # check type
            if not isinstance(v,ns[s][k]):
                raise TypeError( '%s->%s expected %s is %s' % (s,k,ns[s][k],type(v)))
            # if values then check is key TODO
    return True


#n = schema("namelist.yml")
#print n
#print
assert check(example) is True

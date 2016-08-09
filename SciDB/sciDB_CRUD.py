import numpy as np
from scidbpy import connect
sdb = connect('http://localhost:48080') # connect to the database
from scidbpy.parse import _fmt

singles = {}

dtypes = 'int8 int16 int32 int64 uint8 uint16 uint32 uint64 float double datetime datetimetz bool string char'.split()
vals = [-128, -2**15+2, -2**31+2, -2**63+2, 2**8-1, 2**16-1, 2**32-1, 2**63-1, 1.23, 1e100, "'01/01/2001 12:23'", "'01/01/2001 12:23:01 +05:00'", 'true', "'test'", "'a'"]

#Create
def make(dtype, val):
    return sdb.afl.build('<x:%s>[i=0:1,10,0]' % dtype, val).eval()

#Retrieve
def run(make):
    for dtype, val in zip(dtypes, vals):
        a = make(dtype, val)
        print a
        print 'Plaintext:', repr(sdb._scan_array(a.name))
        print 'Binary :', repr(sdb._scan_array(a.name, fmt=_fmt(a)))
        print 'NumPy :', a.toarray()
        print '-----------'

	if dtype == 'bool' :
	    a.relabel('update')
	    print 'Update:'
	    print '-----------'

	#Delete
        a.reap()


run(make)

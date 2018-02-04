#!/usr/bin/python2

import sys
import re
import string
 
if len (sys.argv) != 3:
    print 'Usage: %s bkp exe' % sys.argv[0]
    exit (1)
 
(progname, bkp, exe) = sys.argv
 
def is_valid_hex (hex_str):
    if len (hex_str) != 4:
        return False
 
    for c in hex_str:
        if c not in string.hexdigits:
            return False
 
    return True
 
fp = open (bkp)
 
content = ''
for idx, line in enumerate (fp.readlines ()):
    line = re.sub (' +', ' ', line)
    fields = line.split (' ')
 
    for field in fields:
        if is_valid_hex (field):
            content += field.decode ('hex')
fp.close ()
 
fp_out = open (exe, 'wb')
fp_out.write (content)
fp_out.close ()

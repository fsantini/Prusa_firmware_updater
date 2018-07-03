#!/usr/bin/env python
#
# Python script for flashing Prusa i3 Mk3/Mk2.5 firmware (with separate language packs)
#
# Requires avrdude
#
# Copyright 2018 Francesco Santini <francesco.santini@gmail.com>
#
# Contains code derived from Prusa Research Slic3r https://github.com/prusa3d/Slic3r
# Released under the same license as Slic3r: GNU AFFERO GENERAL PUBLIC LICENSE v3
# Available under https://raw.githubusercontent.com/prusa3d/Slic3r/master/LICENSE

import sys
import subprocess
import re
import urllib


HEX_TERMINATOR = ":00000001FF"
AVRDUDE = "./avrdude"
AVRDUDE_CONF = "./avrdude.conf"



try:
    FILE = sys.argv[2]
    PORT = sys.argv[1]
except:
    print "Usage:", sys.argv[0], "[comm port] [hex file or url]"
    sys.exit(-1)

# check if file is url
urlRegex = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE)

if urlRegex.match(FILE): # file is an url
    # download the file
    print "Downloading firmware..."
    FILE,_ = urllib.urlretrieve(FILE)
    print "Firmware downloaded to", FILE

def find_languagepack(filename):
    res = 0
    with open(filename, 'r') as f:
        for l in iter(f.readline, ''): # need to use this to avoid buffering which screws up f.tell()
            l = l.strip()
            if l == HEX_TERMINATOR:
                if res == 0:
                    res = f.tell()
                else:
                    return res # make sure to return res only if another one had been found before
        return None
    
def escapeFilename(filename):
    return filename.replace(' ', '\ ')


print "Flash command:"
avrdudeCmd = [AVRDUDE, "-C%s" % (escapeFilename(AVRDUDE_CONF),), "-v", "-patmega2560", "-cwiring", "-P%s" % (PORT,), "-b115200", "-D", "-Uflash:w:0:%s:i" % (escapeFilename(FILE),)]
print ' '.join(avrdudeCmd)
subprocess.check_call(avrdudeCmd)

res = find_languagepack(FILE)
if res:
    print "Language pack found. Flashing it with:"
    avrdudeCmd = [AVRDUDE, "-C%s" % (escapeFilename(AVRDUDE_CONF),), "-v", "-patmega2560", "-carduino", "-P%s" % (PORT,), "-b115200", "-D", "-u", "-Uflash:w:%d:%s:i" % (res, escapeFilename(FILE))]
    print ' '.join(avrdudeCmd)
    subprocess.check_call(avrdudeCmd)
    
print "All done"

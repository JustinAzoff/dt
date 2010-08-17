#!/usr/bin/env python

import random
import md5
from optparse import OptionParser
import os

def md5sum(fn):
    m = md5.md5()
    f = open(fn)
    while True:
        buf = f.read(1024*8)
        if not buf:
            break
        m.update(buf)

    f.close()
    return m.hexdigest()

def test(fn, size):
    written = 0
    f = open(fn, 'w')
    bufsize = 1024*1024
    if bufsize > size:
        bufsize = size
    buf = ''.join(chr(random.randint(0,255)) for _ in xrange(bufsize))
    
    m = md5.md5()
    while written < size:
        f.write(buf)
        written += len(buf)
        m.update(buf)

    f.close()
    return m.hexdigest()

def do_test(fn, size):
    expected = test(fn, size)
    actual = md5sum(fn)

    if expected != actual:
        print "MISMATCHED CONTENTS"
        print "We think %s should be %s" % (fn, expected)
        print "But it is really      %s" % (actual)

    return expected == actual

def dt(files=10, size=1024*1024*10, nodelete=False, verbose=False):
    success = 0
    failures = 0
    for x in xrange(files):
        fn = "dt-%04d.img" % x
        if verbose:
            print "Pass: %04d/%04d (%s)" % (x+1, files, fn)
        if do_test(fn, size):
            success += 1
        else:
            failures += 1

        if not nodelete:
            os.unlink(fn)

    if failures:
        print "FAILURES DETECTED"
    print "success: %d, failures: %d" % (success, failures)

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", "--files",   dest="files", action="store",     type="int", help="The Number of files to create",default=10)
    parser.add_option("-s", "--size",    dest="size",  action="store",     type="int", help="The size of the files to create, in bytes",default=1024*1024*10)
    parser.add_option("-n", "--no-delete",dest="nodelete", action="store_true",        help="Whether to cleanup or not",default=False)
    parser.add_option("-v", "--verbose",dest="verbose", action="store_true",           help="The size of the files to create, in bytes",default=False)
    (options, args) = parser.parse_args()

    dt(options.files, options.size, options.nodelete, options.verbose)

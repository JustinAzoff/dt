#!/usr/bin/env python

from optparse import OptionParser

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", "--files",   dest="files", action="store",     type="int", help="number of files to create",default=10)
    parser.add_option("-s", "--size",    dest="size",  action="store",     type="int", help="size of each file",default=1024*10)
    parser.add_option("-n", "--no-delete",dest="nodelete", action="store_true",        help="",default=False)
    (options, args) = parser.parse_args()

    print options.files, options.size, options.nodelete

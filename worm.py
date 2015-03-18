"""
worm.py - an implementation of a worm, for academic purposes for course
INFO3155 Information Assurance and Security at UWI, Dept. of Computing.
This file is either to be used on a system with a Python environment, or
made into a standalone executable. It should ideally loaded onto a target
and executed somehow. When main() runs it should perform 3 basic tasks:
monitor and sendback resource usage of target system to some remote system,
replication, and propagation. We should be able to disable the replication/
propagation functions both at build and in use. We should also have a
reliable method of stopping the program at any time.
"""

import subprocess
import psutil
import socket

def main():
    """Main function of program."""
    #repl()
    #prop()     #maybe can use psutil for these as well..id new targets etc..?
    
    # Collect info
    memory = psutil.virtual_memory()
    memoryReport = "mem: "+bytes2human(memory.total)
    print memoryReport
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8080))
    s.send(memoryReport)
    s.close()
    pass

def repl():
    """Replication function."""
    pass

def prop():
    """Propagation function."""
    pass

def bytes2human(n):
    ## this code from https://github.com/giampaolo/psutil/blob/master/examples/meminfo.py
    
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

#if __name__ == '__main__':
#   main()
main()

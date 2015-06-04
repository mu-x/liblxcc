#!/usr/bin/python
'''PyBLD -- C++ Build System ;)
'''

import os

from glob import glob
from subprocess import Popen, PIPE

VERBOSE = True

DEFAULTS = dict(
    compiler = 'g++',
    flags = ['-std=c++11', '-Wall'],
    libs = [],
    isLib = False,
    libFlags = ['-shared', '-fPIC'],
    source = '',
    files = '*.cpp',
    output = './build',
)

class Error(Exception):
    pass

class Target(object):
    def __init__(self, source='', **info):
        self.__dict__.update(**DEFAULTS)
        self.__dict__.update(**info)
        self.sources = glob(os.path.join(source, self.files))
        self.name = getattr(self, 'name', source or 'noname')
        if self.isLib:
            self.flags += self.libFlags
            self.name = 'lib%s.so' % self.name
        self.target = os.path.join(self.output, self.name)

    def command(self):
        return [self.compiler] + self.flags + \
            ['-l' + lib for lib in self.libs] + \
            self.sources + ['-o', self.target]

    def build(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        cmd = self.command()
        if VERBOSE: print 'Building', self.name, '...'
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        if proc.returncode:
            line = ' '.join(["'%s'" % i if ' ' in i else i for i in cmd])
            raise Error('\n'.join(
                ['Could not build: ' + self.name, 'Command: ' + line] +
                (['', out] if out else []) + (['', err] if err else [])))

if __name__ == '__main__':
    try:
        Target('lxcc', isLib=True, libs=['pthread']).build()
        print 'Done!'
    except Error, e:
        print e



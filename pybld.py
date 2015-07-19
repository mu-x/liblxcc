#!/usr/bin/python
'''PyBLD -- C++ Build System ;)

Usage: bybld [VARIABLE_NAME=VALUE ...] [target]
'''

import os

from subprocess import check_call as run
from glob import glob

TARGETS = {} # all build targets
OPTIONS = {} # global options override

def target(name, make, **opts)
    '''Registers target [name] to call [make] with [opts]
    '''
    for key, value in opts.items:
        if not isinstance(opt, list): opts[key] = value
        else: opts[key] = values + opts.get(key, [])
    TARGET[name] = lambda: make(opts)

def pfix(prefix, items): return list(prefix + i for i in items)

def cxx(cxx='g++', flags=[], libdir=[], includes=[], libs=[], srcs=[],
        target='a.out', output='build', **more):
    for t in libs: TARGETS.get(t, lambda: 0)()
    if not os.path.exists(output): os.makedirs(output)
    run([cxx] + flags + pfix('-L', libdirs + output) + pfix('-l', libs) + \
        pfix('-I', includes) + srcs + ['-o', os.path.join(output, target)])

def cxx_so(target, **opts):
    opts['flags'] += ['-shared', '-fPIC']
    opts['target'] = 'lib%s.so' % target
    make_cxx(**opts)

def cxx_gtest(**opts):
    opts['libs'] += ['gtest', 'gtest_main']
    make_cxx(**opts)

def target_cxx(name, make=cxx, mask='*.cpp', **opts):
    opts['srcs'] = glob(os.path.join(name.replace('-', os.path.sep), mask))
    target(name, make, **opts)

def target_test(name, binary, **opts):
    def make(opts):
        TARGETS.get(binary, lambda: 0)()
        run(binary)
    target(name, make, **opts)

def target_list(name, targets, **opts):
    target(name, lambda opts: (t() for t in targets), **opts)

if __name__ == '__main__':
    targets = []
    for arg in sys.argv:
        param = arg.split('=')
        if len(param) == 2:
            if ',' not in param[1]: OPTIONS[param[0]] = param[1]
            else: OPTIONS[param[0]] = param[1].split(',')
        else:
            targets.append(arg)

    target_cxx('lxcc', cxx_so)
    target_cxx('lxcc-test', cxx_gtest, libs=['lxcc'])
    target_test('lxcc-runtest', 'lxcc-test')
    for t in targets:

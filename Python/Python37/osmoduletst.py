import os

def osmethodtest():
    #print(os.get_exec_path())
    print(os.getenv('OS'))

    curworkdir = os.getcwd()
    homedir = os.getenv('HOMEPATH')

    print("curworkdir: {},  homedir: {}".format(curworkdir, homedir))

def profilefunc(cls, param, wparam):
    print('profilefunc')

def sysmethodtest():
    import sys

    print('argv: {}, argc: {}'.format(sys.argv, len(sys.argv)))
    print(sys.base_exec_prefix, sys.base_prefix)

    import configparser
    config = configparser.ConfigParser(sys.argv)
    print(config.options('-o'))

    
    #mydir = 'input/profile/base.env'
    mydir = os.getcwd()
    pyfile = mydir + '/Test.py'
    base = os.path.basename(pyfile)
    filepath, filename = os.path.split(pyfile)
    head, suffix = os.path.splitext(pyfile)
    print('basename: {}, filepath: {}, filename: {}, head: {}, suffix: {}'.format(base, filepath, filename, head, suffix))


if __name__ == "__main__":
    osmethodtest()

    sysmethodtest()


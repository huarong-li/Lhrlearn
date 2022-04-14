import os
from posixpath import basename

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
    config = configparser.ConfigParser()

    config.read_file(open('./Python/Python37/config.cfg'))
    print(config.options('a'))
    
    #mydir = 'input/profile/base.env'
    mydir = os.getcwd()
    pyfile = mydir + '/Test.py'
    base = os.path.basename(pyfile)
    filepath, filename = os.path.split(pyfile)
    head, suffix = os.path.splitext(pyfile)
    print('basename: {}, filepath: {}, filename: {}, head: {}, suffix: {}'.format(base, filepath, filename, head, suffix))

    def export_api():
        print("export_api")
    import argparse
    arg_parse=argparse.ArgumentParser()
    arg_parse.add_argument('-p', dest='export_api', action='store_const', const=export_api, help='export api')
    arg_parse.add_argument('-o', nargs='?', dest='output', help='export api',default='3',type=str)
    
    args = arg_parse.parse_args()
    print(args.output)
    if args.export_api:
        args.export_api()


if __name__ == "__main__":
    osmethodtest()

    sysmethodtest()


import fnmatch
import os,sys

def get_file_path(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)
 
 
def walk_helper(args, dir_name, files):
    if ".git" in dir_name:
        return
 
    names = []
 
    file_list, wildcards = args
    for wc in wildcards:
        wc_file_name = get_file_path(dir_name, wc)
        for file_ in files:
            if file_.endswith(".py") or file_.endswith(".pyc"):
                continue
            file_name = get_file_path(dir_name, file_)
            if (fnmatch.fnmatch(file_name, wc_file_name) and
                    not os.path.isdir(file_name)):
                names.append(file_name)
 
    if names:
        file_list.append((dir_name, names))

def walk_helper_1(args, dir_name, files):
    if ".git" in dir_name:
        return
 
    file_list, wildcards = args
    for wc in wildcards:
        wc_file_name = get_file_path(dir_name, wc)
        for file_ in files:
            if file_.endswith(".py") or file_.endswith(".pyc"):
                continue
            file_name = get_file_path(dir_name, file_)
            if (fnmatch.fnmatch(file_name, wc_file_name) and
                    not os.path.isdir(file_name) and is_import_header_file(file_name)):
                file_list.append(os.path.abspath(file_name))
 
def get_data_files(src_dir, *wildcards):
    file_list = []
    os.path.walk(src_dir, walk_helper_1, (file_list, wildcards))
    return file_list

jsdoc_imported_header_file_names = [
    'fs_actioncallback.h', 'fs_redaction.h', 'fs_basictypes.h',
    'fs_common.h', 'fs_image.h', 'fs_render.h',
    'fx_coordinates.h', 'fs_fdfdoc.h', 'fs_bookmark.h',
    'fs_filespec.h', 'fs_pdfdoc.h', 'fs_pdflayer.h',
    'fs_pdfpage.h', 'fs_readingbookmark.h', 'fs_search.h',
    'fs_security.h', 'fs_psi.h', 'fs_action.h',
    'fs_annot.h', 'fs_pdfgraphicsobject.h', 'fs_pdfform.h',
    'fs_pdfobject.h', 'fs_pdfnametree.h', 'fs_rendition.h',
    'fs_watermark.h', 'fs_headerfooter.h', 'fs_pdfattachments.h',
    'fs_signature.h', 'fs_fillsign.h', 'fs_DP_WebLinks.h',
    'fs_pdfpagelabel.h', 'fs_connectedpdf.h', 
]

jsdoc_imported_pageeditor_header_file_names = [
    'fs_pageeditor.h'
]

def is_import_header_file(filepath):
    for file in jsdoc_imported_header_file_names:
        if file in filepath:
            return True
    return False

def is_import_pageeditor_header_file(filepath):
    for file in jsdoc_imported_pageeditor_header_file_names:
        if file in filepath:
            return True
    return False

def write_to_file(filename, filestr_array):
    f1 = open(filename, 'w')
    for index in range(len(filestr_array)):
        f1.write(filestr_array[index])
        if index != len(filestr_array) -1:
            f1.write('\n')

def export_api(*args):
    print args
    files = get_data_files('..\\include', '*.h')
    #print files

    write_to_file('clangTool\\fileInfo\\fileList_local.txt', files)

import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-e', dest='export_api', action='store_const',
                        const=export_api, help='export api')

    args = parser.parse_args()
    if (args.export_api):
        args.export_api()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

def arg_parse_1(args):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('-o', '--output', nargs='?',
                        help='sum the integers (default: find the max)')
    parser.add_argument('-i', '--input', nargs='?', dest='input_file', default='3',type=str,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args(args)

    print args.integers
    print args.input_file
    print args.output
    print args.accumulate(args.integers)


if __name__ == "__main__":
    
    #arg_parse_1(['--sum', '-o', 'ddd.txt', '2'])
    #arg_parse_1(['--sum', '-i', 'ddd.txt', '2'])

    arg_parse()


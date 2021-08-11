import os
import sys
import shutil

# 查找exe文件位置

def normalize_and_reduce_paths(paths):
    """Return a list of normalized paths with duplicates removed.

    The current order of paths is maintained.
    """
    # Paths are normalized so things like:  /a and /a/ aren't both preserved.
    reduced_paths = []
    for p in paths:
        np = os.path.normpath(p)
        # XXX(nnorwitz): O(n**2), if reduced_paths gets long perhaps use a set.
        if np not in reduced_paths:
            reduced_paths.append(np)
    return reduced_paths

def normalize_and_reduce_path():
    paths = os.environ['PATH'].split(';')
    paths = normalize_and_reduce_paths(paths)
    path_str = ';'.join(paths)
    os.environ['PATH'] = path_str

def find_exe(exe, path=None):
    if path is None:
        path_ = os.environ['PATH']
        paths = path_.split(os.pathsep)
        base, ext = os.path.splitext(exe)

    if (isinstance(path, str)):
        if (os.path.isfile(os.path.join(os.path.abspath(path),exe))):
            os.environ['PATH'] += os.pathsep + os.path.abspath(path)
    
    if (isinstance(path, list)):
        for p in path:
            if (os.path.isdir(p)):
                os.environ['PATH'] += os.pathsep + os.path.abspath(p)

    for p in os.environ['PATH'].split(';'):
        fn = os.path.join(os.path.abspath(p),exe)
        if os.path.isfile(fn):
            return fn
    
    return exe

if __name__ == "__main__":
    jsexe_path = find_exe('clang-jsapi.exe')
    print(jsexe_path)
    cmd_list = []
    cmd_list.append(jsexe_path)
    cmd_list.append('-h')
    os.system(' '.join(cmd_list))

    jsexe_path1 = find_exe('clang-jsapi.exe', './cmdline_parse')
    print(jsexe_path1)
    cmd_list = []
    cmd_list.append(jsexe_path1)
    cmd_list.append('-h')
    os.system(' '.join(cmd_list))

    jsexe_path1 = find_exe('clang-jsapi.exe', ['./cmdline_parse', './pyinstall'])
    print(jsexe_path1)
    cmd_list = []
    cmd_list.append(jsexe_path1)
    cmd_list.append('-h')
    os.system(' '.join(cmd_list))

    normalize_and_reduce_path()

#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import subprocess
from distutils import log
from distutils.util import get_platform

import tkinter
import tkinter.messagebox
import tkinter.colorchooser
from tkinter.constants import *
import tkinter.dialog
import tkinter.simpledialog
import tkinter.commondialog


def runCmd(cmd, shell=True):
    import subprocess
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=shell)
    for line in iter(p.stdout.readline, b''):
        print(line)

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

def _find_exe(exe, paths=None):
    """Return path to an MSVC executable program.

    Tries to find the program in several places: first, one of the
    MSVC program search paths from the registry; next, the directories
    in the PATH environment variable.  If any of those work, return an
    absolute path that is known to exist.  If none of them work, just
    return the original program name, 'exe'.
    """
    if not paths:
        paths = os.getenv('path').split(os.pathsep)
    for p in paths:
        fn = os.path.join(os.path.abspath(p), exe)
        if os.path.isfile(fn):
            return fn
    return exe

def _find_visualstudio_installationpath():
    root = os.environ.get("ProgramFiles(x86)") or os.environ.get("ProgramFiles")
    if not root:
        return None

    try:
        path = subprocess.check_output([
            os.path.join(root, "Microsoft Visual Studio", "Installer", "vswhere.exe"),
            "-latest",
            "-prerelease",
            "-requires", "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
            "-property", "installationPath",
        ], encoding="mbcs", errors="strict").strip()
    except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
        return None
    
    if os.path.isdir(path):
        return path
    return None

def _find_msbuild():
    best_dir = _find_visualstudio_installationpath()
    if not best_dir:
        return None
    maybe_dir = ('Current', '15.0')
    for item in maybe_dir:
        ms_path = os.path.join(best_dir, "MSBuild", item, "Bin", "MSBuild.exe")
        log.info("MSBuild found %s", ms_path)
        if (os.path.isfile(ms_path)):
            return ms_path

    return None

def _find_vc2015():
    return None, None

def _find_vc2017():
    """Returns "15, path" based on the result of invoking vswhere.exe
    If no install is found, returns "None, None"

    The version is returned to avoid unnecessarily changing the function
    result. It may be ignored when the path is not None.

    If vswhere.exe is not available, by definition, VS 2017 is not
    installed.
    """
    import json

    root = os.environ.get("ProgramFiles(x86)") or os.environ.get("ProgramFiles")
    if not root:
        return None, None

    try:
        path = subprocess.check_output([
            os.path.join(root, "Microsoft Visual Studio", "Installer", "vswhere.exe"),
            "-latest",
            "-prerelease",
            "-requires", "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
            "-property", "installationPath",
        ], encoding="mbcs", errors="strict").strip()
    except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
        return None, None

    path = os.path.join(path, "VC", "Auxiliary", "Build")
    if os.path.isdir(path):
        return 15, path

    return None, None

def _find_vcvarsall(plat_spec):
    _, best_dir = _find_vc2017()
    vcruntime = None
    vcruntime_plat = 'x64' if 'amd64' in plat_spec else 'x86'
    if best_dir:
        vcredist = os.path.join(best_dir, "..", "..", "redist", "MSVC", "**",
            "Microsoft.VC141.CRT", "vcruntime140.dll")
        try:
            import glob
            vcruntime = glob.glob(vcredist, recursive=True)[-1]
        except (ImportError, OSError, LookupError):
            vcruntime = None

    if not best_dir:
        best_version, best_dir = _find_vc2015()
        if best_version:
            vcruntime = os.path.join(best_dir, 'redist', vcruntime_plat,
                "Microsoft.VC140.CRT", "vcruntime140.dll")

    if not best_dir:
        log.debug("No suitable Visual C++ version found")
        return None, None

    vcvarsall = os.path.join(best_dir, "vcvarsall.bat")
    if not os.path.isfile(vcvarsall):
        log.debug("%s cannot be found", vcvarsall)
        return None, None

    if not vcruntime or not os.path.isfile(vcruntime):
        log.debug("%s cannot be found", vcruntime)
        vcruntime = None

    return vcvarsall, vcruntime

class MyDialog(tkinter.Toplevel):
    def __init__(self, master, title=None, modal=True) -> None:
        tkinter.Toplevel.__init__(self, master)
        self.transient(master)
        if title: self.title(title)
        self.minsize(width=450, height=300)
        # self.attributes('-topmost', 1)
        if modal:
            self.grab_set()

    def doModal(self):
        self.focus_set()
        self.wait_window(self)

class MyCommonDialog(tkinter.commondialog.Dialog):
    def __init__(self, master, title=None) -> None:
        tkinter.commondialog.Dialog.__init__(self, master)

class MainWindow:
    def __init__(self, parent) -> None:
        self.root=parent
        self.win_flag1=tkinter.IntVar(self.root, 0)
        self.win_flag2=tkinter.IntVar(self.root, 0)
        self._winflag=None
        self.initWidgets()
    
    def initWidgets(self):
        self.button1 = tkinter.Button(self.root, text="First Window", command=self.button1_command)
        self.button1.place(x=70, y=40, width=200, height=40)
        self.button2 = tkinter.Button(self.root, text="Second Window", command=self.button2_command)
        self.button2.place(x=70, y=100, width=200, height=40)
        self.button3 = tkinter.Button(self.root, text="Second Window", command=(lambda self=self: self.onCommand_button(4)))
        self.button3.place(x=70, y=160, width=200, height=40)
        tkinter._default_root
        tkinter._cnfmerge
        print("tkinter.TkVersion: ", tkinter.TkVersion)

    def onActivate(self):
        print(locals().keys())
        print(self.__dict__.keys())
        print('root' in self.__dict__.keys())
        print('root1' in self.__dict__.keys())
        if ('root' in self.__dict__.keys() and isinstance(self.root, tkinter.Tk)):
            for k, v in self.__dict__.items():
                print(k, v)
            for k in self.__dict__.keys():
                print(k)
            for k in self.__dict__.values():
                print(k)
            for k in self.__dict__:
                print(k)

    def button1_command(self):
        if (self.win_flag1.get() == 0):
            self.win_flag1.set(1)
            d = tkinter.dialog.Dialog(None, {'title': 'File Modified',
                      'text':
                      'File "Python.h" has been modified'
                      ' since the last time it was saved.'
                      ' Do you want to save it before'
                      ' exiting the application.',
                      'bitmap': tkinter.dialog.DIALOG_ICON,
                      'default': 0,
                      'strings': ('Save File',
                                  'Discard Changes',
                                  'Return to Editor')})
            # d.protocol("WM_DELETE_WINDOW", d.quit)
            print(d.num)
            
            self.win_flag1.set(0)
        else:
            print("button1_command allready popup")

    def button2_command(self):
        if (self.win_flag2.get() == 0):
            self.win_flag2.set(1)
            next_win=MyDialog(self.root, "Second Window", modal=True)
            next_win.doModal()
            self.win_flag2.set(0)
        else:
            print("button2_command allready popup")
    
    def button3_command(self):
        result=tkinter.simpledialog.askinteger("dd", "sdsdss", minvalue=3, maxvalue=300, initialvalue=56)
        print(result)
    def onCommand_button(self, num):
        print(num)
        if num == 4:
            import base64
            import re
            print((base64.b64decode(base64.b64encode('Huarong'.encode('utf-8'))), 'ddd'))
            print('Huarong'.encode('utf-8'))
            _magic_re = re.compile(r'([\\{}])')
            _space_re = re.compile(r'([\s])', re.ASCII)
            match=_magic_re.search('{hh} "{height}" 54')
            print(tkinter._stringify(['[wi/dth] \hj34','{hh} "{height}" 54']))

            self.test()
            # dlg=MyCommonDialog(self.root, title='eee')
            # dlg.show()
    def test(self):
        plat_name=None
        if plat_name is None:
            plat_name = get_platform()

        _find_vcvarsall(plat_name)
        # log.set_verbosity(2)
        ms_build_path = _find_msbuild()

        self.generate_js()

    def test_python_info():
        import sys
        major, minor, micro, level, serial = sys.version_info
        levelnum = {'alpha': 0xA,
            'beta': 0xB,
            'candidate': 0xC,
            'final': 0xF,
           }[level]
        string = sys.version.split()[0] # like '2.3a0'

        print(" * For %s," % string)
        print(" * PY_MICRO_VERSION = %d" % micro)
        print(" * PY_RELEASE_LEVEL = %r = %s" % (level, hex(levelnum)))
        print(" * PY_RELEASE_SERIAL = %d" % serial)
        print(" *")

        field3 = micro * 1000 + levelnum * 10 + serial

        print(" * and %d*1000 + %d*10 + %d = %d" % (micro, levelnum, serial, field3))
        print(" */")
        print("#define FIELD3", field3)

    def add_dir_to_environ_path(self, path):
        __paths = []
        try:
            for p in os.environ['path'].split(';'):
                __paths.append(p)
        except KeyError:
            pass
        __paths.append(path)
        __paths = normalize_and_reduce_paths(__paths)
        new_env_path = ";".join(__paths)
        os.environ['path'] = new_env_path
    def generate_js(self, *args):
        #cmd /c %msys_path_exe% -msys -here ./build.sh cgw
        self.add_dir_to_environ_path('C:\msys64')
        msys_path_exe = _find_exe('msys2_shell.cmd') or 'msys2_shell.cmd'
        if not os.path.isfile(msys_path_exe):
            raise ValueError('msys not exist')

        cmd_list = []
        cmd_list.append(msys_path_exe)
        cmd_list.append('-mingw64')
        cmd_list.append('-defterm')
        cmd_list.append('-no-start')
        #cmd_list.append('-full-path')
        cmd_list.append('-here')
        #cmd_list.append('./build_prject_with_msys.cmd')
        cmd_list.append('./build.sh')
        cmd_list.append('sgw')

        cmd_str = ' '.join(cmd_list)
        runCmd(cmd_str)
        print('generate_js')


class App:
    def __init__(self) -> None:
        self.root=tkinter.Tk()
        self.root.config(width=400, height=250)
        self.root.title("Multi Windows Demo")
        self._main_Frame=MainWindow(self.root)
    def OnLaunched(self):
        self._main_Frame.onActivate()
        self.root.mainloop()
    def GetMainFrame(self):
        return self.root

if __name__ == "__main__":
    app=App()
    
    app.OnLaunched()

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        'include_files': 'cert/'
    } 
}

executables = [
    Executable('shoot.py', base=base)
]

setup(name='SHTR.proto',
      version='0.0.1',
      description='SHTR.prototype 1 . Expect lots of bugs. :(',
      options=options,
      executables=executables
      )

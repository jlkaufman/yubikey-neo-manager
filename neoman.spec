# -*- mode: python -*-
import os
import sys
from glob import glob

NAME = "YubiKey NEO Manager"

WIN = sys.platform in ['win32', 'cygwin']
OSX = sys.platform in ['darwin']

ICON = os.path.join('neoman', 'neoman.png')
if WIN:
    ICON = os.path.join('resources', 'neoman.ico')

elif OSX:
    ICON = os.path.join('resources', 'neoman.icns')

a = Analysis(['scripts/neoman'],
             pathex=[''],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

# DLLs and dylibs should go here.
libs = glob('lib/*.dll') + glob('lib/*.dylib') + glob('lib/*.so')
for filename in libs:  
    a.datas.append((filename[4:], filename, 'DATA'))
a.datas.append(('neoman.png', 'neoman/neoman.png', 'DATA'))

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=NAME if not WIN else '%s.exe' % NAME,
          debug=False,
          strip=None,
          upx=True,
          console=False , icon=ICON)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=NAME)

if OSX:
    app = BUNDLE(coll,
                 name="%s.app" % NAME,
                 icon=ICON)
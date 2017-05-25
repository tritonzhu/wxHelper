# -*- mode: python -*-

import ntpath
import PyQt5

block_cipher = None

data_files = [
    ('static', 'static'),
    ('templates', 'templates'),
]

binary_files = [
    ('icon', 'icon')
]

a = Analysis(['src\\main.py'],
             pathex=[os.path.join(ntpath.dirname(PyQt5.__file__), 'Qt', 'bin'),
             os.path.join(ntpath.dirname(PyQt5.__file__), 'Qt', 'plugins'),
             'src\\'],
             binaries=binary_files,
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='wxHelper',
          debug=True,
          strip=False,
          upx=False,
          console=True,
          icon='icon/icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='wxHelper')

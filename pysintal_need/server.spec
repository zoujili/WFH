# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['server.py'],
             pathex=['C:\\project\\ai\\server_v3','C:\\Users\\zoujil\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=['cython', 'sklearn', 'sklearn.utils._cython_blas','sklearn.utils._weight_vector','sklearn.neighbors.typedefs','sklearn.neighbors._quad_tree','sklearn.tree','sklearn.tree._utils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='server')

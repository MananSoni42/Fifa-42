# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['driver.py'],
             pathex=['/home/manan/Projects/fifa-42'],
             binaries=[],
             datas=[('assets/fonts/*', 'assets/fonts'), ('assets/img/*', 'assets/img'), ('assets/img/formations/*', 'assets/img/formations'), ('assets/img/running/*', 'assets/img/running')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Fifa-42',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

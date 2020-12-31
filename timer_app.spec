# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [("Pokemon_Smile_Envs/*","Pokemon_Smile_Envs"),
               ("Pokemon_Smile_Pokemon/*","Pokemon_Smile_Pokemon"),
               ("save.ini",".")]

a = Analysis(['timer_app.py'],
             pathex=['/Users/Ben/Desktop/Pokemon-Timer'],
             binaries=[],
             datas=added_files,
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
          [],
          exclude_binaries=True,
          name='timer_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='timer_app')
app = BUNDLE(coll,
             name='timer_app.app',
             icon="025.icns",
             bundle_identifier=None)

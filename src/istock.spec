# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['istock.py'],
             pathex=['E:\\CS311\\Final Project\\iStock\\src'],
             binaries=[],
             datas=[
                 (".\\assets\\logo.png","assets\\"),
                 (".\\view\\authen.py","view\\"),
                 (".\\view\\home.py","view\\"),
                 (".\\notify\\lineNotify.py","notify\\"),
                 (".\\db\\dbConnect.py","db\\"),
                 (".\\db\\istock.db","db\\"),
                 ],
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
          name='istock',
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
               name='istock')

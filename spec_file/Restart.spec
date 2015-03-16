# -*- mode: python -*-
from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())
a = Analysis(['C:\\uits\\compile\\restart\\main.py'],
             pathex=['C:\\uits\\Kivy-1.8.0-py2.7-win32\\PyInstaller-2.1\\Restart'],
             hiddenimports=[],
             runtime_hooks=None)
for d in a.datas:
    if 'pyconfig' in d[0]: 
        a.datas.remove(d)
        break
pyz = PYZ(a.pure)
exe = EXE(pyz,
		Tree('C:\\uits\\compile\\restart'),
		a.scripts,
		a.binaries,
		a.zipfiles,
		a.datas,
		name='Restart.exe',
		debug=False,
		strip=None,
		upx=True,
		console=False,
		icon='C:\\uits\\compile\\restart\\myicon.ico')

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
include_files = ["form.ui", "env/Scripts/pyside6-uic.exe", "imprint.txt"]

build_options = {'packages': ["PySide6" ], 'excludes': [], "include_files": include_files}


executables = [
    Executable('mainwindow.py', target_name = 'physics-project')
]

setup(name='physics-project',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)

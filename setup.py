from cx_Freeze import setup, Executable

include_files = []

build_options = {
    'packages': ["PySide6", "pandas", "openpyxl", "cx_Freeze", "matplotlib", "numpy"],
    'excludes': ["email"],
    "include_files": include_files
}

bdist_msi_options = {
    'upgrade_code': '{f172a143-1a96-4ee8-8044-3b1ca751a476}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\,
    }

executables = [
    Executable('mainwindow.py', base="Win32GUI", target_name='physics-project')
]

setup(name='physics-project',
      version='1.0',
      description='',
      options={'build_exe': build_options},
      executables=executables)

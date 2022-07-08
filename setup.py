from cx_Freeze import setup, Executable

include_files = []

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "program",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]main.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    ("StartupShortcut",  # Shortcut
     "StartupFolder",  # Directory_
     "program",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]main.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),
]

msi_data = {"Shortcut": shortcut_table}

build_options = {
    'packages': ["PySide6", "pandas", "openpyxl", "cx_Freeze", "matplotlib", "numpy"],
    'excludes': ["email"],
    "include_files": include_files
}

bdist_msi_options = {
    'upgrade_code': '{f172a143-1a96-4ee8-8044-3b1ca751a476}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\physics-project',
    }

executables = [
    Executable('mainwindow.py', base="Win32GUI", target_name='physics-project')
]

setup(name='physics-project',
      version='1.0',
      description='',
      options={'build_exe': build_options},
      executables=executables)

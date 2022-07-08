# Download
You can find all needed Files in builds/build.zip

# Build
To build this Project you need the package cx_freeze.
Then you can run "py setup.py build". The result will be located in /build.  

# Build /widgets/form.py from /form.ui
When you changed something in the /form.ui, you need to build the form.py new.
You can do that with "pyside6-uic form.ui -o widgets/form.py".x
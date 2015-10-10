from distutils.core import setup
import py2exe
import sys
sys.argv.append("py2exe")
py2exe_options={
    "compressed":1,
    "bundle_files":1}
setup(name="zentaonotice",
      windows=["zentaonotice.py"],
      zipfile=None,
      options={'py2exe':py2exe_options})

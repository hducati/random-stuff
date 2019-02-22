from cx_Freeze import setup, Executable
import sys, os
import scrapy_int


os.environ['TCL_LIBRARY']=r'C:/Programs/Python/Python35/tcl/tcl8.6'
os.environ['TK_LIBRARY']=r'C:/Programs/Python/Python35/tcl/tk8.6'

build_exe_options = dict(excludes=["tkinter"], includes=["idna.idnadata"], optimize=1)

setup(name="main_web_scraping",
      version="1.1",
      description="Scrap data",
      executables=[Executable("scrapy_int.py")],
      options=dict(build_exe=build_exe_options)
      )

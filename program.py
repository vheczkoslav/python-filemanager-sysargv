import sys
import os

if len(sys.argv) == 1:
       print("These are arguments you can use in this program:")
       print("\tcrefil\t<--Used to create files")
       print("\tafter any argument you can use --help to know more about program")
if len(sys.argv) == 2:
       if sys.argv[1] == "crefil":
              print("you need to pass 1 more argument: file name+type")
       else:
              print("no argument passed")

if len(sys.argv) == 3:
       if sys.argv[1] == "crefil":
              open(sys.argv[2], "w")
       if sys.argv[1] == "crefil" and sys.argv[2] == "--help":
              if sys.argv[2] == "--help":
                     print(r"there is only one argument needed for create file command: file name+format.\nexample: python program.py crefil test.txt or python program.py crefil 'C:\Users\Username\test.py'")      

if len(sys.argv) == 4:
       pass
       
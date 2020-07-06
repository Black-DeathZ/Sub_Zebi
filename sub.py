#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import os
print """
                                    /)
                                   //
               __卐__             //
              /-(____)           //
             ////- -|\          //
          ,____o% -,_          //
         /  \\   |||  ;        //
        /____\....::./\      //
       _/__/#\_ _,,_/--\    //
       /___/######## \/""-(\ )
     /___\  __  /___\/     |
    /____\\'__'//____\ _ _ _|

"""

hr = raw_input("Enter site name without www :")
sub_list = open("subs.txt").read()
subs = sub_list.splitlines()
os.system("clear")
for sub in subs:
    sb_check = ("http://"+sub+"."+hr)
    try:
        requests.get(sb_check)
    except requests.ConnectionError:
        pass
    else:

        print "[+] Valid ==>: ",sb_check

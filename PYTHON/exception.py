#!/usr/bin/python3


from shutil import ExecError


try:
    x = 10 / 0

except Exception as err:
    print('⚠ Division on 0 ⚠') 

finally:
    print('End of Programme, See you soon!')


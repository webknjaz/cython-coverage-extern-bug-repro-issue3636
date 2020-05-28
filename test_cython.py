import sys


def dumbtrace(frame, event, args):
    frame.f_code.co_filename.endswith('.pyx') and sys.stdout.write(
        "%015s:%-3s %09s\n" % (
            frame.f_code.co_filename,
            frame.f_lineno,
            event,
        ),
    )
    return dumbtrace  # "step in"


'--debug' in sys.argv and sys.settrace(dumbtrace)


import call_mymath
import call_mymath.call_mymath
from call_mymath.call_mymath import call_sinc
import flat_ns_call_mymath
from flat_ns_call_mymath import call_sinc as flat_ns_call_sinc


print('call_mymath package is located at:')
print(call_mymath.__file__)
print('call_mymath.call_mymath module is located at:')
print(call_mymath.call_mymath.__file__)
print('flat_ns_call_mymath package is located at:')
print(flat_ns_call_mymath.__file__)


print('calling call_sinc(7):')
print(call_sinc(7))


print('calling flat ns call_sinc(7):')
print(flat_ns_call_sinc(7))

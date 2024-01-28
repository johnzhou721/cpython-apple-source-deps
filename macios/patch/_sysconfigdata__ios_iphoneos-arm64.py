import os

# os.uname().machine is the host CPU architecture on the simulator
arch = os.uname().machine
if arch == 'x86_64':
    from x86_64_sysconfigdata__ios_iphoneos import *
elif arch == 'arm64':
    from arm64_sysconfigdata__ios_iphoneos import *
else:
    raise RuntimeError("Unknown iOS Catalyst architecture.")

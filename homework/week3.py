# sp20-516-252 E.Cloudmesh.Common.1 - 5
# sp20-516-252 E.Cloudmesh.Shell.1 - 3
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from time import sleep

# E.Cloudmesh.Common.1
# Develop a program that demonstrates the use of banner, HEADING, and VERBOSE
banner("my banner")

class Example(object):
    def doit(self):
        HEADING()
        print("hello")

Example().doit()

m = {"key": "value"}
VERBOSE(m)

# E.Cloudmesh.Common.2
# demonstrate the use of dotdict
data = {
    "test":"this tests dotdict"
}

data = dotdict(data)
print(data.test)

# E.Cloudmesh.Common.3
# demonstrate the use of Flat-Dict
data = {"name": "Jessica",
        "address": {
            "city":"New York",
            "state":"NY"
        }}
flat = FlatDict(data,sep =",")
print(flat)

# E.Cloudmesh.Common.4
# demonstrate the use of cloudmesh.common.Shell
result = Shell.pwd()
print(result)

# E.Cloudmesh.Common.5
# demonstrate the use of cloudmesh.common.StopWatch
StopWatch.start("hi")
sleep(1)
StopWatch.stop("hi")
print(StopWatch.get("hi"))
StopWatch.benchmark()

# E.Cloudmesh.Shell.1
# Installation, done

# E.Cloudmesh.Shell.2
# Write a new command with firstname as the command name

# E.Cloudmesh.Shell.3
# Write a new command and experiment with docopt syntax and argument
# interpretation of the dict with if conditions.

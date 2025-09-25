#python build and install 
```
git submodule update --init --recursive
pip3 install -r requirements.txt
pip3 wheel .
pip3 install opencl_tag-*.whl
```
#python usage
```
from opencl_tag import OPENCL_TAG
opencl_tag = OPENCL_TAG()
# only add a tag
opencl_tag.tag("infer")
#tag a duration, 0 mean start, 1 mean end,
opencl_tag.tag_duration("infer", 0)
do_infer
opencl_tag.tag_duration("infer", 1)
```
#for C++ code, include the src/opencl_tag.hpp
```
#include "opencl_tag.hpp"
// example 1
{
   AUTO_OPENCL_TAG tag("infer")
   do infer()
}
// example 2
OPENCL_TAG tag();
tag.tag("test")
// example 3
OPENCL_TAG tag();
// tag a duration, 0 mean start, 1 mean end,
tag.tag_duration("test", 0)
do infer()
tag.tag_duration("test", 1)
```

#for C++ and python code, all need to repacle Opencl library \
after run pip3 wheel ., the profile Opencl library is at ./bin/intercept/  \
for windows python, can put the OpenCL.dll in same direcotry with the python.exe \
for LINUX, can export LD_PRELOAD=./bin/intercept/libOpencl.so
```
# windows
set CLI_ChromePerformanceTiming=1
set CLI_DumpDir=C:\trace_dir
set CLI_ChromePerformanceTimingPerKernel=0
# linux
export CLI_ChromePerformanceTiming=1
export CLI_DumpDir=/your_trace_dir
export CLI_ChromePerformanceTimingPerKernel=0
# open the trace file with chrome in mode chrome://tracing
``


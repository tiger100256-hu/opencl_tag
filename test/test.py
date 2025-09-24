import time
from opencl_tag import OPENCL_TAG
cl_tag = OPENCL_TAG()
cl_tag.tag("test")
cl_tag.tag_duration("test1", 0)
time.sleep(0.01)
cl_tag.tag_duration("test1", 1)
cl_tag.tag_duration("test1", 0)
time.sleep(0.01)
cl_tag.tag_duration("test1", 1)

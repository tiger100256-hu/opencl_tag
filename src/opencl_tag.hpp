#ifndef _OPENCL_TAG_H
#define _OPENCL_TAG_H
#include <CL/cl.h>
#include <iostream>
#include <string>
#include <map>
#include <mutex>

class OPENCL_TAG_IMP {
public:
    OPENCL_TAG_IMP() {
        cl_int err;
        // Step 1: Get platform and device
        cl_platform_id platform;
        err = clGetPlatformIDs(1, &platform, nullptr);
        err |= clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 1, &device, nullptr);
        // Step 2: Create context and command queue
        context = clCreateContext(nullptr, 1, &device, nullptr, nullptr, &err);
    }
    void tag(std::string tag_name)  {
        cl_int err;
        const std::string source_str = "OPENCL_TAG:" + tag_name ;
        const char* source = source_str.c_str();
        cl_program program = clCreateProgramWithSource(context, 1, &source, nullptr, &err);
    }
    ~OPENCL_TAG_IMP() {
        clReleaseContext(context);
    }

private:
    cl_context context;
    cl_device_id device;
};
class OPENCL_TAG {
public:
    void tag(std::string tag_name) {
        static std::mutex myMutex;
        static OPENCL_TAG_IMP imp;
        std::lock_guard<std::mutex> lock(myMutex);
        imp.tag(tag_name);
    }
};

#endif /* _OPENCL_TAG_H */

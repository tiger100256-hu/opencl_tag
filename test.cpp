#include <CL/cl.h>
#include <iostream>
#include "opencl_tag.hpp"
#include <chrono>
#include <iostream>
#include <thread>
int main() {
    for (int i = 0; i < 10; i++) {
	    OPENCL_TAG test;
	    test.tag("test1");
	    std::this_thread::sleep_for(std::chrono::milliseconds(5));
	    test.tag("test2");
	    std::this_thread::sleep_for(std::chrono::milliseconds(5));
	    test.tag("test3");
	    std::this_thread::sleep_for(std::chrono::milliseconds(5));
    }
}

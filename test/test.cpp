#include <CL/cl.h>
#include <iostream>
#include <chrono>
#include <thread>
#include "../src/opencl_tag.hpp"
int main() {
    for (int i = 0; i < 10; i++) {
	    OPENCL_TAG test;
	    test.tag("test1");
	    std::this_thread::sleep_for(std::chrono::milliseconds(5));
	    test.tag("test2");
	    std::this_thread::sleep_for(std::chrono::milliseconds(5));
	    test.tag("test3");
	    std::this_thread::sleep_for(std::chrono::milliseconds(5));
	    test.tag_duration("test4");
	    std::this_thread::sleep_for(std::chrono::milliseconds(20));
	    test.tag_duration("test4", 1);
    }
    return 0;
}

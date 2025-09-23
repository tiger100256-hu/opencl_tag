cmake_minimum_required(VERSION 3.10)
project(opencl_tag)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(thirdparty)
set(OPENCL_DIR ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/opencl-intercept-layer/intercept/)
set(OpenCL_INCLUDE_DIRS ${OPENCL_DIR})
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/bin/intercept/Release/)
# Add executable
add_executable(user_event_example test.cpp)
# Link OpenCL
target_include_directories(user_event_example PRIVATE ${OpenCL_INCLUDE_DIRS})
target_link_libraries(user_event_example PRIVATE OpenCL)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(opencl_tag opencl_tag.cpp)
target_include_directories(opencl_tag PRIVATE ${OpenCL_INCLUDE_DIRS})
target_link_libraries(opencl_tag PRIVATE OpenCL)

set_target_properties(opencl_tag PROPERTIES
	   LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_SOURCE_DIR}/opencl_tag
	   LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_SOURCE_DIR}/opencl_tag
	   LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/opencl_tag)


# Install the module
install(TARGETS opencl_tag LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/opencl_tag")



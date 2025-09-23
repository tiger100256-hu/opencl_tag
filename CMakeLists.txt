cmake_minimum_required(VERSION 3.10)
project(opencl_tag_project)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(OPENCL_DIR ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/opencl-intercept-layer/intercept/)
set(OpenCL_INCLUDE_DIRS ${OPENCL_DIR})
if(WIN32)
    link_directories(${CMAKE_CURRENT_SOURCE_DIR}/bin/intercept/Release/)
else()
    link_directories(${CMAKE_CURRENT_SOURCE_DIR}/bin/intercept/)
endif()

# Add executable
add_executable(user_event_example test.cpp)
# Link OpenCL
target_include_directories(user_event_example PRIVATE ${OpenCL_INCLUDE_DIRS})
target_link_libraries(user_event_example PRIVATE OpenCL)
add_dependencies(user_event_example opencl-intercept-layer)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)
add_subdirectory(thirdparty)
pybind11_add_module(opencl_tag opencl_tag.cpp)
target_include_directories(opencl_tag PRIVATE ${OpenCL_INCLUDE_DIRS})
target_link_libraries(opencl_tag PRIVATE OpenCL)
add_dependencies(opencl_tag opencl-intercept-layer)

set_target_properties(opencl_tag PROPERTIES
	   LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_SOURCE_DIR}/opencl_tag
	   LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_SOURCE_DIR}/opencl_tag
	   LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/opencl_tag)



# Install the module
install(TARGETS opencl_tag LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/opencl_tag")



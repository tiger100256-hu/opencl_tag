
include(ExternalProject)
ExternalProject_Add(opencl-intercept-layer
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/opencl-intercept-layer
    BINARY_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../bin"
    CMAKE_ARGS
        "-DCMAKE_BUILD_TYPE=Release"
    BUILD_COMMAND ${CMAKE_COMMAND} --build . --config Release --target OpenCL
    INSTALL_COMMAND ""
)

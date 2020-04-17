cmake_minimum_required(VERSION 3.16)
project(example_module)

set(CMAKE_CXX_STANDARD 14)

add_library(example_module
        foo.c
        bar.c)

target_link_libraries(example_module C ${PYTHON_LIBRARIES})
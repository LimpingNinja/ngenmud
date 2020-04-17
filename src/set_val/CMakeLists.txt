cmake_minimum_required(VERSION 3.16)
project(set_val C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(set_val
    set_val.c
    set_val.h)

target_link_libraries(set_val C ${PYTHON_LIBRARIES})
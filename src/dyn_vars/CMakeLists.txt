cmake_minimum_required(VERSION 3.16)
project(dyn_vars C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(dyn_vars
    dyn_vars.c
    dyn_vars.h)

target_link_libraries(dyn_vars C ${PYTHON_LIBRARIES})
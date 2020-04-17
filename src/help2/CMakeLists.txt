cmake_minimum_required(VERSION 3.16)
project(help2 C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(help2
    hedit.c
    hedit.h
    help.c
    help.h)

target_link_libraries(help2 C ${PYTHON_LIBRARIES})
cmake_minimum_required(VERSION 3.16)
project(time C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(time
    mudtime.h
    time.c)

target_link_libraries(time C ${PYTHON_LIBRARIES})
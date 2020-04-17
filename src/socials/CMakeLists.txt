cmake_minimum_required(VERSION 3.16)
project(socials C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(socials
    socedit.c
    socedit.h
    socials.c
    socials.h)

target_link_libraries(socials C ${PYTHON_LIBRARIES})
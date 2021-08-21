cmake_minimum_required(VERSION 3.16)
project(alias C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(alias
        alias.c
        alias.h)

cmake_minimum_required(VERSION 3.16)
project(items C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(items
    container.c
    container.h
    furniture.c
    furniture.h
    iedit.c
    iedit.h
    items.c
    items.h
    portal.c
    portal.h
    worn.c
    worn.h)

target_link_libraries(items C ${PYTHON_LIBRARIES})
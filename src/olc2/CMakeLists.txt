cmake_minimum_required(VERSION 3.16)
project(olc2 C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(olc2
    accedit.c
    bedit.c
    esedit.c
    medit.c
    oedit.c
    olc.c
    olc.h
    olc_extender.c
    olc_extender.h
    olc_submenus.h
    pcedit.c
    protedit.c
    redit.c
    zedit.c)

target_link_libraries(olc2 C ${PYTHON_LIBRARIES})
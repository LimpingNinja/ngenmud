cmake_minimum_required(VERSION 3.16)
project(editor C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_library(editor
    editor.c
    editor.h
    notepad.c)

target_link_libraries(editor C ${PYTHON_LIBRARIES} scripts)
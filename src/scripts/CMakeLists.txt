cmake_minimum_required(VERSION 3.16)
project(scripts C)

set(CMAKE_C_STANDARD 11)
find_package (Python2 COMPONENTS Interpreter Development)

include_directories(.)

add_library(scripts
    pyaccount.c
    pyaccount.h
    pyauxiliary.c
    pyauxiliary.h
    pychar.c
    pychar.h
    pyevent.c
    pyevent.h
    pyexit.c
    pyexit.h
    pyhooks.c
    pyhooks.h
    pymud.c
    pymud.h
    pymudsys.c
    pymudsys.h
    pyobj.c
    pyobj.h
    pyolc.c
    pyolc.h
    pyplugs.c
    pyplugs.h
    pyroom.c
    pyroom.h
    pysocket.c
    pysocket.h
    pystorage.c
    pystorage.h
    script_editor.c
    script_editor.h
    scripts.c
    scripts.h
    trigedit.c
    triggers.c
    trighooks.c
    trighooks.h)

target_link_libraries(scripts C ${PYTHON_LIBRARIES} )

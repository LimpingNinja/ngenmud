cmake_minimum_required(VERSION 3.16)
project(ngenmud C)

set(CMAKE_C_STANDARD 11)
find_package(PythonInterp 2.7 REQUIRED)
find_package(PythonLibs 2.7 REQUIRED)

message("Python Libraries found: ${PYTHON_LIBRARIES}")

include_directories(.)
macro(SUBDIRLIST result curdir)
    file(GLOB children RELATIVE ${curdir} ${curdir}/*)

    foreach(child ${children})
        if(IS_DIRECTORY ${curdir}/${child} AND EXISTS ${curdir}/${child}/CMakeLists.txt AND NOT EXISTS ${curdir}/${child}/.exclude)
            list(APPEND dirlist ${child})
        endif()
    endforeach()
    set(${result} ${dirlist})
endmacro()

SUBDIRLIST(subdirs ${CMAKE_CURRENT_SOURCE_DIR})

foreach(subdir ${subdirs})
    add_subdirectory(${subdir})
    link_directories(${subdir})
    include_directories(${subdir})
    message("Adding module: ${subdir}")
endforeach()

add_executable(ngenmud
    account.c
    account.h
    action.c
    action.h
    auxiliary.c
    auxiliary.h
    bitvector.c
    bitvector.h
    body.c
    body.h
    buffer.c
    buffer.h
    character.c
    character.h
    command.c
    command.h
    commands.h
    event.c
    event.h
    exit.c
    exit.h
    extra_descs.c
    extra_descs.h
    filebuf.c
    filebuf.h
    gameloop.c
    handler.c
    handler.h
    hashtable.c
    hashtable.h
    hooks.c
    hooks.h
    inform.c
    inform.h
    interpret.c
    io.c
    list.c
    list.h
    log.c
    log.h
    map.c
    map.h
    mccp.c
    mud.c
    mud.h
    near_map.c
    near_map.h
    numbers.c
    numbers.h
    object.c
    object.h
    parse.c
    parse.h
    property_table.c
    property_table.h
    prototype.c
    prototype.h
    races.c
    races.h
    room.c
    room.h
    room_reset.c
    room_reset.h
    save.c
    save.h
    set.c
    set.h
    socket.c
    socket.h
    storage.c
    storage.h
    string_utils.c
    strings.c
    strings.h
    utils.c
    utils.h
    world.c
    world.h
    wrapsock.h
    zone.c
    zone.h socket_channel.c socket_channel.h)

link_directories( scripts dyn_vars set_val olc2 editor items )
link_directories( time socials alias help2)

target_link_libraries(ngenmud C ${PYTHON_LIBRARIES} ${subdirs} z)

install(TARGETS ngenmud DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/../bin)
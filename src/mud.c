//*****************************************************************************
//
// mud.c
//
// a bunch of variables and settings associated with the functioning, limits,
// and such of the MUD.
//
//*****************************************************************************

#include "mud.h"
#include "utils.h"
#include "storage.h"
#include "string.h"


//*****************************************************************************
// local defines, variables, and datastructures
//*****************************************************************************

//
// the file where we store all of our mud settings
#define MUD_DATA       "../lib/muddata"

//
// our storage set of mud settings
STORAGE_SET *settings = NULL;

//
// for generating unique IDs to characters, rooms, objects, exits, etc
int next_available_uid = START_UID;

int next_uid(void) {
    return next_available_uid++;
}

int top_uid(void) {
    if (next_available_uid == START_UID)
        return NOTHING;
    return next_available_uid - 1;
}


//*****************************************************************************
// implementation of functions in mud.h
//*****************************************************************************
void init_mud_settings() {
    settings = storage_read(MUD_DATA);

    // make sure we have initial values for some stuff
    if (!*mudsettingGetString("world_path"))
        mudsettingSetString("world_path", DFLT_WORLD_PATH);
    if (!*mudsettingGetString("start_room"))
        mudsettingSetString("start_room", DFLT_START_ROOM);
    if (mudsettingGetInt("pulses_per_second") == 0)
        mudsettingSetInt("pulses_per_second", DFLT_PULSES_PER_SECOND);
    if (mudsettingGetInt("listening_port") == 0)
        mudsettingSetInt("listening_port", DFLT_LISTEN_PORT);
    if (mudsettingGetInt("screen_width") == 0)
        mudsettingSetInt("screen_width", DFLT_SCREEN_WIDTH);
    if (mudsettingGetInt("paragraph_indent") == 0)
        mudsettingSetInt("paragraph_indent", DFLT_PARA_INDENT);
    if (!*mudsettingGetString("message_somewhere"))
        mudsettingSetString("message_somewhere", DFLT_SOMEWHERE);
    if (!*mudsettingGetString("message_something"))
        mudsettingSetString("message_something", DFLT_SOMETHING);
    if (!*mudsettingGetString("message_someone"))
        mudsettingSetString("message_someone", DFLT_SOMEONE);
    if (!*mudsettingGetString("message_nothing_special"))
        mudsettingSetString("message_nothing_special", DFLT_NOTHING_SPECIAL);
    if (!*mudsettingGetString("message_what"))
        mudsettingSetString("message_what", DFLT_WHAT);
    if (!*mudsettingGetString("required_pymodules"))
        mudsettingSetString("required_pymodules", "");
}

void mudsettingSetString(const char *key, const char *val) {
    store_string(settings, key, val);
    storage_write(settings, MUD_DATA);
}

void mudsettingSetDouble(const char *key, double val) {
    store_double(settings, key, val);
    storage_write(settings, MUD_DATA);
}

void mudsettingSetInt(const char *key, int val) {
    store_int(settings, key, val);
    storage_write(settings, MUD_DATA);
}

void mudsettingSetLong(const char *key, long val) {
    store_long(settings, key, val);
    storage_write(settings, MUD_DATA);
}

void mudsettingSetBool(const char *key, bool val) {
    store_bool(settings, key, val);
    storage_write(settings, MUD_DATA);
}

const char *mudsettingGetString(const char *key) {
    return read_string(settings, key);
}

double mudsettingGetDouble(const char *key) {
    return read_double(settings, key);
}

int mudsettingGetInt(const char *key) {
    return read_int(settings, key);
}

long mudsettingGetLong(const char *key) {
    return read_long(settings, key);
}

bool mudsettingGetBool(const char *key) {
    return read_bool(settings, key);
}

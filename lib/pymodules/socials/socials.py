"""
package: socials

socials are commonly used emotes (e.g. smiling, grinning, laughing). Instead
making people have to write out an entire emote every time they would like
to express such an emote, they can simply use one of these simple commands
to perform a pre-made emote. This is essentially a copy of the c module written
in python. There are no changes good or bad.

Description of module concepts:
 cmds are the list of commands that trigger the social. More than one cmd
 can be specified (comma-separated). Assumes cmds != NULL. All other
 arguments can be NULL.

 to_char_notgt is the message sent to the character if no target for
 the social is provided.

 to_room_notgt is the message sent to the room if no target for the
 social is provided.

 to_char_self is the message sent to ourself when the target provided
 was ourself. If to_char_self is not provided, the message will default
 to the same one used for to_char_notgt.

 to_room_self is the message sent to the room when the target provided
 was ourself. If to_room_self is not provided, the message will default
 to the same one used for to_char_notgt.

 to_char_tgt is the message sent to the character when a target is
 provided.

 to_vict_tgt is the message sent to the target when a target is provided

 to_room_tgt is the message sent to the room when a target is provided

 adverbs and adjectives are default modifiers that can be suggested or
 applied to the emote through $M and $m (adjective: evil, adverb: evilly).
 If a player types an override it will override both $M and $m unless they
 clearly specify $M= and/or $m= for advanced usage.

 require_tgt is a boolean describing whether this emote forces the caller
 to have a target.

 min_pos and max_pos are the minimum and maximum positions the socials can
 per performed from, respectively.

"""
from mudsys import add_cmd, remove_cmd
from cmd_checks import chk_conscious, chk_can_move, chk_grounded, chk_supine
import mud, storage, char, auxiliary, time, string, hooks, socedit, mudsys

# This stores all the socials themselves, before unlinking
__social_table__ = { }
# This stores all the socials after unlinking
__socials__ = { }

__socials_file__ = "../lib/misc/socials"

class Social:
    def __init__(self, cmds = "", to_char_notgt = "", to_room_notgt = "", to_char_self = "",
                 to_room_self = "", to_char_tgt = "", to_vict_tgt = "", to_room_tgt = "",
                 adverb = "", adjective = "", require_tgt = "", min_pos = "", max_pos = "",
                 storeSet = None):
        if not storeSet == None:
            self.__cmds__ = storeSet.readString("cmds")
            self.__to_char_notgt__ = storeSet.readString("to_char_notgt")
            self.__to_room_notgt__ = storeSet.readString("to_room_notgt")
            self.__to_char_self__ = storeSet.readString("to_char_self")
            self.__to_room_self__ = storeSet.readString("to_room_self")
            self.__to_char_tgt__ = storeSet.readString("to_char_tgt")
            self.__to_vict_tgt__ = storeSet.readString("to_vict_tgt")
            self.__to_room_tgt__ = storeSet.readString("to_room_tgt")
            self.__adverb__ = storeSet.readString("adverb")
            self.__adjective__ = storeSet.readString("adjective")
            self.__require_tgt__ = storeSet.readString("require_tgt")
            self.__min_pos__ = storeSet.readString("min_pos")
            self.__max_pos__ = storeSet.readString("max_pos")
        else:
            self.__cmds__ = cmds
            self.__to_char_notgt__ = to_char_notgt
            self.__to_room_notgt__ = to_room_notgt
            self.__to_char_self__ = to_char_self
            self.__to_room_self__ = to_room_self
            self.__to_char_tgt__ = to_char_tgt
            self.__to_vict_tgt__ = to_vict_tgt
            self.__to_room_tgt__ = to_room_tgt
            self.__adverb__ = adverb
            self.__adjective__ = adjective
            self.__require_tgt__ = require_tgt
            self.__min_pos__ = min_pos
            self.__max_pos__ = max_pos

    def store(self):
        set = storage.StorageSet()
        set.storeString("cmds",           self.__cmds__)
        set.storeString("to_char_notgt",  self.__to_char_notgt__)
        set.storeString("to_room_notgt",  self.__to_room_notgt__)
        set.storeString("to_char_self",   self.__to_char_self__)
        set.storeString("to_room_self",   self.__to_room_self__)
        set.storeString("to_char_tgt",    self.__to_char_tgt__)
        set.storeString("to_vict_tgt",    self.__to_vict_tgt__)
        set.storeString("to_room_tgt",    self.__to_room_tgt__)
        set.storeString("adjective",      self.__adjective__)
        set.storeString("adverb",         self.__adverb__)
        set.storeString("require_tgt",    self.__require_tgt__)
        set.storeString("min_pos",        self.__min_pos__)
        set.storeString("max_pos",        self.__max_pos__)
        return set

    def get_cmds(self): return self.__cmds__
    def get_to_char_notgt(self): return self.__to_char_notgt__
    def get_to_char_self(self): return self.__to_char_self__
    def get_to_char_tgt(self): return self.__to_char_tgt__
    def get_to_room_notgt(self): return self.__to_room_notgt__
    def get_to_room_self(self): return self.__to_room_self__
    def get_to_room_tgt(self): return self.__to_room_tgt__
    def get_to_vict_tgt(self): return self.__to_vict_tgt__
    def get_adverb(self): return self.__adverb__
    def get_adjective(self): return self.__adjective__
    def get_require_tgt(self): return self.__require_tgt__
    def get_min_pos(self): return self.__min_pos__
    def get_max_pos(self): return self.__max_pos__

    def set_cmds(self, val):
        self.__cmds__ = val
        return self.__cmds__
    def set_to_char_notgt(self, val):
        self.__to_char_notgt__ = val
        return self.__to_char_notgt__
    def set_to_char_self(self, val):
        self.__to_char_self__ = val
        return self.__to_char_self__
    def set_to_char_tgt(self, val):
        self.__to_char_tgt__ = val
        return self.__to_char_tgt__
    def set_to_room_notgt(self, val):
        self.__to_room_notgt__ = val
        return self.__to_room_notgt__
    def set_to_room_self(self, val):
        self.__to_room_self__ = val
        return self.__to_room_self__
    def set_to_room_tgt(self, val):
        self.__to_room_tgt__ = val
        return self.__to_room_tgt__
    def set_to_vict_tgt(self, val):
        self.__to_vict_tgt__ = val
        return self.__to_vict_tgt__
    def set_adverb(self, val):
        self.__adverb__ = val
        return self.__adverb__
    def set_adjective(self, val):
        self.__adjective__ = val
        return self.__adjective__
    def set_require_tgt(self, val):
        self.__require_tgt__ = val
        return self.__require_tgt__
    def set_min_pos(self, val):
        if val in socedit.Position.items():
            self.__min_pos__ = val
        return self.__min_pos__
    def set_max_pos(self, val):
        if val in socedit.Position.items():
            self.__max_pos__ = val
        return self.__max_pos__

def link_social(new_cmd, old_cmd, save=True):
    if old_cmd in __socials__.keys():
        unlink_social(new_cmd, save)
    social_data = get_social(old_cmd)

    cmds = social_data.get_cmds()
    keywords = [x.strip() for x in cmds.split(',')]
    keywords.append(new_cmd)

    # relink all the individual mappings
    new_cmds = ','.join(keywords)
    for k in keywords:
        __socials__[k] = new_cmds

    # set the new hash, delete the old one and add the new
    social_data.set_cmds(new_cmds)
    del __social_table__[cmds]
    __social_table__[new_cmds] = social_data

    # add the command to the system
    add_cmd(new_cmd, None, cmd_social, "player", False)
    # this needs to be rewritten
    if social_data.get_min_pos == "sitting":
        mudsys.add_cmd_check(new_cmd, chk_conscious)
    elif social_data.get_min_pos == "standing":
        mudsys.add_cmd_check(new_cmd, chk_can_move)
    elif social_data.get_max_pos == "standing":
        mudsys.add_cmd_check(new_cmd, chk_grounded)
    elif social_data.get_max_pos == "sitting":
        mudsys.add_cmd_check(new_cmd, chk_supine)


    if save is True:
        save_socials()


def unlink_social(social_cmd, save=True):
    if social_cmd not in __socials__.keys():
        return

    social_link = __socials__[social_cmd]
    if social_link in __social_table__.keys():
        social_data = __social_table__.pop(social_link)

        if social_data is not None:
            cmds = social_data.get_cmds()
            result = [x.strip() for x in cmds.split(',')]
            # remove the original cmd from the command list
            result.remove(social_cmd)
            remove_cmd(social_cmd)
            # if there are still commands left re-add
            if len(result) > 0:
                social_data.set_cmds(','.join(result))
                __social_table__[social_link] = social_data
            else:
                __socials__[social_cmd]

        if save is True:
            save_socials()

def add_social(social_data, save=True):
    cmds = social_data.get_cmds()
    result = [x.strip() for x in cmds.split(',')]
    for res in result:
        unlink_social(res)
        add_cmd(res, None, cmd_social, "player", False)
        if social_data.get_min_pos == "sitting":
            mudsys.add_cmd_check(res, chk_conscious)
        elif social_data.get_min_pos == "standing":
            mudsys.add_cmd_check(res, chk_can_move)
        elif social_data.get_max_pos == "standing":
            mudsys.add_cmd_check(res, chk_grounded)
        elif social_data.get_max_pos == "sitting":
            mudsys.add_cmd_check(res, chk_supine)
        __socials__[res] = cmds
    __social_table__[cmds] = social_data
    if save:
        save_socials()


def get_social(social):
    if social in __socials__:
        return __social_table__[__socials__[social]]
    return None


def save_socials():
    set = storage.StorageSet()
    socials = storage.StorageList()
    set.storeList("socials", socials)

    for cmd, data in __social_table__.iteritems():
        one_set = data.store()
        socials.add(one_set)

    set.write(__socials_file__)
    set.close()
    return


def save_social(social):
    save_socials()
    return

def load_socials():
    storeSet = storage.StorageSet(__socials_file__)
    for social_set in storeSet.readList("socials").sets():
        social_data = Social(storeSet=social_set)
        cmds = social_data.get_cmds()
        result = [x.strip() for x in cmds.split(',')]
        __social_table__[cmds] = social_data
        for res in result:
            add_cmd(res, None, cmd_social, "player", False)
            if social_data.get_min_pos() == "sitting":
                mudsys.add_cmd_check(res, chk_conscious)
            elif social_data.get_min_pos() == "standing":
                mudsys.add_cmd_check(res, chk_can_move)
            elif social_data.get_max_pos() == "standing":
                mudsys.add_cmd_check(res, chk_grounded)
            elif social_data.get_max_pos() == "sitting":
                mudsys.add_cmd_check(res, chk_supine)
            __socials__[res] = cmds
    storeSet.close()
    return

def cmd_socials(ch, cmd, arg):
    '''
    Syntax: socials, socials <social name>

    Socials are a form of emote, they are prepared emotes that are commands you can use and they
    allow for single use, targeting other people, etc. An example of a social would be the grin social.

    If you type:
        > grin

    You will see the following, while others around you will also see a variation as if you had performed
    the action:
        You grin mischievously.

    If you want to grin at Kevin though, you can do so by typing:
        > grin kevin

    You will see:
        You grin mischievously at Kevin.

    Since these are targeted, Kevin will see it directed at them and the room will see you directing
    this mischievous grin at Kevin. Additionally you can change that mischievous nature of the grin
    by typing your own adverb (or even phrase):

        > grin stupidly
        > grin stupidly at kevin

    There are quite a few defined socials that you can do. The command 'socials' will list all of
    the socials currently available to you. Additionally you can specify a social and see how a
    specific social will look if used, the adverbs, and any synonyms.
    '''
    buf = [ ]
    socs = sorted(__socials__.keys())
    count = 0
    for soc in socs:
        count = count + 1
        buf.append("%-20s" % soc)
        if count % 4 == 0:
            ch.send("".join(buf))
            buf = [ ]

    if count % 4 != 0:
        ch.send("".join(buf))


def cmd_soclink(ch, cmd, arg):
    if arg is None or arg is "":
        ch.send("Link which social to which?")
        return

    arg = arg.lower()
    arg, new_soc = mud.parse_args(ch, True, cmd, arg, "| word(subcommand) word(arguments)")
    if new_soc is None:
        ch.send("You must provide a new command and an old social to link it to.")
        return

    social_data = get_social(arg)

    if social_data is None:
        ch.send("No social exists for %s" % arg)

    link_social(new_soc, arg);
    ch.send("%s is now linked to %s" % (new_soc, arg))

def cmd_socunlink(ch, cmd, arg):
    if arg is None or arg is "":
        ch.send("Unlink which social?")
        return

    social_data = get_social(arg)
    if social_data is None:
        ch.send("No social exists for %s." % arg)
        return

    unlink_social(arg)
    ch.send("The %s social was unlinked." % arg)
    mud.log_string("%s unlinked the social %s." % (ch.name, arg))

# One generic command for handling socials. Does table lookup on all of
# the existing socials and executes the proper one.
def cmd_social(ch, cmd, arg):
    data = get_social(cmd)
    # If they used a phrasal or adjective/adverb then this will be 2 length
    # otherwise it will be one length.
    args = arg.split(" at ", 1)
    has_modifier = True if len(args) == 2 else False

    # does the social exist? Do we have a problem? DO WE?
    if data:
        if has_modifier is True:
            tgt, type = mud.generic_find(ch, arg, "all", "immediate", False)
            if tgt is None or type != "char":
                ch.send("That individual does not seem to be here.")
                return
        else:
            tgt, type = mud.generic_find(ch, arg, "all", "immediate", False)

        # No target was supplied, the emote is to ourselves.
        if tgt is None:
            if data.get_to_char_notgt():
                mud.message(ch, None, None, None, True, "to_char", "%s" % (
                            data.get_to_char_notgt() if has_modifier == False
                            else string.replace(data.get_to_char_notgt(), "$M", arg)))
            if data.get_to_room_notgt():
                mud.message(ch, None, None, None, True, "to_room", "%s" % (
                            data.get_to_room_notgt() if has_modifier == False
                            else string.replace(data.get_to_room_notgt(), "$M", arg)))
            return
        # a target was supplied and it is us
        elif ch == tgt:
            if data.get_to_char_self():
                mud.message(ch, None, None, None, True, "to_char",
                            data.get_to_char_self() if has_modifier else
                            string.replace(data.get_to_char_self(), "$M", args[0]))
            elif data.get_to_char_notgt():
                mud.message(ch, None, None, None, True, "to_char",
                        data.get_to_char_notgt() if has_modifier == False
            else string.replace(data.get_to_char_notgt(), "$M", args[0]))
            if data.get_to_room_self():
                mud.message(ch, None, None, None, True, "to_room",
                        data.get_to_room_self() if has_modifier == False
                        else string.replace(data.get_to_room_self(), "$M", args[0]))
            elif data.get_to_room_notgt():
                mud.message(ch, None, None, None, True, "to_room",
                            data.get_to_room_notgt() if has_modifier == False
                            else string.replace(data.get_to_room_notgt(), "$M", args[0]))
            return
        # a target was supplied and it is not us
        else:
            if data.get_to_char_tgt():
                mud.message(ch, tgt, None, None, True, "to_char",
                    data.get_to_char_tgt() if has_modifier == False
                    else string.replace(data.get_to_char_tgt(), "$M", args[0]))
            if data.get_to_vict_tgt():
                mud.message(ch, tgt, None, None, True, "to_char",
                        data.get_to_vict_tgt() if has_modifier == False
                        else string.replace(data.get_to_vict_tgt(), "$M", args[0]))
            if data.get_to_room_tgt():
                mud.message(ch, tgt, None, None, True, "to_room",
                            data.get_to_room_tgt() if has_modifier == False
                            else string.replace(data.get_to_room_tgt(), "$M", args[0]))
    else:
        mud.log_string("ERROR: %s tried social, %s, but no such social exists!" % (ch.name, cmd))
    return
            

load_socials()
add_cmd("socials", None, cmd_socials, "player", False)
add_cmd("socunlink", None, cmd_socunlink, "builder", False)
add_cmd("soclink", None, cmd_soclink, "builder", False)
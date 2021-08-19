"""
 socedit is a set of tools for editing socials online. Socedit requires that
 olc2 be installed.
"""
import olc
from enum import Enum
from socials import add_social, save_social, get_social, Social
from mudsys import cmd_exists, add_cmd

class Socedit(Enum):
    """
    Enumeration class for holding the menu selections for the OLC social
    editor.
    """
    char_notgt = 1
    room_notgt = 2
    char_self = 3
    room_self = 4
    char_tgt = 5
    vict_tgt = 6
    room_tgt = 7
    adverb = 8
    adjective = 9
    require_tgt = 10
    min_pos = 11
    max_pos = 12

class Position(Enum):
    none = -1
    unconscious = 0
    sleeping = 1
    sitting = 2
    standing = 3
    flying = 4

    def getMembers(self):
        return __members__

def socedit_menu(sock, social):
    """
    Creates the menu for the OLC for social editing.

    :param sock: the player socket editing the social
    :param social: the name of the social editing
    :return: None
    """
    sock.send("{y[{c%s{y]\r\n"
              "{g 1) to char notgt: {c%s\r\n"
              "{g 2) to room notgt: {c%s\r\n"
              "{g 3) to char self : {c%s\r\n"
              "{g 4) to room self : {c%s\r\n"
              "{g 5) to char tgt  : {c%s\r\n"
              "{g 6) to vict tgt  : {c%s\r\n"
              "{g 7) to room tgt  : {c%s\r\n"
              "{g 8) default adv  : {c%s\r\n"
              "{g 9) default adj  : {c%s\r\n"
              "{g10) require tgt  : {c%s\r\n"             
              "{g11) minimum pos  : {c%s\r\n"
              "{g12) maximum pos  : {c%s\r\n"
              "\r\n"
              "{gTo assocciate/unassociate commands, use soclink and socunlink"
              % ( social.get_cmds(), social.get_to_char_notgt(), social.get_to_room_notgt(),
                  social.get_to_char_self(), social.get_to_room_self(), social.get_to_char_tgt(),
                  social.get_to_vict_tgt(), social.get_to_room_tgt(), social.get_adverb(),
                  social.get_adjective(), social.get_require_tgt(), social.get_min_pos(),
                  social.get_max_pos()))

def socedit_chooser(sock, social, option):
    if option == '1':
        sock.send(
               "The message to character when no target is supplied : ")
        return Socedit.char_notgt.value
    elif option == '2':
        sock.send(
           "The message to room when no target is supplied : ")
        return Socedit.room_notgt.value
    elif option == '3':
        sock.send(
           "The message to character when target is self : ")
        return Socedit.char_self.value
    elif option == '4':
        sock.send(
           "The message to room when target is self : ")
        return Socedit.room_self.value
    elif option == '5':
        sock.send(
           "The message to character when a target is found : ")
        return Socedit.char_tgt.value
    elif option == '6':
        sock.send(
           "The message to target when a target is found : ")
        return Socedit.vict_tgt.value
    elif option == '7':
        sock.send(
           "The message to room when a target is found : ")
        return Socedit.room_tgt.value
    elif option == '8':
        sock.send(
            "The default adverb for this social (replaces $M): ")
        return Socedit.adverb.value
    elif option == '9':
        sock.send(
            "The default adjective for this social (replaces $m): ")
        return Socedit.adjective.value
    elif option == '10':
        sock.send(
            "Whether this social requires a target when used (1=yes, 2=no): ")
        return Socedit.require_tgt.value
    elif option == '11':
        sock.send("{gValid Positions:")
        for name, member in Position.getMembers().items():
            sock.send("  {c%%2d{y) {g%%-%ds%%s" % member.value, name)
        sock.send("Pick a minimum position: ")
        return Socedit.min_pos.value
    elif option == '12':
        sock.send("{gValid Positions:")
        for name, member in Position.getMembers().items():
            sock.send("  {c%%2d{y) {g%%-%ds%%s" % member.value, name)
        sock.send("Pick a maximum position: ")
        return Socedit.max_pos.value
    else:
        return -1

def socedit_parser(sock, social, choice, arg):
    if int(choice) == 1:
        social.set_to_char_notgt(arg)
        return True
    elif choice == Socedit.room_notgt.value:
        social.set_to_room_notgt(arg)
        return True
    elif choice == Socedit.char_self.value:
        social.set_to_char_self(arg)
        return True
    elif choice == Socedit.room_self.value:
        social.set_to_room_self(arg)
        return True
    elif choice == Socedit.char_tgt.value:
        social.set_to_char_tgt(arg)
        return True
    elif choice == Socedit.vict_tgt.value:
        social.set_to_vict_tgt(arg)
        return True
    elif choice == Socedit.room_tgt.value:
        social.set_to_room_tgt(arg)
        return True
    elif choice == Socedit.adverb.value:
        social.set_adverb(arg)
        return True
    elif choice == Socedit.adjective.value:
        social.set_adjective(arg)
        return True
    elif choice == Socedit.require_tgt.value:
        if arg == "1" or arg == "0":
            social.set_require_tgt(arg)
            return True
        return False
    elif choice == Socedit.min_pos.value:
        try:
            val = int(arg)
        except:
            return False

        x = social.set_min_pos(val)
        if x == val:
            return True
        return False
    elif choice == Socedit.max_pos.value:
        try:
            val = int(arg)
        except:
            return False

        x = social.set_min_pos(val)
        if x == val:
            return True
        return False
    else:
        return False

def cmd_socedit(ch, cmd, arg):
    """
    This starts the social editor olc process, allowing you to edit or create new socials
    for the mud. The minimum permissions required for this is builder.

    syntax: socedit <social name>
    """
    if arg == '' or arg is None:
        ch.send("Which social are you trying to edit?")
        return
    else:
        # strip down to one argument
        arg = arg.split(" ",1)[0]

    # find the social
    social = get_social(arg)

    # make sure we're not trying to edit a command
    if social is None and cmd_exists(arg):
        ch.send("A command already exists with that name!\r\n")
    else:
        if social is None:
            ch.send("Social doesn't exist. Creating new social.")
            social = Social(cmds=arg, to_char_notgt="You emote $M.", to_room_notgt="$n emotes $M.",
                            adverb="smartly", min_pos="sitting", max_pos="flying")
            add_social(social)

    ch.send("%s" % social.get_cmds())
    olc.do_olc(ch.sock, socedit_menu, socedit_chooser, socedit_parser, save_social, social)

add_cmd("socedit", None, cmd_socedit, "player", False)
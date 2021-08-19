"""
cmd_checks.py

General reusable command checks that can be accessed by other
modules to place restrictions on commands.
"""
import movement

def chk_can_manip(ch, cmd):
    """
    Check if a character can manipulate an object based on their
    current position.

    :param ch: character
    :param cmd: command name being performed
    :return: True if possible, False if not
    """
    if not ch.pos in ["sitting", "standing", "flying"]:
        ch.send("You cannot do that while " + ch.pos + ".")
        return False


def chk_conscious(ch, cmd):
    """
    Check if a character is conscious.

    :param ch: character
    :param cmd: command being performed
    :return: True if conscious, False if not
    """
    return chk_pos_ok(ch, "sitting")


def chk_can_move(ch, cmd):
    """
    Check if a character is able to move

    :param ch: character
    :param cmd: command being performed
    :return: True if conscious, False if not
    """
    return chk_pos_ok(ch, "standing")


def chk_grounded(ch, cmd):
    """
    Check if a character is not flying

    :param ch: character
    :param cmd: command being performed
    :return: True if conscious, False if not
    """
    return chk_pos_ok(ch, "standing", True)


def chk_supine(ch, cmd):
    """
    Check if a character is sitting/laying/not erect

    :param ch: character
    :param cmd: command being performed
    :return: True if conscious, False if not
    """
    return chk_pos_ok(ch, "sitting", True)


def chk_pos_ok(ch, chkpos, max_check=False):
    """

    :param ch: character
    :param chkpos: position to analyze
    :param max_check: if False check min_pos, if True chk max_pos
    :return: True if the character meets the condition, False if Not
    """
    pos_index = movement.positions.index(ch.pos)
    chkpos_index = movement.positions.index(chkpos)
    pos = ch.pos
    if pos == chkpos:
        return True

    if max_check is False and pos_index < chkpos_index:
        if pos == "unconscious":
            ch.send("You cannot do that while unconscious!")
        elif pos == "sleeping":
            ch.send("Not while you are sleeping you won't!")
        elif pos == "sitting":
            ch.send("You cannot do that while sitting!")
        elif pos == "standing":
            ch.send("You must be flying to try that out.")
        elif pos == "flying":
            ch.send("That is not possible in any position you can think of.")
        else:
            ch.send("Your position is all wrong!")
            mudsys.log_string("Character %s has invalid position %s" % (ch.name, ch.pos))
        return False
    elif max_check is True and pos_index > chkpos_index:
        if pos == "unconscious":
            ch.send("You are not quite sure how you can achieve this.")
        elif pos == "sleeping":
            ch.send("You must reach a deeper state of consciousness to do that!")
        elif pos == "sitting":
            ch.send("You are too alert to be able to do this!")
        elif pos == "standing":
            ch.send("You need to be closer to the ground to try that.")
        elif pos == "flying":
            ch.send("You cannot do that while you are flying.")
        else:
            ch.send("Your position is all wrong!")
            mudsys.log_string("Character %s has invalid position %s" % (ch.name, ch.pos))
        return False



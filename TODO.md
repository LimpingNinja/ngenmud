# KEVIN'S TO DO LIST - AKA: Wishful Thinking
## THOUGHTS / CONSIDERATIONS
- [x] Move all of the mudlib defines into a config file and create a parser
- [ ] Allow python outside of the PYMOD_LIB directory, allow lazy loading, right
    now the mud crashes as PYMOD_LIB is an autoload directory and subdirectories
    make it barf.
- [ ] Create a master.py which is the first object loaded, this can be used as 
    an initialization driver and override.
- [ ] Create an autoload.py which can be used to autoload any additional python 
    scripts.
- [ ] Python 3 migration: Rough.
- [ ] https://restrictedpython.readthedocs.io/en/latest/index.html
    
## TASK LIST - MUD ENGINE
### HIGH PRIORITY
- [ ] Python accounts aren't dereferencing properly
- [ ] Input handlers, specifically the editors, tend to output information
      twice when in a sub-menu such as the quest stage editor
- [x] Heartbeat Hooks needed 
- [ ] Move send_message parsing for $ expansion to mudlib, why does the engine
      actually care about this? Also it's really painful to use preprocessing
      directives for mudSettings to handle this. (RE: SOMEONE"'s")

### MUDLIB PRIORITY
- [ ] Rewrite the example zone to be a little more interesting and include
      some samples of scripting and object commands.
- [ ] Snoop module
- [ ] Intermud Daemon
- [ ] OLC for mud settings
- [ ] Master and Autoload
- [ ] Domain permissions systems
- [ ] Wizard home directories, frobbing
- [ ] Code based rooms, objects, etc. this is a difficult one. Should they
      be based on prototypes as (essentially) clones?
    
### LOW PRIORITY
- [ ] IP banning module
- [ ] soft-code chat channels
- [ ] spellchecking in the text editor
- [ ] stackable objects
- [ ] mountable characters
- [ ] Rewrite MCCP as its own module

### WONT FIX
- [ ] Script dictionaries aren't fully dereferenced if a script creates a method.
      This is a known memory leak. Figure out how to fix!

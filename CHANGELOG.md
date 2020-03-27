# NGenMud v1.0.0

This is the base release of NGenMud which is a child/derivative of NakedMud. The goal for this is to fix some of the hanging bugs and to make step-wise feature enhancements that follow the progression that NakedMud was taking: Offloading more of the game logic to the lib and keeping the C code for the driver/engine and for modules requiring performance. Changes in this release:

### FIXED:
- The mud was not outputting an IAC,GA after prompts. I modified the socket code to spit this out after busting a prompt. Other editors may not have this, but the GA will fix some lags/delays in popular clients.
- AutoDoc used backspace overprints, 'doc' was illegible, fixed it. Essentially this was causing headers in the doc command and readers to make titles look like 'F FI FIXED XED ED D'; this does not happen now.
  
### MODIFIED:
- Moved most sane options to /lib/muddata including port, paths, messaging,     and formatting options. This required changing the boot order (so that the port is read later for the sockets)
- Changed the SCons slightly (adding libm, essentially) to make sure the mud compiled on current versions of Linux; will test this out cross-platform at a later date.
- [Mudlib] Modified look in rooms to create both a short and long view of the exits.
- Naming consistency (NGenMud) and branding changed throughout
- MOTD and GREETING modified to update and bring in line with naming
  
### ADDED:
- "heartbeat" hook was added with a pulse of once per 2 seconds, this is intended to give scripts an easy timer.
- .gitignore file with sane settings for NGenMud
- Text font for who display (because it looks better while still being generic)
"""
package: socials

socials are commonly used emotes (e.g. smiling, grinning, laughing). Instead
making people have to write out an entire emote every time they would like
to express such an emote, they can simply use one of these simple commands
to perform a pre-made emote.
"""
import os

__all__ = [ ]

# compile a list of all our modules
for fl in os.listdir(__path__[0]):
    if fl.endswith(".py") and not (fl == "__init__.py" or fl.startswith(".")):
        __all__.append(fl[:-3])

# import all of our modules so they can register relevant mud settings and data
for module in __all__:
    exec "import " + module
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Georgie")
define gf = Character("Georgia")
define gm = Character("George")
define c = Character("Charlie")
define a = Character("Aspen")
define w = Character("Wren")
define p = Character("Percy")
define pl = Character("Persephone")
define s = Character("???")
define r = Character("Archie")
define j = Character("Jim")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show georgie happy

    # These display lines of dialogue.

    g "You've created a new Ren'Py game."

    g "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

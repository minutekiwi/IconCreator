# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.screenshot_crop = (210,250,300,300)
init python:
    def getIcon():
        global iconBounds
        iconBounds= renpy.get_image_bounds("iconMask", 300, 300, layer='screens')

    import re
    def file_list(dir=""):
        list = renpy.list_files()
        rv = []
        for f in list:
            if re.match(dir,f):
                rv.append(f[(len(dir)-4):])
        return rv
style summer_fonts_text:
    font "gui/Pacifico.ttf"
    color "#fff"
    outlines [ (absolute(5), "#e3e3e3", absolute(2), absolute(2)),(absolute(3), "#a66f8d", absolute(0), absolute(0)), ]
style summer_fonts_button_text:
    font "gui/Pacifico.ttf"
    hover_color "#fff"
    size 35
    text_align 0.5
    hover_outlines [ (absolute(5), "#e3e3e3", absolute(1), absolute(1)),(absolute(3), "#a66f8d", absolute(0), absolute(0)), ]
    idle_outlines [ (absolute(3), "#a66f8d", absolute(0), absolute(0)), ]
init:
    $ config.keymap['game_menu'].remove('K_ESCAPE')
    $ config.keymap['game_menu'].remove('K_MENU')
    $ config.keymap['game_menu'].remove('mouseup_3')
define config.screenshot_callback = getIcon()
#define config.screenshot_crop =
define config.screenshot_pattern = "SummerIcon%02d.png"
transform def_img_atl:
    zoom 0.5 alpha 0.8 align(0.5,0.5)
    on hover,selected_idle,selected_hover:
        ease 0.2 zoom 0.6 alpha 1.0
    on idle:
        ease 0.1 zoom 0.5 alpha 0.8

define e = Character("Eileen")
default chosen_bg_img = "bg_yellow"
default chosen_fg_img = "melanie"
default choosing_BG = True
screen iconCreator:
    style_prefix "summer_fonts"
    add "gameBg.jpg"
    $ bg_images = file_list("images/bg/")
    $ fg_images = file_list("images/fg/")
    vbox:
        xalign 0.5 ypos 35 xfill True
        spacing -50
        box_wrap False
        text "Studio Élan's":
            size 50 text_align 0.5 xalign 0.5
        text "Summer Icon Creator":
            size 70 text_align 0.5 xalign 0.5
    add Solid("#e3e3e3",xsize=320,ysize=320):
        xpos 0.5
        ypos 245
        yoffset 5
        xoffset 8
        xalign 0.5
    add Solid("#a66f8d",xsize=310,ysize=310):
        xpos 0.5
        ypos 245
        xalign 0.5
    add "iconMask":
        xpos 0.5
        ypos 550
        xanchor 0.5
        yanchor 1.0
    add chosen_bg_img:
        xpos 0.5
        ypos 550
        xanchor 0.5
        yanchor 1.0
    add chosen_fg_img:
        xpos 0.5
        ypos 550
        xanchor 0.5
        yanchor 1.0
    hbox:
        xalign 0.5
        ypos 570
        ysize 100
        textbutton "SAVE" action Screenshot():
            yalign 0.5
    vbox:
        text "BACKGROUND":
            xoffset 20
        yalign 1.0 xalign 0.5
        vpgrid id "backgrounds":
            rows 1
            spacing 5
            xfill True
            ysize 200
            draggable True
            mousewheel "horizontal"
            side_xalign 1.0
            scrollbars "horizontal"
            for i in bg_images:
                fixed:
                    xsize 180 ysize 180
                    imagebutton idle i hover i action SetVariable("chosen_bg_img",i) at def_img_atl
    window:
        xalign 0.5 yalign .725
        ypadding 0 xpadding 0 ysize 420
        vbox:
            text "FOREGROUND":
                xoffset 20
            vpgrid id "foregrounds":
                rows 2
                spacing 5
                xfill True
                draggable True
                mousewheel "horizontal"
                side_xalign 1.0
                scrollbars "horizontal"
                for i in fg_images:
                    fixed:
                        xsize 180 ysize 180
                        imagebutton idle i hover i action SetVariable("chosen_fg_img",i) at def_img_atl


    #do something
# The game starts here.
label before_main_menu:
    call screen iconCreator
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    call screen iconCreator
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

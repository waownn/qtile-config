
#     #####################################################################################
#     ###  ###                       typing import List                           ###   ###
#     #####################################################################################

import os
import subprocess
from typing import Callable, List  # noqa: F401

from libqtile import hook
from libqtile import bar, layout, widget
#from libqtile import qtile

from libqtile.extension.dmenu import DmenuRun
from libqtile.extension.window_list import WindowList
from libqtile.extension.command_set import CommandSet

# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall, MonadWide, MonadThreeCol
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating
from libqtile.command import lazy
# import widgets and bar

from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal
#import susebattery
from colors import gruvbox

#     #####################################################################################
#     ###  ###                           THEME & Bar                            ###   ###
#     #####################################################################################

#from bar1 import bar
from bar11 import screen1_bar, screen2_bar

# from theme import (
#     S_BAR1 as screen1_bar,
#     S_BAR2 as screen2_bar,
#     COLOR as color,
# )
#     #####################################################################################
#     ###  ###                           MY PROGRAMMES                            ###   ###
#     #####################################################################################

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
terminal = "kitty"
# terminal = guess_terminal()
home = os.path.expanduser('~')

#     #####################################################################################
#     ###  ###                              KEYBINDINGS                           ###   ###
#     #####################################################################################

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [
   
# QTILE  KEYS
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "q", lazy.window.kill()),

    # Launch applications
    Key([mod], "w", lazy.spawn('firefox'), desc="Launch browser"),
    Key([mod], "e", lazy.spawn('kitty -e nnn -d -a -S'),
        desc="Launch nnn in home directory"),
    Key([mod], "d", lazy.spawn('rofi -show drun -show-icons'), desc="Launch discord"),
    Key([mod], "s", lazy.spawn('obs'), desc="Launch OBS"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Command prompt
    Key([mod], "p", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # DmenuRun
    Key([mod], 'p', lazy.run_extension(DmenuRun(
        font="TerminessTTF Nerd Font",
        fontsize="13",
        dmenu_command="dmenu_run",
        dmenu_prompt=" ",
        dmenu_height=10,
        dmenu_lines=15,
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        selected_foreground=gruvbox['dark-blue'],
        selected_background=gruvbox['bg'],
    ))),

    Key([mod, "shift"], 'w', lazy.run_extension(WindowList(
        all_groups=True,
        font="TerminessTTF Nerd Font",
        fontsize="13",
        dmenu_prompt=" ",
        dmenu_height=10,
        # dmenu_lines=15,
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        selected_foreground=gruvbox['dark-blue'],
        selected_background=gruvbox['bg'],
    ))),

    Key([mod, "control"], 'n', lazy.run_extension(CommandSet(
        commands={
            'Thesis notes': 'kitty nvim Neorg/Notes/Thesis/index.norg',
            'Dev notes': 'kitty nvim Neorg/Notes/Dev/index.norg',
            'JWL notes': 'kitty nvim Neorg/Notes/JWL/index.norg',
            'YouTube notes': 'kitty nvim Neorg/YT/index.norg',
        },
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        dmenu_prompt=' ',
        dmenu_lines=10,
        dmenu_height=10,
        selected_foreground=gruvbox['blue'],
        selected_background=gruvbox['bg'],
    ))),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

   # # Keybindings for resizing windows in MonadTall layout
   # Key([mod], "i", lazy.layout.grow()),
   # Key([mod], "m", lazy.layout.shrink()),
   # Key([mod], "n", lazy.layout.normalize()),
   # Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),

   # Key([mod, "control"], "Up", lazy.layout.grow()),
   # Key([mod, "control"], "Down", lazy.layout.shrink()),
   # Key([mod, "control"], "Left", lazy.layout.normalize()),
   # Key([mod, "control"], "Right", lazy.layout.maximize()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


   # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "Up", lazy.layout.flip_up()),
    Key([mod, "mod1"], "Down", lazy.layout.flip_down()),
    Key([mod, "mod1"], "Left", lazy.layout.flip_right()),
    Key([mod, "mod1"], "Right", lazy.layout.flip_left()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

  # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod, "control"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    #CHANGE WORKSPACES
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)



#     #####################################################################################
#     ###  ###                        GROUPS ( WORKSPACE )                        ###   ###
#     #####################################################################################


# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#groups = [
#    Group('1', label="一", matches=[ Match(wm_class='firefox'), Match(wm_class='brave'), Match(wm_class='qutebrowser')], layout="columns"),
#    Group('2', label="二", layout="monadtall"),
#    Group('3', label="三", layout="columns"),
#    Group('4', label="四", matches=[ Match(wm_class='discord'), Match(wm_class='zoom'),
#                                   Match(wm_class="teams-for-linux")], layout="stack"),
#    Group('5', label="五", matches=[Match(wm_class="Spotify")], layout="stack"),
#    Group('6', label="六", layout="Bsp"),
#    Group('7', label="七", layout="monadtall"),
#    Group('8', label="八", layout="monadtall"),
#    Group('9', label="九", layout="TreeTab"),
#]

groups = [
    Group("ampersand", label="", layout="bsp"),
    Group("eacute", label="", matches=[ Match(wm_class='firefox'), Match(wm_class='brave-browser'), Match(wm_class='qutebrowser')], layout="monadtall"),
    Group("quotedbl", label="", layout="monadthreecol"),
    Group("apostrophe", label="", matches=[ Match(wm_class='thunar')], layout="ratiotile"),
    Group("parenleft", label="", layout="stack"),
    Group("section", label="", matches=[Match(wm_class="Spotify")], layout="stack"),
    Group("egrave", label="", matches=[ Match(wm_class='discord'), Match(wm_class='zoom'),
                                   Match(wm_class="teams-for-linux")], layout="monadtall"),
    Group("exclam", label="", layout="floating"),
    Group( "ccedilla", label="", layout="treeTab"),
    Group("agrave", label="", layout="spiral"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Key([mod], i.name, lazy.function(go_to_group(i.name))),

        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'kitty', width=0.4, height=0.5, x=0.3, y=0.1, opacity=1),
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('pomo', 'pomotroid', x=0.4, y=0.2, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop',
             width=0.4, height=0.6, x=0.3, y=0.1, opacity=1),
]))
# extend keys list with keybinding for scratchpad
keys.extend([Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),

])

#     #####################################################################################
#     ###  ###                                 LAYOUT                             ###   ###
#     #####################################################################################

layouts = [
    layout.Tile (
        margin=10,
        border_width=3,
        border_focus="#bc7cf7",
        border_normal="#4c566a",
        fair=True),
    layout.TreeTab(
        active_bg = 'ff99cc',
        active_fg = '000000',
        bg_color = '293136',
        font = 'novamono for powerline',
        #font = 'inconsolata for powerline',
        fontsize = 18,
        panel_width = 100,
        inactive_bg = 'a1acff',
        inactive_fg = '000000',
        sections = ['Qtile'],
        section_fontsize = 18,
        section_fg = 'ffffff',
        section_left = 5),
    layout.Bsp (
        margin=10,
        border_width=3,
        border_focus="#bc7cf7",
        border_normal="#4c566a",
        fair=True),
    Stack(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        border_width=2, autosplit=True,
        num_stacks=1,
        margin=8,),
    MonadTall(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        margin=8,
        border_width=2,
        single_border_width=1,
        single_margin=8,),
    MonadThreeCol(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        border_width=2,
        border_normal_stack=gruvbox['dark-gray'],
        border_focus_stack=gruvbox['dark-green'],
        border_on_single=2,
        margin=8,
        align=MonadTall._right,
        margin_on_single=8,),
   layout.Slice(
       border_focus= gruvbox['cyan'],
       border_normal=gruvbox['dark-gray'],
       border_width=2,
       margin=4,),
   layout.Zoomy(
       columnwidth= 200,
       property_big=5,
       property_small=1,
       margin= [10, 15, 10, 15]),
   layout.Matrix(
       columns=3,
       border_focus= gruvbox['cyan'],
       border_normal=gruvbox['dark-gray'],
       border_width=2,
       margin=4 ),
   layout.RatioTile(
       border_focus= gruvbox['cyan'],
       border_normal=gruvbox['dark-gray'],
       border_width=2,
       margin=4,
       ratio= 1.618,
       ratio_increment= 3
       ),
   layout.Spiral(border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        border_width=2,
        border_normal_stack=gruvbox['dark-gray'],
        border_focus_stack=gruvbox['dark-green'],
        border_on_single=2,
        margin=8, ratio=0.4, clockwise=False,
        margin_on_single=8,),
   Floating(
        border_normal=gruvbox['bg0'],
        border_focus=gruvbox['magenta'],
        border_width=2,)
    ]

floating_layout = Floating(
    border_normal=gruvbox['bg0'],
    border_focus=gruvbox['magenta'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        Match(title="Android Emulator - pixel5:5554"),
        Match(wm_class="Genymotion Player"),
        Match(title="AICOMS"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
        Match(wm_class="xarchiver"),
    ])

#     #####################################################################################
#     ###  ###                             DEFINITIONS                            ###   ###
#     #####################################################################################

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=19,
    padding=10,
    foreground=gruvbox['bg'],
)

extension_defaults = widget_defaults.copy()

# screens = [
#     Screen(top=bar)
# ]

screens = [
    Screen(
        # wallpaper_mode="fill",
        top=screen1_bar,
         # wallpaper="~/.config/qtile/wallpapers/nord.png",
        # wallpaper="~/.config/qtile/splash.png",
         # wallpaper="~/.config/qtile/nord.png",
    ),
    Screen(
        # wallpaper_mode="fill",
        top=screen2_bar,
        # wallpaper="/media/shared/Pictures/fav/new/nordic-wallpapers/wild.png",
        # wallpaper="/media/shared/Pictures/fav/new/gruvbox-wallpaper/houses.jpg",
        # wallpaper="/media/shared/Pictures/fav/new/nordic-wallpapers/ign_stuff.png",
        # wallpaper="~/.config/qtile/nord.png",
  ),

]

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
follow_mouse_focus = True

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/sh/autostart.sh')
    subprocess.run([home])


@hook.subscribe.startup_complete
def set_screens():
    home = os.path.expanduser('~/.config/qtile/sh/set-screens.sh')
    subprocess.run([home])

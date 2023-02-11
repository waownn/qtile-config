
from libqtile import bar, widget

from colors import dracula as theme
from functions import (open_audio_devices, open_gnome_system_monitor,
                       open_plasma_systemmonitor, open_power_options,
                       open_xfce4_power_manager_settings, toggle_redshift)

from unicodes import right_arrow, left_arrow
from colors import gruvbox

screen1_bar = bar.Bar(
    [
    widget.Wallpaper(
            background=gruvbox['fg0'],
            foreground=gruvbox['fg9'],
            fontshadow=gruvbox['bg'],
            label="",
            fontsize=18,
            directory="~/.config/qtile/wallpapers",
        ),

    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['fg0'],
            foreground = gruvbox['bg']),

    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg'],
        margin_x = 5),

    widget.Prompt(),
    #right_arrow(gruvbox['fg0'], gruvbox['bg']),
    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['bg'],
            foreground = gruvbox['fg0']),

    widget.CurrentLayout(
           scale = 0.7,
        background=gruvbox['fg0'],
        foreground=gruvbox['fg9']),

    #right_arrow(gruvbox['bg'], gruvbox['fg9']),
    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['fg0'],
            foreground = gruvbox['fg1']),

    widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['fg1'],
        foreground=gruvbox['fg9'],
        show_zero=True,),

    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['fg1'],
            foreground = gruvbox['bg']
            ),

    #right_arrow(gruvbox['bg'], gruvbox['bg0']),
    widget.WindowName( background = gruvbox['bg'],
               foreground=gruvbox['fg9']
               ),


   #left_arrow(gruvbox['bg0'], gruvbox['fg0']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['bg'],
           foreground = gruvbox['fg0']),

    widget.ThermalSensor(
        format=' {temp}°C',
        #zone = '/sys/devices/platform/coretemp.0/hwmon/hwmon*/temp1_input',
        background=gruvbox['fg0'],
       foreground=gruvbox['dark-green']
    ),
   # left_arrow(gruvbox['fg0'], gruvbox['fg1']),
    widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg0'],
           foreground = gruvbox['fg1']),

    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green']
    ),

   #left_arrow(gruvbox['fg1'], gruvbox['fg2']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg1'],
           foreground = gruvbox['fg2']),

    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg2'],
        foreground=gruvbox['yellow']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg2'],
           foreground = gruvbox['fg3']),

    #left_arrow(gruvbox['fg3'], gruvbox['dark-blue']),
    widget.Net(
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-blue']),

  # left_arrow(gruvbox['fg3'], gruvbox['bg0']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg3'],
           foreground = gruvbox['bg0']),

    widget.Clock(
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-magenta'],
        format=' %Y-%m-%d %a %I:%M %p'),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['bg0'],
           foreground = gruvbox['fg0']),

    #left_arrow(gruvbox['fg0'], gruvbox['bg']),
    widget.Systray(
        background=gruvbox['fg0']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg0'],
           foreground = gruvbox['bg']),

    widget.Spacer(length=20, background=gruvbox['fg0'])
], background=gruvbox['bg'], size=30, margin=4)


screen2_bar = bar.Bar(
    [
    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg'],
        margin_x = 5),

    widget.Prompt(),
    #right_arrow(gruvbox['fg0'], gruvbox['bg']),
    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['bg'],
            foreground = gruvbox['fg0']),

    widget.CurrentLayout(
           scale = 0.7,
        background=gruvbox['fg0'],
        foreground=gruvbox['fg9']),

    #right_arrow(gruvbox['bg'], gruvbox['fg9']),
    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['fg0'],
            foreground = gruvbox['fg1']),

    widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['fg1'],
        foreground=gruvbox['fg9'],
        show_zero=True,),

    widget.TextBox(text='\u25e2',
            padding=0, fontsize=50,
            background = gruvbox['fg1'],
            foreground = gruvbox['bg']
            ),

    #right_arrow(gruvbox['bg'], gruvbox['bg0']),
    widget.WindowName( background = gruvbox['bg'],
               foreground=gruvbox['fg9']
               ),


   #left_arrow(gruvbox['bg0'], gruvbox['fg0']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['bg'],
           foreground = gruvbox['fg0']),

    widget.ThermalZone(
        format=' {temp}°C',
        #zone = '/sys/devices/platform/coretemp.0/hwmon/hwmon*/temp1_input',
        background=gruvbox['fg0'],
       foreground=gruvbox['dark-green']
    ),
   # left_arrow(gruvbox['fg0'], gruvbox['fg1']),
    widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg0'],
           foreground = gruvbox['fg1']),

    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green']
    ),

   #left_arrow(gruvbox['fg1'], gruvbox['fg2']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg1'],
           foreground = gruvbox['fg2']),

    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg2'],
        foreground=gruvbox['yellow']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg2'],
           foreground = gruvbox['fg3']),

    #left_arrow(gruvbox['fg3'], gruvbox['dark-blue']),
    widget.Net(
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-blue']),

  # left_arrow(gruvbox['fg3'], gruvbox['bg0']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg3'],
           foreground = gruvbox['bg0']),

    widget.Clock(
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-magenta'],
        format=' %Y-%m-%d %a %I:%M %p'),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['bg0'],
           foreground = gruvbox['fg0']),

    #left_arrow(gruvbox['fg0'], gruvbox['bg']),
    widget.Systray(
        background=gruvbox['fg0']),
   widget.TextBox(text='\u25e2',
           padding=0, fontsize=50,
           background = gruvbox['fg0'],
           foreground = gruvbox['bg']),

    widget.Spacer(length=20, background=gruvbox['fg0'])
], background=gruvbox['bg'], size=30, margin=4)

def configure_dpi(self):
        ...
        self.root.set_property("RESOURCE_MANAGER", "Xft.dpi: %d\n" % float(dpi),
                               type="STRING", format=8,
                               mode=xcffib.xproto.PropMode.Append)
        pangocffi.set_default_dpi(dpi)

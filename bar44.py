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
            foreground=gruvbox['dark-magenta'],
            fontshadow=gruvbox['bg'],
            label="",
            fontsize=18,
            directory="~/.config/qtile/wallpapers",
        ),
    right_arrow(gruvbox['bg'], gruvbox['fg0']),

    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0, fontsize=24,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_arrow(gruvbox['fg0'], gruvbox['bg']),
    widget.CurrentLayout(
        background=gruvbox['fg0'],
        foreground=gruvbox['dark-blue']
    ),
    right_arrow(gruvbox['bg0'], gruvbox['fg0']),

    widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-yellow'],
        show_zero=True,
    ),

   right_arrow(gruvbox['bg'], gruvbox['bg0']),
    widget.TaskList(foreground=gruvbox['fg'],
        background=gruvbox['bg'],
        border=None, margin=3,
       icon_size=20, padding=3, 
        spacing = 7),

   # right_arrow(gruvbox['bg'], gruvbox['bg0']),
   # widget.WindowName(foreground=gruvbox['fg']),
left_arrow(gruvbox['bg'], gruvbox['fg1']),
    widget.Wttr(
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-blue'],
        location={'Hasselt':'Htl'},
        format='%l: %c %t(%f),%w'),

    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
    widget.ThermalSensor(
        #format= ' temp: {temp} °C',
        format='  {tag}: {temp:.0f}{unit} ',
        #format_crit= '{temp}°C CRIT!',
        background=gruvbox['fg2'],
       foreground=gruvbox['dark-green'],
           fgcolor_high= '#ffaa00',
           fgcolor_normal= gruvbox['fg9'],
           metric = True,
			high = 45,
			padding = 3,
			),

    left_arrow(gruvbox['fg2'], gruvbox['fg3']),
    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-yellow']
    ),

    left_arrow(gruvbox['fg3'], gruvbox['fg4']),
    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg4'],
        foreground=gruvbox['green']
    ),

    left_arrow(gruvbox['fg4'], gruvbox['fg7']),
    widget.Net(
        format = '  {down} ↓↑ {up}',
        background=gruvbox['fg7'],
        foreground=gruvbox['dark-blue']
    ),
    left_arrow(gruvbox['fg7'], gruvbox['fg5']),
    widget.PulseVolume(
        background=gruvbox['fg5'],
        foreground=gruvbox['dark-gray'],
        fmt=' Vol: {}  ',
    ),

    left_arrow(gruvbox['fg5'], gruvbox['fg']),
    widget.Clock(
        background=gruvbox['fg'],
        foreground=gruvbox['fg1'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(gruvbox['fg'], gruvbox['fg8']),
    widget.Systray(
        background=gruvbox['fg8']
    ),

    widget.Spacer(length=25, background=gruvbox['fg8'])],
    background=gruvbox['bg'], 
    size=32, margin= [4, 10, 0, 10])


screen2_bar = bar.Bar(
    [
    right_arrow(gruvbox['bg0'], gruvbox['fg0']),

    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_arrow(gruvbox['fg0'], gruvbox['bg']),
    widget.CurrentLayout(
        background=gruvbox['fg0'],
        foreground=gruvbox['fg9']
    ),
    right_arrow(gruvbox['bg0'], gruvbox['fg0']),

    widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['bg0'],
        foreground=gruvbox['fg9'],
        show_zero=True,
    ),

   right_arrow(gruvbox['bg0'], gruvbox['bg']),
    widget.TaskList(foreground=gruvbox['fg'],
             border=None, margin= -6,
            icon_size=8, imargin_x=-6, spacing = 4),

   # right_arrow(gruvbox['bg'], gruvbox['bg0']),
   # widget.WindowName(foreground=gruvbox['fg']),

    left_arrow(gruvbox['bg'], gruvbox['fg6']),
    widget.ThermalZone(
        format= ' temp: {temp} °C',
        #format_crit= '{temp}°C CRIT!',
        background=gruvbox['fg6'],
       foreground=gruvbox['dark-green'],
           fgcolor_high= '#ffaa00',
           fgcolor_normal= gruvbox['fg9'],
           #zone= '/sys/devices/platform/coretemp.0/hwmon/hwmon3/temp1_input',
           metric = True,
			high = 45,
			padding = 3,
			),

    left_arrow(gruvbox['fg6'], gruvbox['bg0']),
    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-yellow']
    ),

    left_arrow(gruvbox['bg0'], gruvbox['fg1']),
    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg1'],
        foreground=gruvbox['green']
    ),

    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
    widget.Net(
        format = '  {down} ↓↑ {up}',
        background=gruvbox['fg2'],
        foreground=gruvbox['dark-blue']
    ),
    left_arrow(gruvbox['fg2'], gruvbox['fg3']),
    widget.PulseVolume(
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-magenta'],
        format="Vol: {percent:2.0%}   ",
    ),

    left_arrow(gruvbox['fg3'], gruvbox['fg4']),
    widget.Clock(
        background=gruvbox['fg4'],
        foreground=gruvbox['dark-green'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(gruvbox['fg4'], gruvbox['fg5']),
    widget.Systray(
        background=gruvbox['fg5']
    ),

    widget.Spacer(length=25, background=gruvbox['fg5'])],
    background=gruvbox['bg'],
    size=32, margin= [4, 10, 0, 10])


def configure_dpi(self):
        ...
        self.root.set_property("RESOURCE_MANAGER", "Xft.dpi: 192\n" % float(dpi),
                               type="STRING", format=8,
                               mode=xcffib.xproto.PropMode.Append)
        pangocffi.set_default_dpi(dpi)

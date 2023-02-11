
from unicodes import left_half_circle, right_half_circle
from libqtile import bar, widget

from colors import dracula as theme
from functions import (open_audio_devices, open_gnome_system_monitor,
                       open_plasma_systemmonitor, open_power_options,
                       open_xfce4_power_manager_settings, toggle_redshift)

from unicodes import right_arrow, left_arrow
from colors import gruvbox

screen1_bar = bar.Bar(
    [
    left_half_circle(gruvbox['dark-magenta']),
    widget.Wallpaper(label="",
            fontsize=18,
            directory="~/.config/qtile/wallpapers",
            background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    left_half_circle(gruvbox['yellow']),
    widget.CurrentLayout(
        background=gruvbox['yellow'],
    ),
    right_half_circle(gruvbox['yellow']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
   widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['dark-blue'],
        show_zero=True
    ),
    right_half_circle(gruvbox['dark-blue']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['cyan']),
    widget.Clock(
        background=gruvbox['cyan'],
        format=' %Y-%m-%d %a %I:%M %p'),
    right_half_circle(gruvbox['cyan']),

    widget.Spacer(length=10),

    # Prompt(foreground=gruvbox['fg']),

    widget.WindowName(foreground=gruvbox['fg']),

    widget.Spacer(length=100),

    left_half_circle(gruvbox['bg']),
    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_half_circle(gruvbox['bg']),

    widget.Spacer(length=100),

    widget.Systray(
        padding=15,
        # background='#00000000'
    ),

    widget.Spacer(length=10),
    left_half_circle(gruvbox['fg3']),
    widget.ThermalZone(
        format= '  {temp} °C',
        format_crit= '{temp}°C CRIT!',
        background=gruvbox['fg3'],
       foreground=gruvbox['dark-green'],
           fgcolor_high= 'ffaa00',
           zone= '/sys/devices/platform/coretemp.0/hwmon/hwmon3/temp1_input',
           metric = True,
			high = 45,
			padding = 3,
        #background=gruvbox['yellow'],
    ),
    right_half_circle(gruvbox['fg3']),

    left_half_circle(gruvbox['dark-cyan']),
    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-cyan']),
    right_half_circle(gruvbox['dark-cyan']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['dark-magenta']),
    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    widget.Net(
        format = '  {down} ↓↑ {up}',
        background=gruvbox['dark-blue']
    ),
    right_half_circle(gruvbox['dark-blue'])
],
    margin=[8, 8, -1, 8],
    background='#00000000',
    opacity=1,
    size=32,
)

screen2_bar = bar.Bar(
    [
    left_half_circle(gruvbox['dark-magenta']),
    widget.Wallpaper(label="",
            fontsize=18,
            directory="~/.config/qtile/wallpapers",
            background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    left_half_circle(gruvbox['yellow']),
    widget.CurrentLayout(
        background=gruvbox['yellow'],
    ),
    right_half_circle(gruvbox['yellow']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
   widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['dark-blue'],
        show_zero=True
    ),
    right_half_circle(gruvbox['dark-blue']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['cyan']),
    widget.Clock(
        background=gruvbox['cyan'],
        format=' %Y-%m-%d %a %I:%M %p'),
    right_half_circle(gruvbox['cyan']),

    widget.Spacer(length=10),

    # Prompt(foreground=gruvbox['fg']),

    widget.WindowName(foreground=gruvbox['fg']),

    widget.Spacer(length=100),

    left_half_circle(gruvbox['bg']),
    widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_half_circle(gruvbox['bg']),

    widget.Spacer(length=100),

    widget.Systray(
        padding=15,
        # background='#00000000'
    ),

    widget.Spacer(length=10),
    left_half_circle(gruvbox['fg3']),
    widget.ThermalZone(
        format= '  {temp} °C',
        format_crit= '{temp}°C CRIT!',
        background=gruvbox['fg3'],
       foreground=gruvbox['dark-green'],
           fgcolor_high= 'ffaa00',
           zone= '/sys/devices/platform/coretemp.0/hwmon/hwmon3/temp1_input',
           metric = True,
			high = 45,
			padding = 3,
        #background=gruvbox['yellow'],
    ),
    right_half_circle(gruvbox['fg3']),

    left_half_circle(gruvbox['dark-cyan']),
    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-cyan']),
    right_half_circle(gruvbox['dark-cyan']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['dark-magenta']),
    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    widget.Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    widget.Net(
        format = '  {down} ↓↑ {up}',
        background=gruvbox['dark-blue']
    ),
    right_half_circle(gruvbox['dark-blue'])
],
    margin=[8, 8, -1, 8],
    background='#00000000',
    opacity=1,
    size=32,
)

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

    right_arrow(gruvbox['bg0'], gruvbox['fg0']),

     widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0, fontsize = 26,
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

   right_arrow(gruvbox['bg'], gruvbox['bg0']),
     widget.TaskList(foreground=gruvbox['fg'],
             border=None, margin= -6,
            icon_size=8, imargin_x=-6, spacing = 4),

   # right_arrow(gruvbox['bg'], gruvbox['bg0']),
   # WindowName(foreground=gruvbox['fg']),

    left_arrow(gruvbox['bg'], gruvbox['fg3']),
     widget.ThermalSensor(
        #format= '  {temp} °C',
        format='  {tag}: {temp:.0f}{unit} ',
        #format_crit= '{temp}°C CRIT!',
        background=gruvbox['fg3'],
       foreground=gruvbox['dark-green'],
           fgcolor_high= 'ffaa00',
          # zone= '/sys/devices/platform/coretemp.0/hwmon/hwmon3/temp1_input',
           metric = True,
			high = 45,
			padding = 3,
			),

    left_arrow(gruvbox['fg3'], gruvbox['fg1']),
     widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green']
    ),

    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
     widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg2'],
        foreground=gruvbox['yellow']
    ),

    left_arrow(gruvbox['fg2'], gruvbox['fg3']),
    widget.Net(
        format = '  {down} ↓↑ {up}',
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-blue']
    ),
    left_arrow(gruvbox['fg3'], gruvbox['fg1']),
     widget.Volume(
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green'],
        fmt=' Vol: {}   ',
        #emoji=True, 
        font="Font Awesome 18 Free Solid",
    ),


widget.Backlight(
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green'],
            backlight_name="intel_backlight",
            # brightness_file="/sys/class/backlight/intel_backlight",
            # max_brightness_file="/sys/class/backlight/intel_backlight",
            # foreground=theme['dark-magenta'],
            fontshadow=gruvbox['bg'],
            format="Bl: {percent:2.0%}  ",
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            mouse_callbacks={'Button1': toggle_redshift, },
        ),
    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
    widget.Wttr(
        background=gruvbox['fg2'],
        foreground=gruvbox['dark-blue'],
        location={'Hasselt':'Hlt'},
        format='%l:%c%t(%f), %w\n'),

    left_arrow(gruvbox['fg2'], gruvbox['bg0']),
     widget.Clock(
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-magenta'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(gruvbox['bg0'], gruvbox['fg0']),
     widget.Systray(
        background=gruvbox['fg0']
    ),

     widget.Spacer(length=25, background=gruvbox['fg0'])],
    background=gruvbox['bg'], 
    size=32, margin= [4, 10, 0, 10])


screen2_bar = bar.Bar(
    [
     widget.GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0, fontsize = 26,
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

   right_arrow(gruvbox['bg'], gruvbox['bg0']),
     widget.TaskList(foreground=gruvbox['fg'],
             border=None, margin= -6,
            icon_size=8, imargin_x=-6, spacing = 4),

   # right_arrow(gruvbox['bg'], gruvbox['bg0']),
   # WindowName(foreground=gruvbox['fg']),

    left_arrow(gruvbox['bg'], gruvbox['fg3']),
     widget.ThermalZone(
        format= '  {temp} °C',
        #format_crit= '{temp}°C CRIT!',
        background=gruvbox['fg3'],
       foreground=gruvbox['dark-green'],
           fgcolor_high= 'ffaa00',
           zone= '/sys/devices/platform/coretemp.0/hwmon/hwmon3/temp1_input',
           metric = True,
            high = 45,
            padding = 3,
            ),

    left_arrow(gruvbox['fg3'], gruvbox['fg1']),
     widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green']
    ),

    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
     widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg2'],
        foreground=gruvbox['yellow']
    ),

    left_arrow(gruvbox['fg2'], gruvbox['fg3']),
    widget.Net(
        format = '  {down} ↓↑ {up}',
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-blue']
    ),
    left_arrow(gruvbox['fg3'], gruvbox['fg1']),
     widget.PulseVolume(
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green'],
        fmt=' Vol: {}  ',
        #emoji=True, 
        font="Font Awesome 18 Free Solid",
    ),

    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
    widget.OpenWeather(
        background=gruvbox['fg2'],
        foreground=gruvbox['dark-blue'],
        location='Hasselt',
        format='{location_city}:{icon}{main_temp} °{units_temperature} {wind_speed} {wind_direction}'),

    left_arrow(gruvbox['fg2'], gruvbox['bg0']),
     widget.Clock(
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-magenta'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(gruvbox['bg0'], gruvbox['fg0']),
     widget.Systray(
        background=gruvbox['fg0']
    ),

     widget.Spacer(length=25, background=gruvbox['fg0'])],
    background=gruvbox['bg'], 
    size=32, margin= [4, 10, 0, 10])

def configure_dpi(self):
        ...
        self.root.set_property("RESOURCE_MANAGER", "Xft.dpi: 192\n" % float(dpi),
                               type="STRING", format=8,
                               mode=xcffib.xproto.PropMode.Append)
        pangocffi.set_default_dpi(dpi)

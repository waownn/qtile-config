from libqtile import bar, widget
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget import modify
from libqtile.lazy import lazy
#from b_theme import Theme, MeasurementsConfig
from qtile_b_widgets import AppName, VisualizerBars


from colors import dracula as theme
from functions import (open_audio_devices, open_gnome_system_monitor,
                       open_plasma_systemmonitor, open_power_options,
                       open_xfce4_power_manager_settings, toggle_redshift)

from unicodes import right_arrow, left_arrow
from colors import gruvbox

screen1_bar = bar.Bar(
    [
            widget.Image(
                label="",
                background='#21222c',
                margin_x=4,
                margin_y=2,
                scale=True,
                mouse_callbacks={'Button1': lazy.spawn("rofi -show drun"), },
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.GroupBox(
                font="Font Awesome 18 Free Solid",
                fontsize=22,
                highlight_method='block',
                foreground='#f8f8f2',
                background='#282a36',
                active='#bd93f9',
                inactive='#5a5958',
                block_highlight_text_color='#282a36',
                this_current_screen_border='#ff79c6',
                this_screen_border='#ff79c6',
                other_current_screen_border='#50fa7b',
                other_screen_border='#50fa7b',
                urgent_border='#282a36',
                borderwidth=3,
                padding=4,
                rounded=True,
                disable_drag=True,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.CurrentLayoutIcon(
                foregoround='#ff79c6',
                background='#282a36',
                padding=4,
                scale=0.7,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=4,
            ),

            widget.TextBox(
                text=" ",
                font="Font Awesome 18 Free Solid",
                fontsize=28,
                foreground='#282a36',
                background='#f1fa8c',
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.CheckUpdates(
                fmt=' {} ',
                distro='openSUSE',
                display_format='Updates: {updates} ',
                no_update_string='System upto date ',
                colour_have_updates='#282a36',
                colour_no_updates='#282a36',
                background='#f1fa8c',
                font="Font Awesome 18 Free Solid",
                fontsize=18,
                update_interval=1200,  # in seconds
                padding=0,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.TextBox(
                text='',
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#8be9fd',
                background='#f1fa8c',
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.TextBox(
                text='',
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#bd93f9',
                background='#8be9fd',
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.TextBox(
                text='',
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#ff79c6',
                background='#bd93f9',
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),


            VisualizerBars(fontsize=18,
                foreground='#282a36',
                background='#ff79c6',
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.TextBox(
                text='',
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#ff5555',
                background='#ff79c6',
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.TextBox(
                text=" ",
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#282a36',
                background='#ff5555',
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            modify(
                AppName,
                default_name='',
                foreground='#282a36',
                background='#ff5555',
                font="Font Awesome 18 Free Solid",
                fontsize=18,
                fmt=' {}  ',
                format='{name}',
                padding=0,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
            ),

            widget.NetGraph(
                background='#282a36',
                graph_color='#bd93f9',
                fill_color='#282a36',
                border_color='#282a36',
                type='line',
                line_width=1,
                border_width=3,
                samples=40,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Net(fontsize=18,
                format='{down} ↓↑ {up} ',
                foreground='#f8f8f2',
                background='#282a36',
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=4,
            ),
widget.TextBox(
                text=' ',
                font="Font Awesome 18 Free Solid",
                fontsize=22,
                foreground='#ffb86c',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

    widget.ThermalSensor(        
        fontsize=18,
        format='CPU: {temp:.0f}{unit} ',
        metric = True,
        high = 45,
        padding = 3,
        background='#21222c',
        foreground='#ffb86c',
        margin_x=4,
        margin_y=4,
        scale=True,
        decorations=[
         RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,)],
                          ),

      widget.Spacer(
                background="#000000.00",
                length=4,
            ),
            widget.TextBox(
                text=' ',
                font="Font Awesome 18 Free Solid",
                fontsize=22,
                foreground='#ffb86c',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Backlight(fontsize=18,
                backlight_name='intel_backlight',
                format='{percent:3.0%} ',
                foreground='#f8f8f2',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=4,
            ),

            widget.TextBox(
                text=' ',
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#ff79c6',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Battery(fontsize=18,
                format='{percent:3.0%} ',
                show_short_text=False,
                foreground='#f8f8f2',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=4,
            ),

            widget.TextBox(
                text=' ',
                font="Font Awesome 18 Free Solid",
                fontsize=25,
                foreground='#50fa7b',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Memory(fontsize=18,
                format='{MemUsed: .0f}{mm} ',
                foreground='#f8f8f2',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=4,
            ),

            widget.TextBox(
                text=" ",
                font="Font Awesome 18 Free Solid",
                fontsize=22,
                foreground='#ff5555',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.PulseVolume(fontsize=18,
                fmt='{} ',
                foreground='#f8f8f2',
                background='#282a36',
                padding=4,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=4,
            ),

            widget.Clock(fontsize=18,
                format='   %d.%m.%Y |   %H:%M:%S ',
                foreground='#282a36', 
                background='#f1fa8c',
                padding=4,
                decorations=[
                    RectDecoration(
                        use_widget_background=True,
                        radius=10,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),
        ],
        32, fontsize=18,
        margin=[4, 4, 2, 4],
        background="#000000.00",
    )


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

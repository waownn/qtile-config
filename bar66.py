from libqtile import bar, widget

from colors import gruvbox as theme
from functions import (open_audio_devices, open_gnome_system_monitor,
                       open_plasma_systemmonitor, open_power_options,
                       open_xfce4_power_manager_settings, toggle_redshift)


screen1_bar = bar.Bar(
    [
        widget.Spacer(length=7),

        # --------------
        #   Shutdown
        # --------------
         widget.TextBox(
             background=theme['bg'],
        #    foreground=theme['orange'],
             text='Exit',
             # padding=10,
             # font="Font Awesome 5 Free Solid",
             mouse_callbacks={'Button1': open_power_options, },
         ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            text='',
            # padding=10,
            fontshadow=theme['bg'],
           # font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_power_options, },
        ),
        widget.Spacer(length=7),

        # --------------
        # Background programs
        # --------------
        widget.Systray(
            background=theme['bg'],
            fontshadow=theme['fg'],
            foreground=theme['dark-yellow'],
            padding=10
        ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['workspaceColor'],
            fontshadow=theme['fg'],
            text='',
            padding=7,
            # font="Font Awesome 5 Free Solid",
            fontsize=20,
            # mouse_callbacks={'Button1': open_power_options, },
        ),
        widget.Spacer(length=7),

        # ----------
        #   the battery
        # ----------
        widget.Battery(
            background=theme['bg'],
            foreground=theme['cyan'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%}",
            fontshadow=theme['fg'],
            charge_char="",
            empty_char="",
            full_char="",
            font="Font Awesome 5 Free Solid",
            notify_below=25,
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
        ),
        widget.BatteryIcon(
            background=theme['bg'],
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
            # scale=1,
            # color_path="/home/waleed/.config/qtile/battery-icons"
            # foreground=theme['dark-magenta'],
            # format="{watt:.2f} W - {percent:2.0%} ",
        ),
        widget.Spacer(length=7),

        # ----------
        # brightness
        # ----------
        widget.Backlight(
            background=theme['bg'],
            foreground=theme['yellow'],
            backlight_name="intel_backlight",
            # brightness_file="/sys/class/backlight/intel_backlight",
            # max_brightness_file="/sys/class/backlight/intel_backlight",
            # foreground=theme['dark-magenta'],
            fontshadow=theme['bg'],
            format="{percent:2.0%}  ",
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            mouse_callbacks={'Button1': toggle_redshift, },
        ),
        widget.Spacer(length=7),

        # ---------------
        # volume level
        # ---------------
        widget.Volume(
            background=theme['bg'],
            foreground=theme['blue'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%} ",
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            fontshadow=theme['fg'],
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['blue'],
            text='',
            padding=5,
            fontsize=12,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.Spacer(length=7),

        # --------
        # NET
        # --------
        widget.Net(
            background=theme['bg'],
            foreground=theme['magenta'],
            fontshadow=theme['fg'],
            format='{up}  {down}   ',
            font="Font Awesome 5 Free Solid",
            fontsize=18,
        ),
        widget.Spacer(length=7),

        # --------
        #   Wallpaper
        # --------
        widget.Wallpaper(
            background=theme['bg'],
            foreground=theme['fg9'],
            fontshadow=theme['fg'],
            label="",
            fontsize=18,
            directory="~/.config/qtile/wallpapers",
        ),
        widget.Spacer(length=7),

        # ------------------------------------------------
        # -------- Beginning of the middle ---------------
        # ------------------------------------------------
        widget.Spacer(),
        # ----------
        #   Clock
        # ----------
        widget.Clock(
            background=theme['bg'],
            foreground=theme['yellow'],
            format="(%I:%M) - %A, %d %B  ",
            fontshadow=theme['fg'],
            fontsize=18,
        ),
        # widget.TextBox(
        #     background=theme['bg'],
        #     foreground=theme['workspaceColor'],
        #     text='',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     margin=2
        # ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ middle end ------------------
        # ------------------------------------------------

        # -------------
        #   Thermal Sensor CPU
        # -------------
        widget.ThermalSensor(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            fontshadow=theme['fg'],
        ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            fontshadow=theme['fg'],
            text='',
            padding=5,
            fontsize=16,
            font="Font Awesome 5 Free Solid",
        ),
        widget.Spacer(length=7),


        # --------
        #   Memory
        # --------
        widget.Memory(
            background=theme['bg'],
            foreground=theme['dark-green'],
            format="{MemPercent: .0f} %  ",
            fontshadow=theme['fg'],
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            # plasma-systemmonitor
            mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        ),
        # widget.TextBox(
        #     text='',
        #     background=theme['dark-blue'],
        #     foreground=theme['widget-fg'],
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        #     margin=2
        # ),
        widget.Spacer(length=7),

        # ----------
        #   processor CPU
        # ----------
        widget.CPUGraph(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            fill_color=theme['dark-yellow'],
            graph_color=theme['magenta'],
            # format='{load_percent}%',
            font="Font Awesome 5 Free Solid",
            border_width=0,
            line_width=0,
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        # widget.TextBox(
        #     background=theme['dark-yellow'],
        #     foreground=theme['widget'],
        #     text=' ',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_gnome_system_monitor, },
        # ),
        widget.Spacer(length=7),

        widget.GroupBox(
            background=theme['bg'],
            foreground=theme["fg1"],
            active=theme["foregroundColor"],
            inactive=theme["workspaceColor"],

            # Text color of the selected page
            block_highlight_text_color=theme['cyan'],
            # Selected color
            highlight_color=theme['fg6'],
            fontsize=20,
            highlight_method='line',
            disable_drag=True,
            borderwidth=2,
            padding=4,
        ),

        widget.Spacer(length=7),

        widget.WindowCount(
            background=theme['bg'],
            foreground=theme['backgroundColor'],
            show_zero=True,
            fontsize=18,
        ),
        widget.CurrentLayoutIcon(
            background=theme["bg"],
            foreground=theme['backgroundColor'],
            scale=0.65,
            padding=3,
        ),

        widget.Spacer(length=7),

    ],
    background=theme['fg7'],
    size=32,
    fontsize=16, margin= [4, 10, 0, 10],
    border_width=[4, 0, 4, 0],  # Draw top and bottom borders
    border_color=[
        theme["fg7"],
        theme["fg7"],
        theme["fg7"],
        theme["fg7"]
    ]  # Borders are magenta
)

screen2_bar = bar.Bar(
    [
        widget.Spacer(length=7),

        # --------------
        #   Shutdown
        # --------------
         widget.TextBox(
             background=theme['bg'],
        #    foreground=theme['orange'],
             text='Exit',
             # padding=10,
             # font="Font Awesome 5 Free Solid",
             mouse_callbacks={'Button1': open_power_options, },
         ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            text='',
            # padding=10,
            fontshadow=theme['bg'],
           # font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_power_options, },
        ),
        widget.Spacer(length=7),

        # --------------
        # Background programs
        # --------------
        widget.Systray(
            background=theme['bg'],
            fontshadow=theme['fg'],
            foreground=theme['dark-yellow'],
            padding=10
        ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['workspaceColor'],
            fontshadow=theme['fg'],
            text='',
            padding=7,
            # font="Font Awesome 5 Free Solid",
            fontsize=20,
            # mouse_callbacks={'Button1': open_power_options, },
        ),
        widget.Spacer(length=7),

        # ----------
        #   the battery
        # ----------
        widget.Battery(
            background=theme['bg'],
            foreground=theme['cyan'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%}",
            fontshadow=theme['fg'],
            charge_char="",
            empty_char="",
            full_char="",
            font="Font Awesome 5 Free Solid",
            notify_below=25,
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
        ),
        widget.BatteryIcon(
            background=theme['bg'],
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
            # scale=1,
            # color_path="/home/waleed/.config/qtile/battery-icons"
            # foreground=theme['dark-magenta'],
            # format="{watt:.2f} W - {percent:2.0%} ",
        ),
        widget.Spacer(length=7),

        # ----------
        # brightness
        # ----------
        widget.Backlight(
            background=theme['bg'],
            foreground=theme['yellow'],
            backlight_name="intel_backlight",
            # brightness_file="/sys/class/backlight/intel_backlight",
            # max_brightness_file="/sys/class/backlight/intel_backlight",
            # foreground=theme['dark-magenta'],
            fontshadow=theme['bg'],
            format="{percent:2.0%}  ",
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            mouse_callbacks={'Button1': toggle_redshift, },
        ),
        widget.Spacer(length=7),

        # ---------------
        # volume level
        # ---------------
        widget.Volume(
            background=theme['bg'],
            foreground=theme['blue'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%} ",
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            fontshadow=theme['fg'],
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['blue'],
            text='',
            padding=5,
            fontsize=12,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.Spacer(length=7),

        # --------
        # NET
        # --------
        widget.Net(
            background=theme['bg'],
            foreground=theme['magenta'],
            fontshadow=theme['fg'],
            format='{up}  {down}   ',
            font="Font Awesome 5 Free Solid",
            fontsize=18,
        ),
        widget.Spacer(length=7),

        # --------
        #   Wallpaper
        # --------
        widget.Wallpaper(
            background=theme['bg'],
            foreground=theme['fg9'],
            fontshadow=theme['fg'],
            label="",
            fontsize=18,
            directory="~/.config/qtile/wallpapers",
        ),
        widget.Spacer(length=7),

        # ------------------------------------------------
        # -------- Beginning of the middle ---------------
        # ------------------------------------------------
        widget.Spacer(),
        # ----------
        #   Clock
        # ----------
        widget.Clock(
            background=theme['bg'],
            foreground=theme['yellow'],
            format="(%I:%M) - %A, %d %B  ",
            fontshadow=theme['fg'],
            fontsize=18,
        ),
        # widget.TextBox(
        #     background=theme['widget'],
        #     foreground=theme['workspaceColor'],
        #     text='',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     margin=2
        # ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ middle end ------------------
        # ------------------------------------------------

        # -------------
        #   Thermal Sensor CPU
        # -------------
        widget.ThermalSensor(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            fontshadow=theme['fg'],
        ),
        widget.TextBox(
            background=theme['backgroundColor'],
            foreground=theme['dark-yellow'],
            fontshadow=theme['bg'],
            text='',
            padding=5,
            fontsize=16,
            font="Font Awesome 5 Free Solid",
        ),
        widget.Spacer(length=7),


        # --------
        #   Memory
        # --------
        widget.Memory(
            background=theme['bg'],
            foreground=theme['dark-green'],
            format="{MemPercent: .0f} %  ",
            fontshadow=theme['fg'],
            font="Font Awesome 5 Free Solid",
            fontsize=18,
            # plasma-systemmonitor
            mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        ),
        # widget.TextBox(
        #     text='',
        #     background=theme['dark-blue'],
        #     foreground=theme['widget-fg'],
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        #     margin=2
        # ),
        widget.Spacer(length=7),

        # ----------
        #   processor CPU
        # ----------
        widget.CPUGraph(
            background=theme['bg'],
            foreground=theme['dark-yellow'],
            fill_color=theme['dark-yellow'],
            graph_color=theme['magenta'],
            # format='{load_percent}%',
            font="Font Awesome 5 Free Solid",
            border_width=0,
            line_width=0,
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        # widget.TextBox(
        #     background=theme['dark-yellow'],
        #     foreground=theme['backgroundColor'],
        #     text=' ',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_gnome_system_monitor, },
        # ),
        widget.Spacer(length=7),

        widget.GroupBox(
            background=theme['bg'],
            foreground=theme["fg1"],
            active=theme["foregroundColor"],
            inactive=theme["workspaceColor"],

            # Text color of the selected page
            block_highlight_text_color=theme['cyan'],
            # Selected color
            highlight_color=theme['fg6'],
            fontsize=20,
            highlight_method='line',
            disable_drag=True,
            borderwidth=2,
            padding=4,
        ),

        widget.Spacer(length=7),

        widget.WindowCount(
            background=theme['bg'],
            foreground=theme['backgroundColor'],
            show_zero=True,
            fontsize=18,
        ),
        widget.CurrentLayoutIcon(
            background=theme["bg"],
            foreground=theme['backgroundColor'],
            scale=0.65,
            padding=3,
        ),

        widget.Spacer(length=7)
    ],
    background=theme['fg8'],
    size=22,
    fontsize=18,
    border_width=[6, 0, 6, 0],  # Draw top and bottom borders
    border_color=[
        theme["fg8"],
        theme["fg8"],
        theme["fg8"],
        theme["fg8"]
    ]  # Borders are magenta
)

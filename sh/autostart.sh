#!/bin/sh

nm-applet -sm-disable &
blueman-applet &
# xrandr --output eDP-1 &
# xfce4-screensaver &
xfce4-power-manager &
setxkbmap -layout "be,ar" -option "grp:win_space_toggle" &
/usr/lib/polkit-kde-authentication-agent-1 &
picom -b --experimental-backends --dbus --config ~/.config/qtile/picom/sharp_shado.conf &
# deadd-notification-center &
#start the conky to learn the shortcuts
#conky -c $HOME/.config/qtile/scripts/radeontop &

# redshift -l -6.21462:106.84513 &
# feh --bg-scale ~/waleed/Pictures/photowm/wally.jpg &
feh --bg-scale /home/waleed/.config/qtile/wallpapers/wallpapersden.jpg  &

#copyq &
#nm-applet &
#mictray &
pasystray &
volumeicon &
#deadd-notification-center &
#~/.fehbg &
#xrandr --auto
xrdb -merge ~/.Xresources

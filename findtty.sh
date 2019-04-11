# script name: findtty.sh
# author: Jerry Davis
# source: https://gist.github.com/lanhed/dcb652c83f032fea31c9
#
# this little script determines what usb tty was just plugged in
# on osx especially, there is no utility that just displays what the usb
# ports are connected to each device.

\ls -1 /dev/tty* > before.tty.list

if [ -z "$PS1" ]; then
    read -s -n1 -t 10 -p "Connect cable, press Enter: " keypress
    echo
else
    sleep 10
fi

\ls -1 /dev/tty* > after.tty.list

ftty=$(diff before.tty.list after.tty.list 2> /dev/null | grep '>' | sed 's/> //')
echo $ftty
rm -f before.tty.list after.tty.list
export MCPUTTY=$ftty  
# PiCTA
Raspberry Pi/Web Browser Chicago Bus Tracker

### About

Project by Taylor Hokanson  
www.taylorhokanson.com  
taylor [at] taylorhokanson [dawt] com 

This code tracks the next two arrival times for the CTA
bus/stop/direction combo of your choice. I know we've got smartphone aps
for this, but I got to thinking
about how many clicks it takes each time to check the bus on my phone. I really
only ever care about the one stop outside my house, and I want to be
able to glance at the predictions many times while getting ready in the
morning.

Note: You must apply for you own API key in order for this code to work. Each
key only allows a certain amount of queries per day, so keep this in
mind if you leave the page running 24/7. Even if you do hit the cap it
should reset at midnight, and you can always code in downtime or
decrease query frequency.

You can use this code with or without a Raspberry Pi. If you just want
the browser functionality, copy the Browser folder to your computer and
create a bookmarklet to index.html. Done! If you want to make a standalone
device, read on. For those totally new to Raspberry Pi, please follow the
excellent instructions at
[Adafruit](https://learn.adafruit.com/category/raspberry-pi) to get your
pi configured for SSH and connected to the internet. Make sure to set
the timezone correctly - this will be important later.

### Bill of Materials

1. Raspberry Pi (not sure which version I used, but it has 26 GPIO pins)
2. Keyboard/mouse (used only during initial setup)
3. Computer monitor (mine has a resolution of 1440 x 900)
4. USB wifi dongle (though Ethernet works too)
5. Tactile switches, wire, female headers, solder
6. HDMI to DVI cable
7. RPi power source
8. 4GB SD card

### Set up Kiosk Mode

First we'll teach the Pi to boot automatically and head straight for a
fullscreen Chromium window (see 
[this link](http://blogs.wcode.org/2013/09/howto-boot-your-raspberry-pi-into-a-fullscreen-browser-kiosk/#comments-toggle)
 for more info). The following commands assume your are logged in to
 your pi via SSH. Note that RPi will not warn you if this process will
 not fit in your remaining SD card space. You can check with `df -m` to
 see how much disk space remains, and delete old update files with `sudo
 apt-get clean`.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install matchbox chromium x11-xserver-utils ttf-mscorefonts-installer xwit sqlite3 libnss3
sudo reboot
```

I didn't have any problems with my monitor auto-detecting, but
apparently this can be an issue. If you have problems, check out step 2
on the link at the top of this section.

Now we'll edit some files to execute automatically on startup. First,
`sudo nano /etc/rc.local` and add the following code above `# Print the IP
address`:

```
if [ -f /boot/xinitrc ]; then
	ln -fs /boot/xinitrc /home/pi/.xinitrc;
	su - pi -c 'startx' &
fi
```

Now `sudo nano /boot/xinitrc` (which creates a new file) and add the following code:

```
#!/bin/sh
while true; do

	# Clean up previously running apps, gracefully at first then harshly
	killall -TERM chromium 2>/dev/null;
	killall -TERM matchbox-window-manager 2>/dev/null;
	sleep 2;
	killall -9 chromium 2>/dev/null;
	killall -9 matchbox-window-manager 2>/dev/null;

	# Clean out existing profile information
	rm -rf /home/pi/.cache;
	rm -rf /home/pi/.config;
	rm -rf /home/pi/.pki;

	# Generate the bare minimum to keep Chromium happy!
	mkdir -p /home/pi/.config/chromium/Default
	sqlite3 /home/pi/.config/chromium/Default/Web\ Data "CREATE TABLE meta(key LONGVARCHAR NOT NULL UNIQUE PRIMARY KEY, value LONGVARCHAR); INSERT INTO meta VALUES('version','46'); CREATE TABLE keywords (foo INTEGER);";

	# Disable DPMS / Screen blanking
	xset -dpms
	xset s off

	# Reset the framebuffer's colour-depth
	fbset -depth $( cat /sys/module/*fb*/parameters/fbdepth );

	# Hide the cursor (move it to the bottom-right, comment out if you want mouse interaction)
	xwit -root -warp $( cat /sys/module/*fb*/parameters/fbwidth ) $( cat /sys/module/*fb*/parameters/fbheight )

	# Start the window manager (remove "-use_cursor no" if you actually want mouse interaction)
	matchbox-window-manager -use_titlebar no -use_cursor no &

	# Start the browser (See http://peter.sh/experiments/chromium-command-line-switches/)
	chromium  --app=http://URL.of.your/choice.html

done;
```

Before you save the file, note that last line before `done;`. This is
where you'll direct the Pi to open up a local file that contains the
PiCTA webpage/code. My path is as follows:

```
chromium  --app=file:///home/pi/Desktop/scripts/bustracker/index.html
```

Even if you haven't got anything there yet you should still be able to
boot the Pi and have it  bring up Chromium in full screen with a "page
not found" error.

### Local Webpage

The Browser folder contains an HTML doc, a CSS page for controlling
visual style, and a local copy of JQuery. You'll probably want to check
for updated JQ versions rather than just rolling with the one I
included, but that's up to you. I recommend you place all three items in
a folder called scripts on your RPi desktop.

### Physical Buttons

One funny feature of the RPi is that it has no physical shutdown button.
Sure, you can implement a shutdown via SSH, but we want the convenience
of single touch wake/sleep. There's a great tutorial at 
[Makezine](http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/) 
on this topic. It's well worth the read if you want to learn about both
the GPIO pins and the advantage of callbacks over polling. For our
purposes we'll need a restart button and a shutdown button.

Restart is the easiest to implement, as my version of the Pi already has
two pads that just need to be jumped. All you need to do here is to
solder on a pair of wires and a tactile switch. The shutdown feature is
not automatically included in the OS and must be created from scratch.
While this guy's tutorial worked for me regarding restart, I needed to
use a different method to get shutdown working.

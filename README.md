# IGZen

## Motivation

My sports team needs me to upload pictures to Instagram for accountability,
motivation for team mates, marketing, etc. I don't wish to have the app
installed on my phone, and end-up spending time endlessly scrolling my feed.
Instagram doesn't allow uploading pictures from their web site on a Desktop.

I tried using the Desktop browser with mobile emulation (or a mobile User
Agent), but the upload experience was pretty bad - you can't pre-process images
before uploading them if you don't have a touch screen.

`igzen` lets me pre-process the image using a Python+Tkinter based viewer, and
then uses selenium to post the images.

## Usage

```sh

# Set INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD environment variables
$ export INSTAGRAM_USERNAME="foobar"
$ export INSTAGRAM_PASSWORD="passwordyo!"

# Install the requirements
$ pip install -r requirements.txt

# Run the main script
$ python main.py --crop <path-to-image> "caption with #hashtags"

```

In the image viewer/cropper, you can click anywhere and draw a square to crop
the image. Hit `SPACE` to actually save the current crop to disk. Hit `q` to
close the image editor, and your browser should automatically open up.

You could pass the `--share` argument to completely automate the process, and
not requiring to even click the share button at the end. If it makes you anxious
to post without any manual checks, don't use this flag.

*NOTE*: The tool uses `pyautogui` to select the image to upload, after signing
into Instagram. You need to make sure that the browser window opened by the tool
is the focused window, for everything to work as expected!

![igzen](https://user-images.githubusercontent.com/315678/73592597-1ca4fa00-4522-11ea-8cbe-1dcbb3120a85.gif)

Happy Instagramming!

## The Name

IGZen stands for Instagram Zen. Zen could be a reference to the simplicity of
the tool. It could also refer to the fact that this tool lets you post stuff to
Instagram, without getting sucked into the timeline and letting it eat away into
your focus time.

## LICENSE

This tool is licensed under GPLv3

![logo](https://raw.githubusercontent.com/balena-io-projects/balena-sound/master/docs/images/balenaSound-logo.png)

Fork of balenaSound with a plugin for streaming [ChristmasFM](https://christmasfm.com/).

This plugin launches a Flask server running on port 3500 which accepts commands for turning the stream on/off, and adjusting the volume. It is located under `plugins\cfm`.
## Usage
There are three commands accepted by the server. GET requests are used in all cases for ease of use (lets you control this from a browser)

- `(YOUR_IP):3500/cfm/volup` - Increments the volume by 10 (maximum 100)
- `(YOUR_IP):3500/cfm/voldown` - Decrements the volume by 10 (minimum 0)
- `(YOUR_IP):3500/cfm/toggle` - Turns the stream on or off

## Notes
- You can also use the server `plugins\cfm\cfm_app.py` as a standalone `Python3` server, note the requirements are defined in the `Dockerfile`.
- This is quickly thrown together, I don't recommend exposing the server to the public internet
- If you are streaming music via Bluetooth it will not stop if you start ChristmasFM, both sounds will play at once (this is either a bug or a feature depending on your musical taste)

## Further Reading
Have a look at the full [readme](https://github.com/balenalabs/balena-sound) for more details.

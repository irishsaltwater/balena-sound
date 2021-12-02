from flask import Flask
import vlc

app = Flask(__name__)

christmas_fm = vlc.MediaPlayer("https://christmasfm.cdnstream1.com/2547_128.mp3")
christmas_fm.audio_set_volume(50) # Default volume to middle point


@app.route("/cfm/toggle")
def toggle():
    # Toggle the stream
    # todo: Retry if failure
    print("toggle")
    if not christmas_fm.is_playing():
        print("Turning stream on")
        christmas_fm.play()
    else:
        print("Turning stream off")
        christmas_fm.stop()

    return ('', 200)


@app.route("/cfm/voldown")
def vol_down():
    # Decrement by 10
    print("Volume down.")
    current_volume = christmas_fm.audio_get_volume()
    new_volume = max(0, (current_volume - 10))
    print("Setting volume to " + str(new_volume))
    christmas_fm.audio_set_volume(new_volume)

    return ('', 200)


@app.route("/cfm/volup")
def vol_up():
    # Increment by 10
    print("Volume up.")

    current_volume = christmas_fm.audio_get_volume()
    new_volume = min(100, (current_volume + 10))
    print("Setting volume to " + str(new_volume))
    christmas_fm.audio_set_volume(new_volume)
    return ('', 200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500, debug=False)

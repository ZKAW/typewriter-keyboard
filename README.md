# Typewriter keyboard

#### Intro
This app will play typewriter sound while typing on the keyboard.

#### Installation
```bash
pip3 install -r requirements.txt
```

#### Usage
```bash
python3 app.py
```
* Or
Start `app.exe` inside dist folder

#### Warning
* Make sure the `sounds` folder is in the same folder as app
* The .exe app may be detected as a virus, because it uses the script listen for key presses, but it is not a virus. 
* You can generate your own .exe with `pyinstaller -F app.exe`
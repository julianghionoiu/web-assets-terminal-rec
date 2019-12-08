

## Run

Activate
```
. venv/bin/activate
```

Test
```
py.test ./tests
```

Test with different diff tool
```
py.test ./tests --approvaltests-use-reporter='PythonNative'
```


Run 
```
./run.py
```

Play recording
```
asciinema play build/data.cast
```


## Background

ANSII Escapes

http://ascii-table.com/ansi-escape-sequences.php
http://ascii-table.com/ansi-escape-sequences-vt-100.php
http://www.termsys.demon.co.uk/vtansi.htm
https://www.real-world-systems.com/docs/ANSIcode.html

https://github.com/tartley/colorama

```
\u001b       Esc
\u0007       Bel
Esc]...Bel   Terminal specific command - ignore

Esc=         Set alternate keypad mode
Esc>         Set numeric keypad mode

Esc[2J       Erase Display
Esc[1;21r    Enable scrolling from row {start} to row {end}.
Esc[K        Erase Line - from cursor

Esc[?1h      Set cursor key to application
Esc[?1l      Set cursor key to cursor
Esc[?12$p    ?
Esc[?12h     ?
Esc[?12l     ?
Esc[?25l     Hide cursor
Esc[?25h     Show cursor
Esc[?2004h   Cursor after enter - could be a focus notify - release focus

Esc[m        Turn off character attributes
Esc[H        Move cursor to the home position at the upper left of the screen
Esc[21;1H    Move cursor to the position
Esc[6n       Query Cursor Position

Esc[26A      Cursor up by the specified number of lines
Esc[26B      Cursor down by the specified number of lines
Esc[26C      Cursor forward by the specified number of columns
Esc[26D      Cursor backward by the specified number of columns


\b           Backspace
\r           Return to beginning of line
\n           Newline
```

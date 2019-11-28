

## Run

Download statement file from HSBC

Run script
```
. venv/bin/activate
./run.py
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

Esc[K        Erase Line - from cursor
Esc[1;21r    Enable scrolling from row {start} to row {end}.
Esc[2J       Erase Display

Esc[H        Move cursor to the home position at the upper left of the screen
Esc[?1h      Set cursor key to application
Esc[?1l      Set cursor key to cursor
Esc[?25l     Hide cursor
Esc[?25h     Show cursor
Esc[?2004h   Cursor after enter - could be a focus notify - release focus
Esc[21;1H    Move cursor to the position
Esc[6n       Query Cursor Position
Esc[26C      Moves the cursor forward by the specified number of columns

Esc[m        Turn off character attributes

\b           Backspace
\r           Return to beginning of line
\n           Newline

\u001b[?25l
```
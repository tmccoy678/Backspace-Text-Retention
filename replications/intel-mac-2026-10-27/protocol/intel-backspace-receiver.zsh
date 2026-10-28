#!/bin/zsh

set -eu
umask 077

readonly artifact_dir="$1"
readonly stamp="$2"
readonly child_state="${artifact_dir}/intel-script-experiment-${stamp}.child-pty.txt"

{
  print -r -- "CHILD_PTY_TTY=$(/usr/bin/tty)"
  print -r -- "TERM=${TERM-UNKNOWN}"
  print -r -- "LINES=$(/usr/bin/tput lines 2>/dev/null || print -r -- UNKNOWN)"
  print -r -- "COLUMNS=$(/usr/bin/tput cols 2>/dev/null || print -r -- UNKNOWN)"
  print -r -- "STTY_BEGIN"
  /bin/stty -a
  print -r -- "STTY_END"
} >| "$child_state"
/bin/chmod 600 "$child_state"

print -r -- "MACOS SCRIPT NATIVE LINE-EDIT TRIAL"
print -r -- "Type a made-up, nonsensitive ASCII draft without pressing Return."
print -r -- "Press the physical Delete key once per character until the draft is gone."
print -r -- "Type a different final sentence, then press Return once."
print -r -- ""

IFS= read -r committed_line
print -r -- "CHILD_RECEIVED: ${committed_line}"


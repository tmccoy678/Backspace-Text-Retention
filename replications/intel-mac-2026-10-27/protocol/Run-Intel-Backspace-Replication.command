#!/bin/zsh

set -eu
umask 077

readonly artifact_dir='/Users/Blu/Desktop/BackspaceGate-Intel-Mac-Replication-2026-10-27'
readonly receiver="${artifact_dir}/intel-backspace-receiver.zsh"
readonly stamp="$(/bin/date '+%Y%m%d-%H%M%S')"
readonly transcript="${artifact_dir}/intel-script-experiment-${stamp}.typescript"
readonly metadata="${artifact_dir}/intel-script-experiment-${stamp}.metadata.txt"
readonly latest="${artifact_dir}/LATEST.txt"

{
  print -r -- "METHOD=macos-script-canonical-line-edit-v1"
  print -r -- "COLLECTION_STARTED=$(/bin/date '+%Y-%m-%d %H:%M:%S %Z')"
  print -r -- "INPUT_SOURCE=physical-keyboard"
  print -r -- "RECORDER=/usr/bin/script -q"
  print -r -- "CHILD=/bin/zsh ${receiver}"
  print -r -- "TRANSCRIPT=${transcript}"
  print -r -- "PARENT_TTY=$(/usr/bin/tty)"
  print -r -- "TERM=${TERM-UNKNOWN}"
  print -r -- "PARENT_LINES=$(/usr/bin/tput lines 2>/dev/null || print -r -- UNKNOWN)"
  print -r -- "PARENT_COLUMNS=$(/usr/bin/tput cols 2>/dev/null || print -r -- UNKNOWN)"
  print -r -- "PARENT_STTY_BEGIN"
  /bin/stty -a
  print -r -- "PARENT_STTY_END"
  /usr/bin/sw_vers
  /usr/bin/uname -a
  /usr/bin/mdls -name kMDItemVersion -raw /System/Applications/Utilities/Terminal.app | /usr/bin/awk '{print "TERMINAL_VERSION=" $0}'
  /usr/bin/shasum -a 256 /usr/bin/script | /usr/bin/awk '{print "SCRIPT_SHA256=" $1}'
  /usr/bin/shasum -a 256 "$receiver" | /usr/bin/awk '{print "RECEIVER_SHA256=" $1}'
} >| "$metadata"
/bin/chmod 600 "$metadata"

print -r -- ""
print -r -- "BACKSPACE GATE — INTEL MAC RECORDED-PTY REPLICATION"
print -r -- "The recorder is active. Follow the instructions below exactly."
print -r -- "Do not type private or sensitive text."
print -r -- ""

/usr/bin/script -q "$transcript" /bin/zsh "$receiver" "$artifact_dir" "$stamp"
/bin/chmod 600 "$transcript"

{
  print -r -- "COLLECTION_FINISHED=$(/bin/date '+%Y-%m-%d %H:%M:%S %Z')"
  /usr/bin/stat -f 'TRANSCRIPT_BYTES=%z' "$transcript"
  /usr/bin/stat -f 'TRANSCRIPT_MODE=%Sp' "$transcript"
  /usr/bin/shasum -a 256 "$transcript" | /usr/bin/awk '{print "TRANSCRIPT_SHA256=" $1}'
} >> "$metadata"

{
  print -r -- "TRANSCRIPT=${transcript}"
  print -r -- "METADATA=${metadata}"
  print -r -- "CHILD_PTY=${artifact_dir}/intel-script-experiment-${stamp}.child-pty.txt"
} >| "$latest"
/bin/chmod 600 "$latest"

print -r -- ""
print -r -- "STATUS=RECORDED"
print -r -- "Tell Blu only that the recording is finished. Do not reveal the phrase yet."
print -r -- "You may leave this window open."


#!/bin/bash

# Commits each submodule. stdout is disabled for ignoring errors,
# keep that in mind.

cd ..

git add codewars-brainfuck
git commit -m "Update codewars-brainfuck repo" 1>/dev/null
git add codewars-c 1>/dev/null
git commit -m "Update codewars-c repo" 1>/dev/null
git add codewars-asm 1>/dev/null
git commit -m "Update codewars-asm repo" 1>/dev/null
git add codewars-python 1>/dev/null
git commit -m "Update codewars-python repo" 1>/dev/null
git add codewars-rust 1>/dev/null
git commit -m "Update codewars-rust repo" 1>/dev/null
git add codewars-shell 1>/dev/null
git commit -m "Update codewars-shell repo" 1>/dev/null


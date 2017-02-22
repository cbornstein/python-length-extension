# python-length-extension
Python script to illustrate length extension vulnerability in URLs containing MD5

# Explanation
This program assumes an MD5 hash of an 8-character password concatenated with a series of server commands. A sample URL format can be found below:

http://www.server.com/api?token=11ed1b5786c5fc4d4fa4294f4d281df1&user=alice&command1=ListFiles&command2=NoOp

This program will calculate the total message length, presumed padding and text equivalent of padding. The program uses the existing hash as the input for a new MD5 hash that will append an additional command onto the existing list of commands concatenated with the password, which ultimately remains unknown. The new hash is appropriately inserted into a new URL, along with the padding of the previous message and a new command, which in this illustrative example, is "&command3=DeleteAllFiles"

# Usage
This program takes a URL of the above form as a command line argument.
python len_ext.py "url"

# WARNING:
This program tests the generated length extension attack after generation using urllib. While the sample command is unlikely to inflict any damage upon a given server, do not use this script on a server for which you do not have permission to test this code on. Please comment out the last section of code to stop the live URL test.

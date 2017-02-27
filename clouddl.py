#!/usr/bin/python
#
# MIT License
#
# Copyright (c) 2017 Caesim404
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import cfscrape
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Downloads files behind cloudflare's anti-bot page by passing cookies and user agent to another command.")
parser.add_argument("-d", "--downloader", choices=["curl","wget"], action="store", help="use a predefined command")
parser.add_argument("-u", "--url", action="store", required=True, help="downlad from this url")
parser.add_argument("-H", "--header", action="append", type=lambda kv: kv.split(":"), help="add a HTTP header")
parser.add_argument("-a", "--user-agent", action="store", type=str, help="use this user agent")
parser.add_argument("-v", "--verbose", action="store_true", help="show debug info")
parser.add_argument("command", metavar="COMMAND", type=str, nargs=argparse.REMAINDER, help="""
	call a command. Available variables: 
		{a} = user agent, 
		{c} = cookies, 
		{u} = url, 
		{h} = headers (repeats the word before it for each one, must be alone in a word)
""")
args = parser.parse_args()

args.header = {k:v for k,v in args.header}

if args.downloader and args.command:
	parser.error("-d/--downloader can't be set alongside COMMAND")
if not args.downloader and not args.command:
	parser.error("you must set either -d/--downloader or COMMAND")

if args.verbose:
	print("Arguments:", args)

tokens, user_agent = cfscrape.get_tokens(args.url, args.user_agent, headers=args.header, stream=True)
if args.verbose:
	print("Tokens:", tokens)
	print("User-Agent:", user_agent)


if args.downloader == "curl":
	cmd = ["curl", "-O", "--cookie", "{c}", "--user-agent", "{a}", "--header", "{h}", "{u}"]
elif args.downloader == "wget":
	cmd = ["wget", "--header", "Cookie: {c}", "--user-agent", "{a}", "--header", "{h}", "{u}"]
else:
	cmd = args.command

if args.verbose:
	print("Raw command:", cmd)

i = 0
while True:
	cmd[i] = cmd[i].format(
		c=";".join(["%s=%s" % (k,v) for (k,v) in tokens.items()]),
		a=user_agent,
		u=args.url,
		h="{h}",
	)
	
	j=i-1
	if cmd[i] == "{h}" and j >= 0:
		word = cmd.pop(j)
		cmd.pop(j)
		
		for kv in args.header.items():
			cmd.insert(j, ":".join(kv))
			cmd.insert(j, word)
			i += 2
		i -= 1
	else:
		i += 1
	
	if i >= len(cmd):
		break

if args.verbose:
	print("Processed command:", cmd)

exit(subprocess.call(cmd))

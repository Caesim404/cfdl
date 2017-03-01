# cfdl 0.2.1

Downloads files behind cloudflare's anti-bot page by passing cookies and user agent to another command.

## Dependencies:
* [Python 2 or 3](https://www.python.org/)
* [cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape)
* wget (optional)
* curl (optional)

I made it only for Linux, but it might work on other systems too.

## Installation:

Simply execute the file. `./cfdl.py`

Or you can install it on your Linux system:

1. `wget https://github.com/Caesim404/cfdl/archive/0.2.1.tar.gz`
2. `sudo install -Dm755 cfdl.py /usr/bin/cfdl`

Or if you have Arch Linux, get it from the [AUR](https://aur.archlinux.org/packages/cfdl).

## Examples:

#### Download a file using curl
`./cfdl.py -d curl -u http://example.com/file.zip`
#### Download a file using wget
`./cfdl.py -d wget -u http://example.com/file.zip`
#### Download a file using a custom command
`./cfdl.py -u http://example.com/file.zip -- my-downloader --cookies {c} --user-agent {a} --url {u}`
#### Download a file using custom headers and user agent
`./cfdl.py -d curl -H "Referer: example.org" -H "X-Custom: value" -a "Custom User-Agent" -u http://example.com/file.zip`

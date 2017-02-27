# clouddl 0.1

Downloads files behind cloudflare's anti-bot page by passing cookies and user agent to another command.

## Dependencies:
* [Python 2 or 3](https://www.python.org/)
* [cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape)

I made it only for Linux, but it might work on other systems too.

## Installation:

Simply execute the file. `./clouddl.py`

Or you can install it on your Linux system:

1. `wget https://raw.githubusercontent.com/Caesim404/clouddl/master/clouddl.py`
2. `sudo install -Dm755 clouddl.py /usr/bin/clouddl`

Or if you have Arch Linux, get it from the AUR.

## Examples:

#### Download a file using curl
`./clouddl.py -d curl -u http://example.com/file.php`
#### Download a file using wget
`./clouddl.py -d wget -u http://example.com/file.php`
#### Download a file using custom command
`./clouddl.py -u http://example.com/file.php downloader --cookies {c} --user-agent {a} --url {u}`
#### Download a file using custom headers and user agent
`./clouddl.py -d curl -H "Referer: example.org" -H "X-Custom: value" -a "Custom User-Agent" -u http://example.com/file.php`

# cfdl 0.2.1

Downloads files behind cloudflare's anti-bot page by passing cookies and user agent to another command.

## Dependencies:
* [Python 3 or 2](https://www.python.org/)
* [cfscrape](https://github.com/Anorov/cloudflare-scrape)
* wget (optional)
* curl (optional)

I made it for Linux, but it might work on other systems too.

## Installation:

If you have Arch Linux, get it from the [AUR](https://aur.archlinux.org/packages/cfdl) and use `cfdl` to run it.

## Examples:

#### Download a file using curl
`./cfdl.py -d curl -u http://example.com/file.zip`
#### Download a file using wget
`./cfdl.py -d wget -u http://example.com/file.zip`
#### Download a file using wget but use a different file name
`./cfdl.py -d wget -u http://example.com/file.zip -- -O newfile.zip`
#### Download a file using a custom command
`./cfdl.py -u http://example.com/file.zip -- my-downloader --cookies {c} --user-agent {a} --url {u}`
#### Download a file using custom headers and user agent
`./cfdl.py -d curl -H "Referer: example.org" -H "X-Custom: value" -a "Custom User-Agent" -u http://example.com/file.zip`

#### Use it to download source files in a PKGBUILD
    makedepends=('cfdl')
    DLAGENTS=('http::/usr/bin/cfdl -u %u -d curl -- -fLC - --retry 3 --retry-delay 3 -o %o'
              'https::/usr/bin/cfdl -u %u -d curl -- -fLC - --retry 3 --retry-delay 3 -o %o')

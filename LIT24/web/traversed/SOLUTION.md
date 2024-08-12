This one was kinda weird and felt like the vulnerability was super forced.

After guessing and poking around for a bit, I was able to determine that the webserver lets us easily escape the web server directory due to improper checks on the requested resource.

We can provide the url encoded version of a dot which is not sanitized out to request any file, effectively giving us LFI.

I then used some good ol' guessing + common LFI tricks to find the flag.

`curl 'litctf.org:31778/%2e%2e/%2e%2e/%2e%2e/%2e%2e/proc/self/cwd/flag.txt'
LITCTF{backtr@ked_230fim0}`
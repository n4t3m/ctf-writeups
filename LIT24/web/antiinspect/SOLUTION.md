This is a baby's first web challenge. We are given a url with a warning that opening would lead to our browser crashing.

We can use curl to easily fetch the page contents from within our terminals and get the flag.

```
curl http://litctf.org:31779/ | grep "LIT"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   482  100   482    0     0   3260      0 --:--:-- --:--:-- --:--:--  3394
      const flag = "LITCTF{your_%cfOund_teh_fI@g_94932}";
```
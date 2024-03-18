We are given the source code of a node application.

There's one route that provides a clear path to the flag:

```js
app.get('/chat', (req, res) => {

    console.log(req.socket.remoteAddress);

    if (req.socket.remoteAddress != '127.0.0.1') //make sure flag is just for locally
        do {
            req.query.message = req.query.message.replace(/(flag)/i, "");
        } while (req.query.message.indexOf("flag") > -1)

    if (/hi|hello|hey/i.test(req.query.message))
        return res.json({ message: "Hi, nice to meet you! My name is Chad Jeepeetee!" });

    if (/what|who|were|when|why/i.test(req.query.message))
        return res.json({ message: "I don't know!" });

    if (/flag/i.test(req.query.message))
        return res.json({ message: "The flag is 1753c{fake_flag_for_testing}" });

    return res.json({ message: req.query.message });
})
```

Looks like we have to send a request to the `/chat` endpoint with flag as a message. If flag is in the message after all isntances of flag is removed, we are given the flag. We can bypass the replace statements if the remote address is set to localhost.

Initially, I tried to control the `req.socket.remoteAddress` parameter, but this was not possible given how the challenge was setup. 

The exploit here is in how the matching works. The `i` after the flag literal indicates case insensetivity. Looking at how the replace function is setup:

```js
        do {
            req.query.message = req.query.message.replace(/(flag)/i, "");
        } while (req.query.message.indexOf("flag") > -1)
```

The removal is based on casing, however the while loop condition is not. If the message parameter were set to something like `FLflagAG`, `flag` would be removed, the condition would break us out of the while loop, and we meet the condition to get the flag.


So simply go to `/chat?message=FLflagAG` to retrieve the flag.

Flag: `1753c{ai_is_not_that_smart_you_know}`
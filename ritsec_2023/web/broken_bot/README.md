![](2023-04-03-13-42-28.png)

This challenge sends you to a website with a login page:

![](2023-04-03-13-43-00.png)

Upon entering any credentials, I am redirected to an archive.org webpage:

![](2023-04-03-13-43-57.png)

Taking a look at the network traffic when this happens, a post request is made to `api.telegram.com`.

![](2023-04-03-13-45-02.png)

After this happens, I am redirected.

I looked up the sendMessage api call and found this page:

![](2023-04-03-13-45-58.png)

Looking back at the URL the post request was sent to, it looks like we are given a Telegram bot's token.

Looking through this website (https://telegram-bot-sdk.readme.io/reference), I found a method that seemed interesting for getting information:

![](2023-04-04-13-59-33.png)

Making this API call, I was able to get the following information:

![](2023-04-04-14-01-05.png)

It looks like we have the `username` and `first_name` of the bot. I searched up the bot's username on the telegram mobile app:

![](2023-04-04-14-01-56.png)

Looks like the bot exists, and clicking on this shows us the flag:

![](2023-04-04-14-09-03.png)

Flag: `Flag{Always_Check_For_Misconfigurations}`

The flag itself makes no sense as there was no misconfiguration? atleast from how I see it.

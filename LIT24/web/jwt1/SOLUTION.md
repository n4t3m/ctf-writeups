Upon accessing the site, you are given an option to create an account and sign into it. You are then given a JWT token as your session cookie. When logged in, there is a "GET FLAG" button. I clicked this and was told that I was unauthorized for the flag.

I checked the attributes of the JWT and it two fields, one for username and a boolean value indicating if we have elevated permissions or not.

I ran through the sinple JWT tricks and found that the server just deserializes the data without ensuring that it is properly signed, so we can freely edit the contents of the two values.

Changing thw JWT to indicate that we are an admin with any username yeilds the flag.

LITCTF{o0ps_forg0r_To_v3rify_1re4DV9}
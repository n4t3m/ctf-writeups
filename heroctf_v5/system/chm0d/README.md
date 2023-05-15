# chm0d

There is a file owned by `user`, `/flag.txt`. The current permission level set to the file is `000`.

Usually you could simply use the chmod binary to add the read permission for the current user, but we do not have permission to use the binry.

We can simply use perl to do the same thing and read the flag.

```
user@ecc72c58d3b74cc31e67212a340a8431:/$ perl -e 'chmod 0755, "flag.txt"'
user@ecc72c58d3b74cc31e67212a340a8431:/$ cat flag.txt
user@ecc72c58d3b74cc31e67212a340a8431:/$
```

Flag: `Hero{chmod_1337_would_have_been_easier}`

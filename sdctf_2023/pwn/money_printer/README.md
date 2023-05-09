# Money Printer

![](2023-05-08-17-12-36.png)

Upon connecting to the service and entering random input:

![](2023-05-08-17-15-47.png)

Let's try entering a number:

![](2023-05-08-17-17-07.png)

Looks like if we enter negative numbers the server "gains" money. What if I enter a larger number:

![](2023-05-08-17-17-55.png)

Cool, looks like we got to this point. After playing around with this prompt for a while we can see there is a format string vulnerability.

![](2023-05-08-17-19-27.png)

Using this, we can use %p to leak data off of the stack. I did not decompile the binary but I will assume the flag has been loaded into memory and is lying somewhere on the stack.

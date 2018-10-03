![Viewing an inbox with CLIMail](https://i.imgur.com/eq34i8K.png)

# CLIMail
A command line tool for checking email from the terminal, written in Coconut
## Install
`pip install climail`
## Opening CLIMail
CLIMail is opened straight from the command line by running the command `climail`
## Logging in
The first time CLIMail is opened, the login prompt will require the user to enter three things:
1. Username (example: user@example.com)
2. Password
3. Host (example: imap.gmail.com)

These will be saved into a new file called `climail_credentials.json` located in the current working directory (this behavior is likely to change in the future).
## How to use CLIMail
After the client is logged in and loaded up, interaction with the client is done through commands. Here is a list of all of the possible commands:
```
case action:
    match ":refresh" or ":r":
        """Refreshes the client"""
    match ":folder " + folder:
        """Selects the specified folder"""
    match ":home":
        """Alias for ':folder INBOX'"""
    match ":read " + id:
        """Reads the email specified by the given ID"""
    match ":page " + pageno:
        """
        Change which 'page' of emails is currently being displayed (zero-indexed)
        """
    match ":login":
        """Logs in to a different account"""
    match ":quit" or ":q":
        """Exit CLIMail"""
```

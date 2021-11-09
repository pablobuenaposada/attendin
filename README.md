![alt tag](https://raw.github.com/pablobuenaposada/attendin/master/logo.png)

# attendin

Answering machine for your LinkedIn conversations.

Checks your non answered conversations against regular expressions and sends a predefined message if necessary.

This project born with the intention of managing annoying job offers without salary information, checks if in the messages there are any hint of salary disclosure and if is not the case a message asking about it is being sent.

## Usage
`docker run -e username=your@mail.com -e password=whatever pablobuenaposada/attendin`

you can schedule it with cron (example for MacOS, search your docker binary path for other OS):
`0 * * * * /usr/local/bin/docker run -e username=your@mail.com -e password=whatever pablobuenaposada/attendin`

## Note
This project uses `linkedin-api` package, unfortunately if you have 2FA enabled in your LinkedIn account this package is not yet prepared to work with it, so in order to use this project you must disable 2FA. 
![alt tag](https://raw.github.com/pablobuenaposada/attendin/master/logo.png)

# attendin

Answering machine for your LinkedIn conversations.

Checks your non answered conversations against regular expressions and sends a predefined message if necessary.

This project born with the intention of managing annoying job offers without salary information, checks if in the messages there are any hint of salary disclosure and if is not the case a message asking about it is being sent.

## Usage
1. `git clone https://github.com/pablobuenaposada/attendin.git && cd attendin`
2. `make docker/build`
3. `make docker/run username=user@gmail.com password=whatever`

## Note
This project uses `linkedin-api` package, unfortunately if you have 2FA enabled in your LinkedIn account this package is not yet prepared to work with it, so in order to use this project you must disable 2FA. 
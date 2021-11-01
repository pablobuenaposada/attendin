![alt tag](https://raw.github.com/pablobuenaposada/attendin/master/logo.png)

# attendin

Answering machine for your LinkedIn conversations.

Checks your non answered conversations against regular expressions and sends a predefined message if necessary.

This project born with the intention of managing annoying job offers without salary information, checks if in the messages there's any hint of salary disclosure and if is not the case a message asking about it is being sent.

## Usage
1. `git clone https://github.com/pablobuenaposada/attendin.git && cd attendin`
2. `make docker/build`
3. `make docker/run username=user@gmail.com password=qwerty`

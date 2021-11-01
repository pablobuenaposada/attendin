![alt tag](https://raw.github.com/pablobuenaposada/attendin/master/logo.png)

# attendin

Answering machine for you LinkedIn conversations.

Checks your non answered conversations against regular expressions and sends a predefined message if necessary.

This project born with the intention of managing annoying job offers without salary information, checks if in the messages there's any hint of salary information and if is not the case a message asking about it is being send. 

## Usage
1. `git clone https://github.com/pablobuenaposada/attendin.git`
2. `make docker/build`
3. `make docker/run username=user@gmail.com password=qwerty`

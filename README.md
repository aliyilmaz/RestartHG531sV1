# RestartHG531sV1
It is used to restart Huawei HG531s V1 model modems.

## Install Python3

    sudo apt-get install python3

## Install the required packages

    pip3 install -r requirements.txt

## Enter the folder

    cd RestartHG531sV1

## Specify the access information

Edit the modem ip address along with the username and password you use to access the modem.

    RestartHG531sV1('http://192.168.1.1/', 'vodafone', 'vodafone')

## Run the file

    python3 ./RestartHG531sV1.py

## Is it platform independent?

Yes, it is platform independent, it can be used on any platform with python installed.

## Which platform was also tested?

Pardus

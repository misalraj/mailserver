#!/bin/bash

mail_user=server_user
mail_pwd=server_pwd

sudo apt-get install -y docker
sudo docker pull catatnight/postfix
sudo docker run -p 25:25 -e maildomain=mail.example.com -e smtp_user=$mail_user:$mail_pwd -d catatnight/postfix
sudo docker run -p 587:587 -e maildomain=mail.example.com -e smtp_user=$mail_user:$mail_pwd -v /path/to/certs:/etc/postfix/certs -d catatnight/postfix

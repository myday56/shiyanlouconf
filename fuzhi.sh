#!/bin/sh
tar -xzvf conf.tar config
cp -R ~/shiyanlouconf/config/. ~/.config
cp ~/shiyanlouconf/.vimrc ~/
rm -R /home/shiyanlou/shiyanlouconf/config
sudo cp ./my.cnf /etc/mysql/

#!/bin/bash
sudo useradd testuser
sudo groupadd testgroup
sudo usermod -aG testgroup testuser
id testuser
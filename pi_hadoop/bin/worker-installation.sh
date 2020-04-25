#! /usr/bin/env bash

sudo su

# create java directory
mkdir /opt/java
mv ~/openjdkpkg.tgz /opt/java/
cd /opt/java
tar -zxf openjdkpkg.tar -C /opt/java

# check if files are there
# ls /opt/java

#update alternatives so the command java point to the new jdk
sudo update-alternatives --install /usr/bin/java java /usr/opt/java/jre/bin/java 100
sudo update-alternatives --install /usr/bin/javac javac /usr/opt/java/jre/bin/java 100

#check if java command is pointing to " link currently points to /opt/jdk/jdk1.8.0_05/bin/java"
update-alternatives --display java

#check if java command is pointing to " link currently points to /opt/jdk/jdk1.8.0_05/bin/javac"
update-alternatives --display javac

#check if java is running
java -version
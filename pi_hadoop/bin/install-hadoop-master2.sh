#! /usr/bin/env bash

cat >> ~/.bashrc << EOF
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-armhf
export HADOOP_HOME=/opt/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
EOF

source ~/.bashrc

cat >> /opt/hadoop/etc/hadoop/hadoop-env.sh << EOF
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
EOF
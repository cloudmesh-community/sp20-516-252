# Hadoop Clusters with Raspberry Pi Jessica Zhu sp20-516-252

For reference, master and workers are burnt using `cloudmesh-pi-cluster`.
master: pi@red
workers: red[001 - 002]

and bridge has been properly created.


## install Java on master and workers

Hadoop requires Java. Raspbian Desktop doesn't come with Java installed
, we therefore need to install java on all of the Pi.

### Install Java on master node

run file in `bin/setup-master`

Check if the java installation is successful
`
$ java -version
`

## Install Java on worker nodes

Since workers don't have access to network, java can be installed by master
 passing the installation package to workers.
 
 run file in `bin/master-to-worker`

Now log into the worker, `ssh red001`
and run file `worker-installation`






sudo mkdir /usr/java/
tar -zxf packageName.tar.gz -C /usr/java

sudo update-alternatives --install /usr/bin/java java /usr/java/jre/bin/java 100
sudo update-alternatives --install /usr/bin/javac javac /usr/java/jre/bin/java 100



references
1. https://gist.github.com/filipelenfers/ef3f593deb0751944bb54b744bcac074
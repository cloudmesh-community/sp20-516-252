# Hadoop Clusters with Raspberry Pi Jessica Zhu sp20-516-252

Reference for setup:
https://github.com/cloudmesh/cloudmesh-pi-burn
https://github.com/cloudmesh/cloudmesh-pi-cluster/blob/master/cloudmesh/bridge/README.md

For the numpy issue:
https://github.com/numpy/numpy/issues/14348


For reference, master and workers are burnt using `cloudmesh-pi-cluster`.
    master: pi@red
    workers: red[001 - 002]

and bridge has been properly created.

You should make sure that workers can be logged in without password

## install Java on master and workers

Hadoop requires Java. Raspbian Desktop doesn't come with Java installed
, we therefore need to install java on all of the Pi.

### Install Java on master node

```
cd ~
git clone https://github.com/cloudmesh-community/sp20-516-252.git
cd sp20-516-252/pi_hadoop/bin
sh setup-master.sh
```
If asked: " Do you want to continue?[Y/n]" Enter, Y.
(Maybe try this to avoid type "Y"
`echo "Y" | sh setup-master.sh`
)

Check if the java installation is successful by running
`
$ java -version
`

It should expect return
```
openjdk version "1.8.0_212"
OpenJDK Runtime Environment (build 1.8.0_212-8u212-b01-1+rpi1-b01)
OpenJDK Client VM (build 25.212-b01, mixed mode)
```

## Install Java on worker nodes

Since workers don't have access to network, java can be installed by master
 passing the installation package to workers.
 
 run command 
  ```
sh master-to-worker.sh
```

Now that each worker has the right java zip package, we are gonna upzip and
 install java on each worker using just one line from master:
 
 This py file is in cloudmesh-common (this JobMultiHostScript.py needs to be
  motified till the source code is fixed)
 ```
cd ~/cm/cloudmesh-common/cloudmesh/common
sudo nano JobMultiHostScript.py
```
 ```
 import sys
 
 def main():
    # EXAMPLE FOR TERMINAL - python JobMultiHostScript.py [SCRIPT-FILE] [HOSTS]
    argumentCounter = 0
    for arg in sys.argv[1:]:
        # Script file
        if argumentCounter == 0:
            scriptFile = arg
        # Get hosts
        else:
            hosts = arg
        argumentCounter = argumentCounter + 1
    with open(scriptFile) as f:
        script = f.readlines()
    script = ''.join(script)
    hosts = Parameter.expand(hosts)
    result = JobMultiHostScript.execute(script, "terminal_script", hosts)
if __name__ == '__main__':
    main()
    """script =
    # This is a comment
    # Task: pwd
    pwd     # tag: pwd
    # Task:  uname
    uname -a
    "";
    hosts = Parameter.expand("purple[01-02]")
    result = JobMultiHostScript.execute(script, "script_name", hosts,
                                        beginLine="# Task: pwd", endLine="# Task: uname")
    """

 ```
 
 `python JobMultiHostScript.py ~/sp20-516-252/pi_hadoop/bin/worker-installation.sh red[001-002]`

After that you should see java 8 is installed:
```
$ java -version
openjdk version "1.8.0_212"
OpenJDK Runtime Environment (build 1.8.0_212-8u212-b01-1+rpi1-b01)
OpenJDK Client VM (build 25.212-b01, mixed mode)
```

## Install jps on master

```
sudo apt-get -y install openjdk-8-jdk-headless default-jre
```
If it is successfully installed, it should show something similar to
```buildoutcfg
10116 Jps
```

## Install Hadoop on Master Node

?? Download and install Hadoop version 3.2.0
```
$ cd ~
$ wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz
$ sudo tar -xvzf hadoop-3.2.0.tar.gz -C /opt/
$ cd /opt/
$ mv hadoop-3.1.0 hadoop
```

Set up Environment. Edit `~/.bashrc` and append the following lines 
Then apply the changes to the running environment
```
$ source ~/.bashrc
```

Now set up Hadoop environment by editing `$ /opt/hadoop/etc/hadoop/hadoop-env.sh`

```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
```
If you are unsure where your JAVA_HOME path is, simply try 
`dirname $(dirname $(readlink -f $(which javac)))`
, which returns HOME_PATH.

Setup Hadoop Configuration Files
```
$ cd $/opt/hadoop/etc/hadoop
```

Edit core-site.xml

```
<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>
```

Edit hdfs-site.xml

```
<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
</property>
</configuration>
```
Edit hdfs-site.xml

```
<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>
```
Edit yarn-site.xml

```
<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>
```

Format Namenode

```
$ hdfs namenode -format
```

start Hadoop Cluster

```
cd $HADOOP_HOME/sbin/
./start-dfs.sh
```
If you got an error similar to `Hadoop: start-dfs.sh permission denied`, then
 do the following:

```
cd ~/.ssh
cat id_rsa.pub >> authorized_keys
```
Then,
```
cd $HADOOP_HOME/sbin/
./start-dfs.sh
```
You should see
...

-- then start yarn?


--
sudo mkdir /usr/java/
tar -zxf packageName.tar.gz -C /usr/java

sudo update-alternatives --install /usr/bin/java java /usr/java/jre/bin/java 100
sudo update-alternatives --install /usr/bin/javac javac /usr/java/jre/bin/java 100

references
1. https://gist.github.com/filipelenfers/ef3f593deb0751944bb54b744bcac074
2. https://dev.to/awwsmm/building-a-raspberry-pi-hadoop-spark-cluster-8b2#hadoopspark

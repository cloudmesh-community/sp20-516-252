## Cloudmesh updates

```
$ pip install cloudmesh-installer -U
$ pip install pip -U
$ cloudmesh-installer new ~/ENV3 pi
$ cms help
$ cms pi
```
## Copy ssh key to a node
```
$ ssh-copy-id pi@node_name
```

```
$ ssh pi@node_name
```
When the below shows up:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       WARNING: POSSIBLE DNS SPOOFING DETECTED!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The host key for the node has been changed. To remove such, run
```
$ rm /home/pi/.ssh/known_hosts
```
Now run `ssh pi@node_name` again, and the prompt should asks you `to continue
 connecting?`

## Go password-less: Find out and copy public key

First, add ssh-agent to master bashrc

Next,
```
$ cat ~/.ssh/id_rsa.pub
```
Then log into its node, e.g. `ssh pi@192.168.1.68`. Then type `nano .ssh
/authorized_key` and paste the key to nano file.

Log out of the node, then run `ssh-add`,   `ssh pi@IP_address`. This time you
 should be able to log into the node without a password.


###Alternative way of copying public key (untested)

`ssh-copy-id pi@worker_ip`


## Week 5
### Hypervisor

a. Bare-metal virtualization
    Virtual machine monitor(VMM) installed directly on top of the hardware
    Has direct access to the underlying hardware

b. hosted visualization
    VMM installed on top of the host OS     
    
    Source:
    Cloud Computing by Gregory
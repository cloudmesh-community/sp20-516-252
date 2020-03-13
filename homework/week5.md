### E.Multipass.1.a

Improve the Multipass installation instructions presented here for Mac OS

#### Preprequisite

`hyperkit` is the default Hypervisor.framework. maxOS version 10.10.3 or
 later is required. It is also possible to change to VirtualBox as a
  virtualization provider. However, Multipass instances using VituralBox don
  't get assigned with an IP address as of now.
  
#### Install

Homebrew seems to be the simplest way for installation. It is recommended to
 test out Multipass in a separately user on your machine with `sudo` privilege.
Run commands
```
$ brew cask install multipass
```

To uninstall,
```
brew cask uninstall multipass
```

### Launch

To launch multipass, run
```
$ multipass launch
```

### E.Multipass.2

What is Primary in multipass?

It is a quick Ubuntu instance that is automatically created when users uses
 command `start` or `shell`.
 When launched, this primary instance gets the same properties as if started
  with `launch` without arguments.

Primary is the default instance when no instance name is specified. For
 example, when run commands `shell`, `start`,`stop`,`restart` etc.

### E.Multipass.3

What is snapcraft in multipass?

Snapcraft is a command line tool that helps developers to build and publish
 their applications in snap file format. It supports commands to help
  developers start the project, build applications, upload applications to
   online stores and publish them. Couple commands include
```
init # Initialize a snapcraft project
push # Pushes a snap to the online snap store
```

### E.Multipass.4

How do you write a bibtex entry for <https://multipass.run>

A bibtex entry for the website would be 

@Misc{Multipass,
  author =	 {{Multipass}},
  title =	 {Instant Ubuntu VMs},
  howpublished = {Web Page},
  year =	 2020,
  key =		 {MISSING},
  organization = {MISSING},
  url =
                  {https://multipass.run},
}

### E.Multipass.5

Provide a list of images supported by MacOS
```
# multipass find
```
| Image        | Aliases           | Version  | Description |
| ------------- |:-------------:| -----:| -----: |
| snapcraft:core | core16 | 20200221 | Snapcraft builder for Core 16|
 |snapcraft:core18 |       |   20200221 | Snapcraft builder for Core 18 |
  |16.04  | xenial      |  20200218.1 | Ubuntu 16.04 LTS |
| 18.04   |  bionic,lts | 20200218 | Ubuntu 18.04 LTS |

### E.Multipass.6

Explain cloud-init in Multipass. Provide an example.

Cloud-init is a standard to customize cloud instances. Multipass can use
 cloud-init to customize an instance during launch.
 
Example:
```
multipass launch -n testVM --cloud-init cloud-config.yaml
```

Note that multipass only supports YAML cloud-config files at the moment.

### Sources
<https://multipass.run/docs/installing-on-macos>\
<https://ubuntu.com/blog/using-cloud-init-with-multipass>
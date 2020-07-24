# Sysadmin stuff
--

### Troubleshooting ssh-keys

##### SELinux issues
When trying to connect, and using ssh -vv, if it seems like the public key is not being sent, check if SELinux is running on the server, and if so, allow .ssh folders to be on nfs drives:

```
$ setsebool -P use_nfs_home_dirs 1
```

# Personal VPN Website

## How to deploy in Ubuntu
1. Clone or copy website files to server, e.g. /root/website.

2. Install lighttpd

`apt-get install lighttpd`

3. Configure lighttpd.conf

vi /etc/lighttpd/lighttpd.conf
```
server.document-root        = "/root/website"   -> Path of Website html files.
\#server.username             = "www-data"       -> Disable authentication
\#server.groupname            = "www-data"       -> Disable authentication
server.port                 = 80
```
4. Restart lighttpd

`service lighttpd restart`

5. Add accept rule for port 80 in IPtable.

run command:

`iptables -I INPUT -p tcp --dport 80 -j ACCEPT`

To enable it on bootup:

Add this line in /etc/rc.local before last line 'exit 0'.

vi /etc/rc.local:
```
# Added for HTTP server
iptables -I INPUT -p tcp --dport 80 -j ACCEPT
exit 0
```

Done! Now you can visit the website by server IP or hostname.

netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=135 name=135_udp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=136 name=136_udp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=137 name=137_udp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=138 name=138_udp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=139 name=139_udp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=145 name=145_udp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=udp localport=445 name=445_udp_in

netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=135 name=135_tcp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=136 name=136_tcp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=137 name=137_tcp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=138 name=138_tcp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=139 name=139_tcp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=145 name=145_tcp_in
netsh advfirewall firewall add rule action=allow dir=in protocol=tcp localport=445 name=445_tcp_in

netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=135 name=135_udp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=136 name=136_udp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=137 name=137_udp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=138 name=138_udp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=139 name=139_udp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=145 name=145_udp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=udp localport=445 name=445_udp_out

netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=135 name=135_tcp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=136 name=136_tcp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=137 name=137_tcp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=138 name=138_tcp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=139 name=139_tcp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=145 name=145_tcp_out
netsh advfirewall firewall add rule action=allow dir=out protocol=tcp localport=445 name=445_tcp_out
@echo off
net use K: /delete
rem net use I: /delete
rem net use X: /delete
rem net use L: /delete
net use M: /delete
net use O: /delete
net use P: /delete
net use W: /delete
net use Q: /delete
rem net use R: /delete
rem net use T: /delete
rem net use U: /delete
net use Y: /delete
net use X: /delete

net use K: \\192.168.1.3\C blackid /user:root
rem net use I: \\192.168.1.3\install /user:root
rem net use X: \\192.168.1.3\E /user:root
rem net use L: \\192.168.1.4\licface_profile /user:licface
net use M: \\192.168.1.3\music
net use N: \\192.168.1.3\film3
rem net use K: \\192.168.1.3\film3 /user:root
rem net use S: \\192.168.1.3\film4 /user:root
net use O: \\192.168.1.3\film4
net use Q: \\192.168.1.3\pythonmodules2 
net use X: \\192.168.1.3\E 
rem net use T: \\192.168.1.3\pandora /user:root
net use W: \\192.168.1.4\www blackid /user:licface
net use P: \\192.168.1.4\projects /user:licface 
net use Y: \\192.168.1.5\www blackid /user:licface

import os
pid = os.getpid()
print "PID =", pid
import sys
from make_colors import make_colors
import subprocess

GIT_BIN = r''
if GIT_BIN == r'':
	GIT_BIN = 'git.exe'
	
def notify(message, event, app = 'Git Control', title = 'Git Control', icon = None, host = None, port = 23053, timeout = 5):
	import traceback
	if not icon:
		icon = os.path.join(os.path.dirname(__file__), 'gitdate.png')
	try:
		import sendgrowl
		growl = sendgrowl.growl()
		if isinstance(host, list):
			for i in host:
				if ":" in i:
					host, port = str(i).strip().split(":")
					port = int(port)
				growl.publish(app, event, title, message, timeout= timeout, iconpath= icon, host = host, port = port)
		else:
			growl.publish(app, event, title, message, timeout= timeout, iconpath= icon)
	except:
		traceback.format_exc(print_msg= False)
	try:
		import PySnarl
		PySnarl.snShowMessage(title, message, timeout= timeout, iconPath= icon)
	except:
		traceback.format_exc(print_msg= False)

def checkRemote():
	a = os.popen(GIT_BIN + " remote -v").readline()
	# print "len(a) =", len(a)
	if len(a) < 1:
		q = raw_input(make_colors('git remote origin (URL): ', 'white', 'red'))
		if len(q) == 0:
			print make_colors("Please Add remote git url (origin) first !", 'white', 'red')
			print make_colors("EXIT!", 'white', 'red')
			sys.exit(0)
		else:
			print make_colors('add remote origin: ', 'lightgreen', color_type= 'colorama') + make_colors('%s' % str(q), 'lightmagenta', color_type= 'colorama') + make_colors(' .....', 'lightcyan', 'colorama')
			remote_add = subprocess.Popen([GIT_BIN, 'remote', 'add', 'origin', '%s' %(str(q))], stdout = subprocess.PIPE, shell= True)
			(remote_add_out, remote_add_err) = remote_add.communicate()
			print make_colors(remote_add_out, 'lightyellow', 'colorama')
			notify('Add remote origin: %s' % str(q), 'Add Remote', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
			while 1:
				if remote_add.poll() == 0:
					break
				else:
					sys.stdout.write(".")
			print make_colors("PUSH to: ", 'white', 'red') +  make_colors("%s" % str(q), 'yellow', '', ['blink'], 'termcolor')
			push = subprocess.Popen([GIT_BIN, "push", "origin", "master"], stdout = subprocess.PIPE, shell= True)
			(push_out, push_err) = push.communicate()
			print make_colors(push_out, 'lightcyan', '', color_type= 'colorama')
			#os.system(GIT_BIN + " push origin master")
			notify('Push to remote origin: %s' % str(q), 'PUSH', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
			while 1:
				if push.poll() == 0 or push.poll() == 1 or push.poll() == 128:
					break
				else:
					sys.stdout.write(".")				
	else:
		b = os.popen(GIT_BIN + " remote get-url origin").read()[:-1]
		#print make_colors("PUSH to: ", 'white', 'red', ['blink'], 'termcolor') + make_colors("%s" % str(b), 'red', 'yellow', ['bold'], 'termcolor')
		#os.system(GIT_BIN + " push origin master")
		#notify('Push to remote origin: %s' % str(b), 'PUSH', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
		
		print make_colors("PUSH to: ", 'white', 'red') +  make_colors("%s" % str(b), 'yellow', '', ['blink'], 'termcolor')
		push = subprocess.Popen([GIT_BIN, "push", "origin", "master"], stdout = subprocess.PIPE, shell= True)
		(push_out, push_err) = push.communicate()
		print make_colors(push_out, 'lightcyan', color_type= 'colorama')
		#os.system(GIT_BIN + " push origin master")
		notify('Push to remote origin: %s' % str(b), 'PUSH', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
		while 1:
			if push.poll() == 0 or push.poll() == 1 or push.poll() == 128:
				break
			else:
				sys.stdout.write(".")			
			
def commit(no_push = False):
	import datetime
	comment = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S:%f')
	TAG = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%H-%M-%S-%f')
	if not os.path.isfile(os.path.join(os.getcwd(), '.gitignore')):
		print make_colors('add .gitignore', 'lightyellow', color_type= 'colorama') + make_colors(' .....', 'lightcyan', 'colorama')
		f = open(os.path.join(os.getcwd(), '.gitignore'), 'w')
		f.write("*.pyc\n*.zip\n*.rar\n*.7z\n*.mp3\n*.wav\n")
		f.close()
	
	print make_colors('add file to index', 'lightyellow', color_type= 'colorama') + make_colors(' .....', 'lightcyan', 'colorama')
	add = subprocess.Popen([GIT_BIN, "add", "-A", '.'], stdout = subprocess.PIPE, shell= True)
	(add_out, add_err) = add.communicate()
	print make_colors(add_out, 'red', 'yellow', ['bold'])
	notify("Add file to index", 'Add File', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
	while 1:
		if add.poll() == 0:
			break
		else:
			#print tag.poll()
			sys.stdout.write(".")
	print make_colors('Commit', 'lightmagenta', color_type= 'colorama') + make_colors(' .....', 'lightcyan', 'colorama')
	commit = subprocess.Popen([GIT_BIN, "commit", "-a", "-m", '%s' % comment], stdout = subprocess.PIPE, shell= True)
	(commit_out, commit_err) = commit.communicate()
	print make_colors(str(commit_out), 'lightcyan', 'colorama')
	notify("Commit", 'Commit', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
	while 1:
		if commit.poll() == 0 or commit.poll() == 1:
			break
		else:
			sys.stdout.write(".")	
	print make_colors("Add Tag: ", "lightyellow", color_type= 'colorama') + make_colors("%s" % TAG, "lightgreen", color_type= 'colorama') + make_colors(' .....', 'lightcyan', 'colorama')
	tag = subprocess.Popen([GIT_BIN, "tag", '%s'%str(TAG)], stdout= subprocess.PIPE, shell= True)
	(tag_out, tag_err) = tag.communicate()
	print make_colors(tag_out, 'white', 'cyan')
	notify("Add tag", 'Add Tag', host = ['127.0.0.1:23053', '192.168.1.2:23053'])
	while 1:
		if tag.poll() == 0:
			break
		else:
			sys.stdout.write(".")
	if no_push:
		return
	else:
		checkRemote()
		return

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == '--no-push':
			commit(no_push = True)
		else:
			commit()		
	else:
		commit()
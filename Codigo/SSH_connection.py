import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.8',port=22,username='marlon',password='admin')
stdin,stdout,stderr=ssh.exec_command('show ip interface brief')
output=stdout.readlines()
type(output)
print('\n'.join(output))
## paramiko 모듈을 사용하여 python에서 ssh 연결 후 command 실행시키기  

### exec_command(cmd)

```
import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ip, username, password)

stdin, stdout, stderr = ssh_client.exec_command(cmd)
stdin.flush()
print stdout.read()
```
- 간단한 명령어를 실행하는 경우 사용
- 매 명령어마다 새로운 세션이 부여되므로 연속적인 작업 진행이 불가능

### invoke_shell()
- 세션을 유지한 상태로 명령어 실행이 가능
- channel을 가져오고 channel을 계속 유지해야 한다

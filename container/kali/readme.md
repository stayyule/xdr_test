# kali-linux-docker 构建帮助文档

## Dockerfile

```
FROM kali_linux_docker:v1.1.0
RUN mkdir -p /opt/apps/secvision
COPY vagent /opt/apps/secvision/vagent
RUN chmod +x /opt/apps/secvision/vagent
WORKDIR /opt/apps/secvision/
ENTRYPOINT ["/opt/apps/secvision/vagent", "-d"]
```

## 构建kali-linux-docker镜像

需要把vagent放置到和Dockerfile同文件夹下。需要把CODE和SERVER_HOST替换。

```
# load image
docker load -i kali_linux_docker.tar

# build docker
docker build -t kali_linux_docker_secvision . 

# run docker
docker run -d --network=host --restart always -e "CODE=xxxxxx" -e "SERVER_HOST=xxxxxx" kali_linux_docker_secvision:latest
```

## 终端执行机器人需要的软件

### 双机终端执行

源机器人

```
masscan
hydra
nmap
metasploit-framework
exploitdb
seclists
Goby
dsniff

nodejs
python2
Python3
lua5.4
lua-socket
gawk
ruby
Perl
nc
```

目标机器人

```
nc
```


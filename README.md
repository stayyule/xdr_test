# 容器安全测试

## 测试环境

- kali * 2
- php-upload
- jsp-upload
- shiro
- rce

### 本地仓库

```shell
docker run -d -p 5000:5000 --name registry registry
```

-  Kali docker agent

```shell
# load kali
docker load < kali_linux_docker.tar
docker images
```
预期结果

    REPOSITORY                                               TAG                       IMAGE ID       CREATED          SIZE
    registry.secvision.cloud:8443/vulpub/kali_linux_docker   v1.1.0                    9edc3f556203   12 days ago      6.03GB

```shell
# build docker
docker build -t 127.0.0.1:5000/secvision/kali:v1.1.0 . 
docker images
```
预期结果

    REPOSITORY                                               TAG                       IMAGE ID       CREATED          SIZE
    127.0.0.1:5000/secvision/kali                            v1.1.0                    060ac8e84beb   33 minutes ago   6.06GB

- Web shell php

```shell
docker load < php-upload.tar
docker tag registry.secvision.cloud:8443/vulhub/upload-labs:v3.0.0 127.0.0.1:5000/secvision/upload-labs:v3.0.0
docker images
```
预期结果

    REPOSITORY                                               TAG                       IMAGE ID       CREATED          SIZE
    127.0.0.1:5000/secvision/upload-labs                     v3.0.0                    37f839ee2a93   4 days ago       472MB
    registry.secvision.cloud:8443/vulhub/upload-labs         v3.0.0                    37f839ee2a93   4 days ago       472MB

- Web shell jsp

```shell
docker load < jsp-upload.tar
docker tag registry.secvision.cloud:8443/vulhub/tomcat:v3.0.0-8.5-jre8 127.0.0.1:5000/secvision/tomcat:v3.0.0-8.5-jre8
docker images
```
预期结果

    REPOSITORY                                               TAG                       IMAGE ID       CREATED          SIZE
    127.0.0.1:5000/secvision/tomcat                          v3.0.0                    84b0c4bdd6ae   2 weeks ago      242MB
    registry.secvision.cloud:8443/vulhub/tomcat              v3.0.0-8.5-jre8           84b0c4bdd6ae   2 weeks ago      242MB

- 内存马

```shell
docker load < shiro.tar
docker tag shiro:v3.0.0-memory 127.0.0.1:5000/secvision/shiro:v3.0.0-memory
```
预期结果

    REPOSITORY                                               TAG                       IMAGE ID       CREATED          SIZE 
    127.0.0.1:5000/secvision/shiro                           v3.0.0                    19fbac1b989c   7 years ago         337MB
    shiro                                                    v3.0.0-memory             19fbac1b989c   7 years ago         337MB

```shell
docker load < javasec-mysql.tar
docker tag registry.secvision.cloud:8443/vulhub/javasec-mysql:v3.0.0 127.0.0.1:5000/secvision/javasec-mysql:v3.0.0
docker load < javasec2.tar
docker tag javasec:v3.0.2 127.0.0.1:5000/secvision/javasec:v3.0.2
```

    REPOSITORY                                               TAG               IMAGE ID       CREATED          SIZE 
    127.0.0.1:5000/secvision/javasec-mysql                   v3.0.0            b56f43cc0060   4 months ago    545MB
    registry.secvision.cloud:8443/vulhub/javasec-mysql       v3.0.0            b56f43cc0060   4 months ago    545MB
    127.0.0.1:5000/secvision/javasec                         v3.0.2            715b53b18464   26 hours ago    729MB
    javasec                                                  v3.0.2            715b53b18464   26 hours ago    729MB

- push

```shell
docker push 127.0.0.1:5000/secvision/kali:v1.1.0
docker push 127.0.0.1:5000/secvision/upload-labs:v3.0.0
docker push 127.0.0.1:5000/secvision/tomcat:v3.0.0-8.5-jre8
docker push 127.0.0.1:5000/secvision/shiro:v3.0.0-memory
docker push 127.0.0.1:5000/secvision/javasec-mysql:v3.0.0
docker push 127.0.0.1:5000/secvision/javasec:v3.0.2
curl localhost:5000/v2/_catalog
```
预期结果

    {"repositories":["secvision/javasec","secvision/javasec-mysql","secvision/kali","secvision/shiro","secvision/tomcat","secvision/upload-labs"]}
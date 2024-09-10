# 环境设置

## Node 节点

配置私有仓库

```shell
vi /etc/docker/daemon.json
```

    # daemon.json
    { "insecure-registries" : [ "registry.secvision.cloud:8443" ] }
 
```shell
systemctl restart docker
```


查看镜像，所有容器都是在节点上拉取的，master上没有镜像

```shell
docker images
```

## Master 节点

### 验证机器人

修改 `custom_config_#.yaml` 文件中的 `code` 和 `server` 地址

```yaml
# custom_config_#.yaml

  verify-src-code: XXXX-XXXX-XXXX
  verify-dst-code: XXXX-XXXX-XXXX
  verify-shell-code: XXXX-XXXX-XXXX
  secvision-server: 192.168.1.100
```

修改厂商列表，运行 `secvision_gen.py` 生成验证机器人配置

```python
# secvision_gen.py
vendor_list = ['vendor1', 'vendor2', 'vendor3', 'vendor4']
```

预期结果：

    secvision_vendor1_config.yaml
    secvision_vendor2_config.yaml
    secvision_vendor3_config.yaml
    secvision_vendor4_config.yaml

上传 `*_config.yaml` 到master节点，顺序执行以下命令

```shell
kubectl apply -f custom_config_1.yaml           # 验证机器人 code,server
kubectl apply -f secvision_vendor1_config.yaml  # 验证机器人
```

查看验证机器人 POD,SVC

```shell
kubectl get po,svc -o wide -n secvision
```

### 日志网关

修改 `syslog_gen.py` 文件中的 `code_list` 和 `vendor_list` 地址，列表长度需要一致

```python
# syslog_gen.py
vendor_list = ['vendor1', 'vendor2', 'vendor3', 'vendor4']
code_list = ['XXXX-XXXX-XXXX', 'XXXX-XXXX-XXXX', 'XXXX-XXXX-XXXX', 'XXXX-XXXX-XXXX']
```

预期结果：

    syslog_vendor1_config.yaml
    syslog_vendor2_config.yaml
    syslog_vendor3_config.yaml
    syslog_vendor4_config.yaml

上传 `*_config.yaml` 到master节点，顺序执行以下命令

```shell
kubectl apply -f syslog_vendor1_config.yaml
```

### Webshell 上传

```shell
kubectl apply -f secvision_config.yaml
```

### 内存马

内存码每次执行完后需要删除重新生成 POD

- 新建

```shell
kubectl apply -f shiro.yaml
```

- 删除

```shell
kubectl delete -f shiro.yaml
```

### 资产识别

```shell
kubectl apply -f test_config.yaml
```

查看资源创建情况及POD、service IP分配

```shell
kubectl get po,svc -o wide 
```

查看POD、service 对应的测试用例

```shell
kubectl get po,svc -l test=4-5 --show-labels
```

### 病毒及Webshell镜像扫描

```shell
kubectl apply -f scan_config.yaml
```

镜像扫描不需要查看pod，只需要拉取镜像即可，pod创建成功后删除，镜像在节点上查看

删除pod及service
```shell
kubectl delete -f scan_config.yaml
```

### 性能

运行 `perf_gen.py` 生成配置 `perf_config.yaml`，上传至master后运行以下代码

```shell
kubectl apply -f perf_config.yaml
```
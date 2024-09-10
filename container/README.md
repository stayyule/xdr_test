# 环境设置

## master

### POD/SVC

上传 `*_config.yaml` 到master节点，顺序执行以下命令

- 验证机器人

```shell
kubectl apply -f custom_config_{vendor}.yaml
kubectl apply -f secvision_config.yaml
```

- 查看验证机器人POD

```shell
kubectl get po,svc -o wide -n secvision
```

- 资产识别

```shell
kubectl apply -f test_config.yaml
```

- 查看资源创建情况及POD、service IP分配

```shell
kubectl get po,svc -o wide 
```

- 查看POD、service 对应的测试用例

```shell
kubectl get po,svc -l test=4-5 --show-labels
```

### 病毒及Webshell镜像扫描

```shell
kubectl apply -f scan_config.yaml
```

镜像扫描不需要查看pod，只需要拉取镜像即可，pod创建成功后删除，镜像在节点上查看

```shell
kubectl delete -f scan_config.yaml
```

### 入侵防御

```shell
kubectl apply -f secvision_config.yaml
```

### 内存马

```shell
kubectl apply -f shiro.yaml
```

### 删除pod及service
```shell
kubectl delete -f XXX.yaml
```

## 节点

查看镜像，所有容器都是在节点上拉取的，master上没有镜像

```shell
docker images
```

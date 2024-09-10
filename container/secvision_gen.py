vendor_list = ['qax', 'yxzw', 'lm', 'qty']
print(f'vendors: {vendor_list}')
yaml_txt = ''
for vendor in vendor_list:

    template_str = f"""   
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    vendor: secvision
    app: kali
    role: verify-src
  name: verify-src-pod
  namespace: secvision
spec:
  containers:
  - image: 172.28.236.251:5000/secvision/kali:3.15
    name: {vendor}-verify-src-pod
    env:
    - name: CODE
      valueFrom:
        configMapKeyRef:
          name: secvision-cm
          key: verify-src-code
    - name: SERVER_HOST
      valueFrom:
        configMapKeyRef:
          name: secvision-cm
          key: secvision-server
  dnsPolicy: ClusterFirst
  restartPolicy: Always
---

"""
    yaml_txt += template_str

# print(yaml_txt)

    with open(f'secvision_{vendor}_config.yaml', 'w+') as fr:
        fr.write(yaml_txt)

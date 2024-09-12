vendor_list = ['qax', 'yxzw', 'lm', 'qty']
agent_list = ['src', 'dst', 'shell']
print(f'vendors: {vendor_list}')

for vendor in vendor_list:
    yaml_txt = ''
    for agent in agent_list:
        template_str = f"""   
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    vendor: secvision
    app: kali
    role: verify-{agent}
  name: {vendor}-verify-{agent}-pod
  namespace: secvision
spec:
  containers:
  - image: 172.28.236.251:5000/secvision/kali:xch
    name: {vendor}-verify-{agent}-pod
    env:
    - name: CODE
      valueFrom:
        configMapKeyRef:
          name: secvision-cm
          key: verify-{agent}-code
    - name: SERVER_HOST
      valueFrom:
        configMapKeyRef:
          name: secvision-cm
          key: secvision-server
  nodeSelector:
    node: test          
  dnsPolicy: ClusterFirst
  restartPolicy: Always
---

"""
        yaml_txt += template_str

    with open(f'secvision_{vendor}_config.yaml', 'w+') as fr:
        fr.write(yaml_txt)

vendor_list = ['qax', 'yxzw', 'lm', 'qty']
code_list = ['L450-G3PQ-UOWG', '1AIZ-RTEU-HBED', 'Y0XX-UC44-TON1', 'QRJX-ATQB-03J4']
print(f'vendors: {vendor_list}')

for vendor, code in zip(vendor_list, code_list):
    yaml_txt = ''

    template_str = f"""   
apiVersion: v1
kind: PersistentVolume
metadata:
  creationTimestamp: null
  name: lgateway-pv
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 100Gi
  hostPath:
    path: /tmp
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  creationTimestamp: null
  name: lgateway
  namespace: secvision
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
  volumeName: lgateway-pv
---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  name: lgateway
  namespace: secvision
spec:
  ports:
  - name: web
    nodePort: 30443
    port: 443
    targetPort: 443
  - name: syslog-tcp
    nodePort: 30513
    protocol: TCP
    port: 514
    targetPort: 514
  - name: syslog-udp
    nodePort: 30514
    protocol: UDP
    port: 514
    targetPort: 514
  - name: socket-tcp
    nodePort: 31513
    protocol: TCP
    port: 1514
    targetPort: 1514
  - name: socket-udp
    nodePort: 31514
    protocol: UDP
    port: 1514
    targetPort: 1514
  - name: syslog-tls
    nodePort: 32514
    protocol: TCP
    port: 6514
    targetPort: 6514
  - name: http-push
    nodePort: 31516
    protocol: TCP
    port: 1516
    targetPort: 1516
  selector:
    app: lgateway
  type: NodePort
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  creationTimestamp: null
  labels:
    app: lgateway
  name: lgateway
  namespace: secvision
spec:
  replicas: 1
  selector:
    matchLabels:
      app: lgateway
  serviceName: ""
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: lgateway
      name: lgateway
      namespace: secvision
    spec:
      containers:
      - args:
        - -c
        - {code}
        - -m
        - 172.28.248.252
        command:
        - ./entrypoint.sh
        env:
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        image: 172.28.236.251:5000/secvision/lgateway:4.25
        imagePullPolicy: IfNotPresent
        name: lgateway
        ports:
        - containerPort: 443
          name: web
        - containerPort: 514
          name: syslog-tcp
          protocol: TCP
        - containerPort: 514
          name: syslog-udp
          protocol: UDP
        - containerPort: 1514
          name: socket-tcp
          protocol: TCP
        - containerPort: 1514
          name: socket-udp
          protocol: UDP
        - containerPort: 6514
          name: syslog-tls
          protocol: TCP
        - containerPort: 1516
          name: http-push
          protocol: TCP
        volumeMounts:
        - mountPath: /opt/apps/secvision
          name: lgateway
          subPath: lgateway
      volumes:
      - name: lgateway
        persistentVolumeClaim:
          claimName: lgateway
status:
  availableReplicas: 0
  replicas: 0
---
"""
    yaml_txt += template_str

    with open(f'syslog_{vendor}_config.yaml', 'w+') as fr:
        fr.write(yaml_txt)

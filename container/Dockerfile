FROM registry.secvision.cloud:8443/vulpub/kali_linux_docker:v1.1.0
RUN mkdir -p /opt/apps/secvision
COPY vagent /opt/apps/secvision/vagent
RUN chmod +x /opt/apps/secvision/vagent
WORKDIR /opt/apps/secvision/
ENTRYPOINT ["/opt/apps/secvision/vagent", "-d"]




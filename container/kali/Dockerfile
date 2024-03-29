FROM registry.secvision.cloud:8443/vulpub/kali_linux_docker:v1.1.0
#FROM kali_linux_docker:v1.1.0
RUN mkdir -p /opt/apps/secvision
COPY vagent /opt/apps/secvision/vagent
RUN chmod +x /opt/apps/secvision/vagent
RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
WORKDIR /opt/apps/secvision/
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]


# docker run -d --network=host --restart always -e "CODE=EF4F-AMG3-1YQJ" -e "SERVER_HOST=100000.secvision.cloud" kali_linux_docker_secvision:latest
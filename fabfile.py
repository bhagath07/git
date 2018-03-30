from fabric.api import *

env.hosts=['192.168.1.22']
env.user='vagrant'
env.password='vagrant'

def tomcat():
    sudo("yum install epel-release -y")
    sudo("yum install wget -y")
    sudo("yum update")
    sudo("yum install java -y")
    with cd("~"):
        sudo("wget http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.29/bin/apache-tomcat-8.5.29.tar.gz")
        sudo("mv apache-tomcat-8.5.29.tar.gz /opt/apache-tomcat-8.5.29.tar.gz")
    with cd("/opt/"):
        sudo("tar -xvzf apache-tomcat-8.5.29.tar.gz")
        sudo("sed -i '37 s/<!--/ /g' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i '43 s/-->/ /g' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i 's/role rolename=\"tomcat\"/role rolename=\"manager-script\"/g' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i 's/role rolename=\"role1\"/role rolename=\"manager-gui\"/g' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i 's/user username=\"tomcat\" password=\"<must-be-changed>\" roles=\"tomcat\"/user username=\"tomcat\" password=\"tomcat\" roles=\"manager-script,manager-gui\"/g' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i '/user username=\"role1\" password=\"<must-be-changed>\" roles=\"role1\"/ d' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i '/user username=\"both\" password=\"<must-be-changed>\" roles=\"tomcat,role1\"/ d' /opt/apache-tomcat-8.5.29/conf/tomcat-users.xml")
        sudo("sed -i '19 s/^/<!--/' /opt/apache-tomcat-8.5.29/webapps/manager/META-INF/context.xml")
        sudo("sed -i '21 s/^/-->/' /opt/apache-tomcat-8.5.29/webapps/manager/META-INF/context.xml")
        sudo("service iptables stop")
        sudo("/opt/apache-tomcat-8.5.29/bin/startup.sh")
    


# Syntax to install docker

1. Upgrade the existing packages
    1. sudo yum update -y
2. Install most recent package
    1.  sudo amazon-linux-extras install docker
3. Start the service docker
    1. sudo service docker start
4. Pull cassandra image
    1. sudo docker pull cassandra
5. python3 -c "import cassandra; print (cassandra.__version__)"

Minikube is essentially kubernetes hosted locally. This does not require azure or any cloud service and only 
requires the PC.

Helpful for people getting started and don't want to use cloud credits at the start to conserve resources

prereq: needs docker

Download link: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download 


Using UBUNTU and WSL

Run the following commands in WSL terminal to download:
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

To start:
run command: minikube start









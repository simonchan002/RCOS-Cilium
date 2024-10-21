Run the following commands to install terraform from this website:
https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli 


git clone the RCOS_Cilium repo within WSL Terminal
run: git clone https://github.com/smoleyxd/RCOS-Cilium.git

cd to the RCOS_Cilium Repo 

Also create a file in RCOS_Cilium repository and import the testing.tfvars file in it, it is located in this same folder

3 main terraform commands:

Run in the following order:

1) terraform init -  initializes a working directory and downloads the necessary provider plugins and modules and setting up the backend for storing your infrastructure's state

2) terraform plan - creates an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure. 
    * In some situations, run terraform plan -var-file=testing.tfvars

3) terraform apply - executes the plan and makes the changes that you want in the infrastructure. MAKE SURE TO PLAN FIRST
    * In some situations, run terraform apply -var-file=testing.tfvars


to Destroy the cluster:
terraform destroy -var-file=testing.tfvars


Issues with terraform

https://stackoverflow.com/questions/62314789/no-internet-connection-on-wsl-ubuntu-windows-subsystem-for-linux 
Change to ip of your wifi
Do nslookup to get ip and make it stay for each startup.


Terraform apply (HANGS)
terraform apply -auto-approve
probably a wifi issue
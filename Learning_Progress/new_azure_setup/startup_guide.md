1) Setup your environment: in this case, I am running WSL + Ubuntu on VsCode

2) $curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

3) az account set --subscription "b3a8a44e-e6a7-42e9-bce7-11cd60df8cc9"

4) terraform state pull

5) vim vars.tfvars and put the secrets, obtain this from a coordinator or a team lead.

6) terraform apply -var-file="vars.tfvars"

7) To get access to aks, az aks get-credentials --resource-group RCOS_Cilium --name test-Cilium-aks


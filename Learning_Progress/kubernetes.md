* What is Kubernetes?
    -Manages applications that contain container
    -Works for managing deployment environments (vm, cloud, physical)
    -High availability (low downtime), scalable, data backup
* Need for container orchestration tool
    -Containers have increased usage
* Main Kubernetes components
    -Node: server (virtual or physical)
    -Pod: creates running environment on top of container (typically runs 1 application container). Each pod gets an IP and uses IP to communicate. If server runs out of resources, pod will die and a new one will be reinstated.
    -Service: Static IP address attached to each pod, this is how pods communicate
        -External service to allow access the application/browser
        -Request goes from Ingress (https, not ip)  -> Service (IP)
        -Load Balancer: Forwards request to pods that are less busy
    -Config Map 
        -Configuration data (external) , don’t need to build a new image
    -Secret 
        -Similar to config map, but is secure for storing passwords
    -Environmental variables: Allows for use the data from config map
    -Volumes: persistent storage (external hard drive); USERS have to back up.
    -Deployment: Define a blueprint of a pod and how many pods to replicate. 
    -Databases should be hosted outside of the K8 cluster
* Kubernetes Architecture
    -Master/Slave config
    -Kubelet - interfaces the container runtime and the node. Taking the config and running the pod and the container inside 
    -Kube Proxy: forwards the requests to different pods. 
* Node Process needs 3:
    -Kubelet
    -Kube Proxy
    -Container Runtime
* Master nodes:
    -API server (request <-> cluster)
    -Scheduler: Start the application pod, also determines which new node the pod  should be executed in
    -Controller manager: pods die, reschedule pods and recovers the original cluster state
    -Etcd: Brain of cluster, IMAGE. Changes get stored here. Holds data on cluster state.

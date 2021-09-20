# Kubernetes

## Kubectl + MiniKube

### Command Outputs

- Manually creating the deployment and service:
```
PS C:\Users\aabou> kubectl create deployment my-app --image=aabounegm/devops_app_python
deployment.apps/my-app created
PS C:\Users\aabou> kubectl get deployments
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
my-app   1/1     1            1           106s
PS C:\Users\aabou> kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
my-app-965b4d766-sjqxj   1/1     Running   0          2m5s
PS C:\Users\aabou> kubectl expose deployment my-app --type=LoadBalancer --port=5000
service/my-app exposed
```

- Output of `kubectl get pods,svc` after manually creating a deployment and a service:
```
PS C:\Users\aabou> kubectl get pods,svc
NAME                         READY   STATUS    RESTARTS   AGE
pod/my-app-965b4d766-sjqxj   1/1     Running   0          3m15s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          21m
service/my-app       LoadBalancer   10.111.158.147   <pending>     5000:31133/TCP   29s
```

- After using configuration files and creating 3 replicas:
```
PS C:\Users\aabou> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-59fdf85d9b-fxc7r   1/1     Running   0          17s
pod/app-python-59fdf85d9b-rlplm   1/1     Running   0          14s
pod/app-python-59fdf85d9b-xqsxt   1/1     Running   0          21s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.104.19.136   <pending>     5000:31959/TCP   95s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          31m
```

### Terminology

- **Ingress**: A Kubernetes object that describes how to route external traffic to a service. It can also perform health checks and load balancing.
- **Ingress Controller**: A component that manages the creation and deletion of ingress resources.
- **StatefulSet**: A Kubernetes object that manages the deployment and scaling of a group of pods and services. It is useful for running a group of pods that share common configuration or state.
- **DaemonSet**: A resource that manages the deployment of one or more pods. It ensures that Nodes run a copy of a Pod(s), as well as garbage collection when the nodes are removed.
- **PersistentVolume**: A resource (just like nodes) that has a lifecycle independent of that of the pods which is used to store persistent data.

## Helm

- Output of `minikube service app2-app-python`:

```
PS C:\Users\aabou> minikube service app2-app-python
|-----------|-----------------|-------------|---------------------------|
| NAMESPACE |      NAME       | TARGET PORT |            URL            |
|-----------|-----------------|-------------|---------------------------|
| default   | app2-app-python | http/5000   | http://192.168.49.2:31043 |
|-----------|-----------------|-------------|---------------------------|
🏃  Starting tunnel for service app2-app-python.
|-----------|-----------------|-------------|------------------------|
| NAMESPACE |      NAME       | TARGET PORT |          URL           |
|-----------|-----------------|-------------|------------------------|
| default   | app2-app-python |             | http://127.0.0.1:51771 |
|-----------|-----------------|-------------|------------------------|
🎉  Opening service default/app2-app-python in default browser...
```


- Output of `kubectl get pods,svc` after using helm:
```
PS C:\Users\aabou> kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/app2-app-python-68dd4f65dc-472ns   1/1     Running   0          3m50s
pod/app2-app-python-68dd4f65dc-gmzgd   1/1     Running   0          3m50s
pod/app2-app-python-68dd4f65dc-tplbz   1/1     Running   0          3m50s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app2-app-python   LoadBalancer   10.108.105.40   <pending>     5000:31043/TCP   3m50s
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          82m
```

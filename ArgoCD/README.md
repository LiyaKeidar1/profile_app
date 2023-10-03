# Getting Argocd on Kubernetes
```
 kubectl create namespace argocd
```
```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
This command creates a Cluster IP service. This happens by default so **optional** :
```
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "ClusterIP"}}'
```

	
Now you can see with: 
```
kubectl get svc -n namespace-name (argoocd)
```

the internal port.

```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d
```
Now you receive a password such as: 8gFXTLm9G6GDS15x


    kubectl --namespace argocd port-forward svc/argocd-server 8081:443
	

The port is based on the port I want my computer to contact the service on-- external (8081) : port the service is waiting on-- internal (443).

At this point you can start deploying a database of your own (see the database directory for more info), and a python app.

# Cleanup

From command line:
```
kubectl delete all --all -n argocd
```


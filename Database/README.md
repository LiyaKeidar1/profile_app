## Get mongodb using Argocd
```
kubectl create namespace mongodb
```
Go to ArgoCD GUI (localhost:8081)
	
- [ ] **+** APP
- [ ]   Add name, on default project
- [ ]   Choose automatic sync policy with self heal

		
- [ ] Paste the mongodb helm in the repository URL box:
    ```
    https://marketplace.azurecr.io/helm/v1/repo
    ```

- [ ] Choose the desired namespace, in this case: mongodb	

## Cleanup

- [ ] Remove from command line (make sure docker daemon is running):
```
kubectl delete all --all -n mongodb
```

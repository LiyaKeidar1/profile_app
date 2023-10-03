# Jenkins Installation
1. **Downloading helm**
		
		[ $(uname -m) = x86_64 ] && sudo curl -Lo get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
	 
		sudo chmod 700 get_helm.sh
	 
		sudo ./get_helm.sh
	 
2. **Adding jenkins chart repo:**
	
	 Adding a chart that uploads jenkins image:
	
		helm repo add jenkins1 https://charts.jenkins.io
	 
		helm repo update
	 
	 
3. **Deploying a simple Jenkins instance:**

	 create a value.yaml

		helm install myjenkins jenkins/jenkins -f values.yaml

		kubectl exec --namespace default -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
	 
	 This will return a password for connecting to jenkins with a username "admin"
	 	
		kubectl --namespace default port-forward svc/myjenkins 8080:8080
	 
	 Now, you can find jenkins on **localhost:8080**

# Cleanup

From command line:

	helm uninstall jenkins


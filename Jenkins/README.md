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

# Jenkins Pipeline

1. Open **localhost:8080** and create a new simple pipeline.


2. Connect your pipeline to your github and create a **webhook** on github in the project's settings.
The webhook performs a run of the pipeline every time I push new commits.

- Jenkins looks for a Jenkinsfile and runs on various stages (test, build, push, etc.)
 At the end of the pipeline we should be able to see an **image** and a **helm package** on **dockerhub**.





# Cleanup

From command line:

	helm uninstall jenkins


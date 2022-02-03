# LLA Devops Test

This is a Python application for testing your DevOps abilities.

## Requirementes
 - Visual studio code
 - Python >= 3.10
 - Docker and kubernetes (if you are using Windows or Mac, you can use Docker Desktop)
  - Terraform

## Running application
1. Create a python virtual environment
1. Activate python environment
1. Install dependencies (use requirements.txt file).
1. Use uvicorn for running the application: `uvicorn app.main:app --reload`
1. open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Deliverables
1. You must to fork or clone this project in yout prefference Git platform with sufficiente permissions to check the CI/CD pipeline logs.
1. You add a terraform project to manage your local Kubernetes cluster and schedule the application using a built docker image.
1. You must install a local self-hosted Runner (it is highly recommended to use dockers by creating them with the docker-compose tool) 
    * [gitlab](https://docs.gitlab.com/runner/install/)
    * [github](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)
    * [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=browser)
1. You must create a CI pipeline and run it in every merge request, run the pytests and upload the junit xml report as an artifact.
1. From master branch, create a TAG called **release/1.0.0**
1. Create a CD pipeline to build a docker image from the release tags, upload it to a container registry (you can use the free gitlab or docker hub service), and deploy it to the local Kubernetes cluster.
1. A document describing the CI/CD workflow with screenshots of the diferent results.

## Observations
* You must add the terraform project to the git repository.
* You can change the folder's structure.
* If you have some coding recommendations, you can create a document and add it to the deliverables.  
  


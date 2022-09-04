# Adult_Censes_dataset_Machine_Learning
Ineuron Internship Project with Machine Learning Pipeline full Deployement from Scratch

## Software and Account Requirement:

1. [Github Account](http://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)



Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate adult_cences_dataset/
```
OR 
```
conda activate adult_cences_dataset
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = ismail46h.shaikh@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = adult-cences-dataset

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

To stop docker conatiner
```
docker stop <container_id>
```

installing requiremnts.txt file using setup.py file
```
python setup.py install
```

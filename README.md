# **Postgres API**
![database with api](img/apipostgres.png)

### **Description**

In this project, an *API* was built in order to construct a database with registers about the likes about movies of the user. The latter can insert his/her favorite author, a brief description and the release date. Besides, he / she can update the database in any part of it and finally, he/she would be able to access it to make comparison with another register.

### **Table of Contents**

- [Contents](#contents)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
- [How to use the project](#how-to-use-the-project)
- [Contributions](#contributions)
- [Credits](#credits)
- [Licence](#licence)

### **Contents**

1. main.py
2. models.py
3. routes.py
4. controllers/movies_controllers.py
5. Dockerfile
6. requirements.txt
7. .gitignore
   
You can access the whole repository here...

### How to Install and Run the Project

![docker](img/dockerimage.png)

The database must be put in a container through Docker. The basic steps must be put in an environment where Docker is installed and in the cmd or PowerShell (Windows). These are just two:

1. docker pull postgres
2. docker run --name <your_name_container> -e POSTGRES_PASSWORD = <your_password> -p <your_port>:<docker´s port> -d <name_image>

### **How to use the project**

You are totally free to upload any sort of movies. You just need to use the proper methods established in the code. The interaction with the api will be performed by the browser.


### **Contributions**

I would like to you to encourage to contribute in any form to the project through this public repository. 

### **Credits**

I would like to thank all the members of my team. Besides, I want to thank the support given by the team of Datapath. 

### **Licence**

*GPL* Licence

![the end](img/image-2.png)
 

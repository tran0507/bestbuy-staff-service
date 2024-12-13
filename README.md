# BestBuy Staff Service

## A. Overview

The **BestBuy Staff Service** is a simple RESTful microservice that allows managing staff information for Best Buy's internal system. This service supports **CRUD** operations (Create, Read, Update, Delete) for staff data. The service is designed as a containerized application running on **Azure Kubernetes Service (AKS)**.

### Staff Information:

- **ID**: Unique identifier for each staff member.
- **Name**: Full name of the staff member.
- **Position**: Role of the staff member.
- **Department**: The department where the staff member works.
- **Email**: Contact email.
- **Phone**: Contact phone number.

## B. How to Use the Microservice

The staff-service exposes the following **REST API endpoints** to perform CRUD operations:

### 1. **Create a Staff Member (POST)**

- **Endpoint**: `POST /staff`
- **Request Body**: 
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "position": "Manager",
    "department": "Sales",
    "email": "johndoe@bestbuy.com",
    "phone": "123-456-7890"
  }

### 2. Get All Staff Members (GET)
Endpoint: GET /staff
Description: Retrieves all staff members.

### 3. Get Staff Member by ID (GET)
Endpoint: GET /staff/{id}
Description: Retrieves a single staff member by their unique id.

### 4. Update a Staff Member (PUT)
Endpoint: PUT /staff/{id}
Request Body:

``` bash 
{
  "name": "John Doe Updated",
  "position": "Senior Manager",
  "department": "Sales",
  "email": "johndoe_updated@bestbuy.com",
  "phone": "123-456-7890"
}
```

### 5. Delete a Staff Member (DELETE)
Endpoint: DELETE /staff/{id}
Description: Deletes a staff member by their unique id


## C. Task Completed 

### 1. Staff-Service Microservice Development:

Created a simple Flask-based REST API to manage staff data.
Implemented CRUD operations for staff information.
Dockerized the Service:

### 2. Created a Dockerfile to containerize the staff-service microservice.
Built and pushed the Docker image to Docker Hub.
Deployed on Azure Kubernetes Service (AKS):

### 3. Created a Kubernetes deployment YAML file to deploy the service on AKS.
Exposed the service using a LoadBalancer.
CI/CD Pipeline Setup:

### 4. onfigured a GitHub Actions CI/CD pipeline to automate the build, test, and deployment of the staff-service.
# Dockerized Text Processing Application

## Project Overview
This project involves creating a **Docker container** that automates **text file processing** using **Python**. The container reads two text files, analyzes word frequency, and logs results while maintaining an optimized image size.

## Technologies Used
- **Docker** (Containerization)
- **Python** (Data Processing)
- **Kubernetes** (Optional - Extra Credit for Orchestration)

---

## Setup Instructions
### Step 1: Install Docker
1. Download and install **Docker Desktop** from [Docker's official website](https://www.docker.com/).
2. Run Docker and ensure it is active.
3. Submit a **screenshot of your running containers**.

### Step 2: Clone the Repository or Transfer Files
If using **GitHub**:
```sh
git clone https://github.com/your-repo/docker-text-processing.git
cd docker-text-processing
```
Otherwise, manually transfer **Dockerfile**, **scripts.py**, and text files to your workspace.

### Step 3: Build the Docker Image
Run the following command to build the image:
```sh
docker build -t text-processor .
```

### Step 4: Run the Docker Container
Execute the following command to run the container and process files:
```sh
docker run --rm text-processor
```
This will execute the script inside the container and print the results to the console.

### Step 5: Verify the Output
1. The script will generate a file **result.txt** inside the container.
2. To inspect the output manually, run:
   ```sh
   docker run --rm text-processor cat /home/data/output/result.txt
   ```

### Step 6: Optimize the Image
Ensure that the final Docker image size is **less than 200MB** using a lightweight base image (`python:3.9-slim`). You can check the image size using:
```sh
docker images
```

### Step 7: Save and Submit Docker Image
1. Save the Docker image as a tar file:
   ```sh
   docker save -o your-email.tar text-processor
   ```
2. Submit the `your-email.tar` file for evaluation.

---

## Extra Credit: Kubernetes Deployment
For extra credit, deploy the container using **Kubernetes**:
1. Apply the Kubernetes deployment file:
   ```sh
   kubectl apply -f kubernetes.yaml
   ```
2. Verify running pods:
   ```sh
   kubectl get pods
   ```
3. Submit the output from:
   ```sh
   kubectl get pods > kube_output.txt; cat kube_output.txt
   ```

---

## Expected Output
After running the container, it should print:
- **Word count per file**
- **Total words in both files**
- **Top 3 most frequent words**
- **Container IP Address**

This output is also stored in `/home/data/output/result.txt` inside the container.

---

## Conclusion
By following this guide, you’ll successfully **build, optimize, and deploy** a Dockerized text processing application with optional Kubernetes orchestration.

🚀 Happy Containerizing!


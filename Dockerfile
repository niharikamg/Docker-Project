# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /home/data

# Copy script and text files
COPY scripts.py IF.txt AlwaysRememberUsThisWay.txt ./

# Run the script on container start
CMD ["python", "scripts.py"]

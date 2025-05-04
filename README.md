# Football Dashboard - NGINX-REVERSE-PROXY

Project based on Docker with automatic SSL, frontend and backend API in Flask.

## Structure

- `frontend/` – HTML + JS
- `backend/` – API Flask
- `reverse-proxy/` – nginx-proxy + Let’s Encrypt

### Running the Backend with Docker

##### Build the Docker Image
```bash
docker build -t backend-image:1.0 .
```
##### Run the Docker Container
```bash
docker run -d -p 5000:5000 --name backend backend-image:1.0
```
###### Accessing the API
```
http://localhost:5000/api/matches
http://localhost:5000/api/teams
```
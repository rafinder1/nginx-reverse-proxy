# Football Dashboard - NGINX-REVERSE-PROXY

Project based on Docker with automatic SSL, frontend and backend API in Flask.

## Structure

- `frontend/` – HTML + JS
- `backend/` – API Flask
- `reverse-proxy/` – nginx-proxy + Let’s Encrypt

### Running system with Docker Compose

##### Run the images
```bash
docker compose up --build -d
```
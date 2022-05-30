FROM ghcr.io/anvilistas/amoni/app-server:latest

COPY /app/requirements.txt ./ 
RUN pip install -r requirements.txt

USER anvil

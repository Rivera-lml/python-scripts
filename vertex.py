# 1️ Autenticación con Google Cloud
gcloud auth application-default login

# 2️ Configurar el proyecto
gcloud config set project TU_PROYECTO_ID

# 3️ Habilitar Vertex AI, BigQuery y Cloud Storage
gcloud services enable aiplatform.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable storage.googleapis.com

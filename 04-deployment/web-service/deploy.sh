# Build docker imaga
docker build -t ride-duration-prediction-service:v1 .

# Run docker image
docker run -it --rm -p 9696:9696 ride-duration-prediction-service:v1 
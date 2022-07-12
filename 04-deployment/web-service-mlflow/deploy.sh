project_name=ride-duration-prediction-service-mlflow:v1

# Export RUN_ID
export RUN_ID='ba1790ad6d544a24a6f092a307359c34'
 
echo DELETING CONTAINER IF EXISTS
docker container rm -f $project_name

echo DELETING IMAGE IF EXISTS 
docker image rm $(docker image ls -q $project_name | uniq)

# Build docker image
docker build -t $project_name --build-arg RUN_ID=$RUN_ID .

# Run docker image
docker run -it --rm -p 9696:9696 $project_name
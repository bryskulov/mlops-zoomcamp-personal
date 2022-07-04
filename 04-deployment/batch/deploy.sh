project_name=batch
 
echo DELETING CONTAINER IF EXISTS
docker container rm -f $project_name

echo DELETING IMAGE IF EXISTS 
docker image rm $(docker image ls -q $project_name | uniq)

echo BUILDING NEW IMAGE 
docker build -t $project_name .

echo RUNNING A CONTAINER
docker run -it --rm $project_name 2021 4
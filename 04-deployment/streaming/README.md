# Scripts used in bash


Running the test

```bash
export PREDICTIONS_STREAM_NAME="ride_predictions"
export RUN_ID="ba1790ad6d544a24a6f092a307359c34"
export TEST_RUN="True"

python test.py
```

Buiding and running the Docker
```bash
docker build -t stream-model-duration:v1 .

Export AWS keys
```
export ***
```

docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="ba1790ad6d544a24a6f092a307359c34" \
    -e TEST_RUN="True" \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    stream-model-duration:v1
```


Creating an ECR repo
```bash
aws ecr create-repository --repository-name duration-model
```


Logging in
```
$(aws ecr get-login --no-include-email)
```


Pushing to ECR
```
REMOTE_URI="326845937160.dkr.ecr.us-east-1.amazonaws.com/duration-model"
REMOTE_TAG="v1"
REMOTE_IMAGE=${REMOTE_URI}:${REMOTE_TAG}

LOCAL_IMAGE="stream-model-duration:v1"
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE}
docker push ${REMOTE_IMAGE}
```
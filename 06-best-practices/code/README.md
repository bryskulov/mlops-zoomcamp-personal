
```bash
docker build -t stream-model-duration:v2 .
```

```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions"\
    -e RUN_ID="ba1790ad6d544a24a6f092a307359c34"\
    -e TEST_RUN="True"\
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}"\
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}"\
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}"\
    stream-model-duration:v2
```
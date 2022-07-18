
Running the test

```bash
export PREDICTIONS_STREAM_NAME="ride_predictions"
export RUN_ID="ba1790ad6d544a24a6f092a307359c34"
export TEST_RUN="True"

python test.py
```

```bash
docker build -t stream-model-duration:v1 .

export AWS_ACCESS_KEY_ID=AKIAUYGMJGYELF5TVPFY
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=us-east-1

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
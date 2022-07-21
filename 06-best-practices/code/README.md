* Bash scripts

** Integration test

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

```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions"\
    -e RUN_ID="ba1790ad6d544a24a6f092a307359c34"\
    -e MODEL_LOCATION="/app/model" \
    -e TEST_RUN="True" \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    -v $(pwd)/model:/app/model \
    stream-model-duration:v2
```

** Kinesis test

```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis list-streams
```

```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis create-stream \
    --stream-name ride_predictions \
    --shard-count 1
```

Formating
``` bash
isort .
black .
pylint --recursive=y .
pytest tests/
```

* Make

Without makefiles:

```
isort .
black .
pylint --recursive=y .
pytest tests/
```

To prepare the project, run

```
make setup
```

if [[ "$*" =~ "pull_data_from_s3" ]]; then
    dvc run -n pull_data_from_s3 \
    -d s3://sent-analysis/reviews.tsv \
    -o ./data/reviews.tsv \
    aws s3 cp s3://sent-analysis/reviews.tsv ./data/reviews.tsv
fi

if [[ "$*" =~ "prepare_data" ]]; then
    dvc run -n prepare_data \
    -d data/reviews.tsv \
    -d prepare_data/__main__.py \
    -o data/train_data.parquet \
    -o data/test_data.parquet \
    docker-compose run sentiment.ml "python -m prepare_data ."
fi

if [[ "$*" =~ "train_model" ]]; then
    dvc run -n train_model \
    -d train/__main__.py \
    -d data/train_data.parquet \
    -o model/lr.model \
    docker-compose run sentiment.ml "python -m train ."
fi

if [[ "$*" =~ "test_model" ]]; then
    dvc run -n test_model \
    -d test/__main__.py \
    -d data/test_data.parquet \
    -d model/lr.model \
    -M metrics/model_performance.json \
    docker-compose run sentiment.ml "python -m test ."
fi

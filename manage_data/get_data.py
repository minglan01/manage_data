"""
get_data.py

Created by jliu on 2018-05-11
"""

import boto3
import os

from pathlib import Path
import pandas as pd

BUCKET_NAME = "jueming-experiment"
S3_KEY_TRAIN = 'alibaba_cloud/conversion_rate_prediction/raw_data/round1_ijcai_18_train_20180301.zip'
S3_KEY_TESTA = 'alibaba_cloud/conversion_rate_prediction/raw_data/round1_ijcai_18_test_a_20180301.zip'
S3_KEY_TESTB = 'alibaba_cloud/conversion_rate_prediction/raw_data/round1_ijcai_18_test_b_20180301.zip'


def is_cached(data_name, cache_dir):
    for i in cache_dir.glob("*.*"):
        if i.name == data_name:
            return True
    return False


home_dir = Path(os.environ["HOME"])
tmp_dir = home_dir / "tmp"
s3 = boto3.resource('s3')


if is_cached(S3_KEY_TRAIN, tmp_dir):
    train_data = pd.read_csv(tmp_dir / "", compression='gzip', header=0, sep=',', quotechar='"')

if tmp_dir.is_dir():
    s3.Bucket(BUCKET_NAME).download_file(S3_KEY_tain, tmp_dir)
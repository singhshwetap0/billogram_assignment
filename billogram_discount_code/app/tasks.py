from celery import shared_task
import pandas as pd
from app.config import FILENAME


@shared_task
def update_csv(row_number, data):
    coupon_df = pd.read_csv(FILENAME, keep_default_na=False)
    print("row:", row_number)
    for k, v in data.items():
        print(k, v)
        coupon_df.at[row_number, k] = v
    coupon_df.to_csv(FILENAME, index=False)

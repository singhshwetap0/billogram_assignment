import random


def coupon_for_brand(brand_code, coupon_count):
    """" This function generate randon coupon codes for a given brand """
    coupon_data = []
    for _ in range(0, coupon_count):
        rand_n = random.randint(1000, 9999)
        total = brand_code + str(rand_n)
        coupon_data.append(total)
    return coupon_data

import os
import csv
import json
import pandas as pd

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.config import BRAND_MAPPING, FILENAME

from app.utility import generate_coupon_code

from app.exception import ValueTooSmallError
from app.tasks import update_csv

coupon_data = []


@method_decorator(csrf_exempt, name='dispatch')
class CouponCodeGeneration(View):

    def post(self, request):
        """"This function generates X no of coupon codes for a given brand

        :param self: instance of the class used to update the status
        :brand name
        :coupon count

        """

        coupon_data = []
        data = json.loads(request.body.decode("utf-8"))
        brand_name = data.get('brand')
        coupon_count = data.get('count')
        if brand_name is not None and coupon_count is not None:
            if coupon_count <= 0:
                raise ValueTooSmallError
            brand_code = BRAND_MAPPING.get(brand_name)
            coupon_code = generate_coupon_code.coupon_for_brand(
                brand_code, coupon_count)
            check_if_file_exists = os.path.isfile(FILENAME)

            for ccode in coupon_code:
                _coupon_data = {
                    "Brand": brand_name,
                    "BrandCode": brand_code,
                    "CouponCode": ccode,
                    "Status": False
                }
                coupon_data.append(_coupon_data)

            with open('brand_coupon.csv', mode='a') as fd:
                fieldnames = ['Brand', 'BrandCode',
                              'CouponCode', 'Status', 'UserID']
                writer = csv.DictWriter(fd, fieldnames=fieldnames)

                if not check_if_file_exists:
                    writer.writeheader()
                writer.writerows(coupon_data)

            fd.close()
            return JsonResponse({"message": "Coupon code has been generated successfully", "status": 201})

    def get(self, request):
        """"This function retrieve coupon code and update the status and user id into file
        :param: user id
        :brand name
        """
        user = request.GET.get('user')
        brand = request.GET.get('brand')

        if not os.path.isfile(FILENAME):
            raise FileNotFoundError

        coupon_pd = pd.read_csv(FILENAME)
        ccode_ind = coupon_pd.loc[(coupon_pd.Brand == brand)
                                  & (coupon_pd.Status == False)]
        coupon_code = ""
        if not ccode_ind.empty:
            ind = ccode_ind.index[ccode_ind["Status"] == False].tolist()[
                0]
            tmp_pd = ccode_ind.iloc[0]
            coupon_code = str(tmp_pd.CouponCode)
            d = {'Status': True, 'UserID': user}
            update_csv.apply_async((ind, d), countdown=10)
            return JsonResponse({"coupon_code": coupon_code, "status": 200})

        else:
            return JsonResponse({"message": "No Coupon code available", "coupon_code": coupon_code, "status": 200})

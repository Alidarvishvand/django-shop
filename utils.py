from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('56634E63794A4D4B4C465372734C6F2B577046514959622B306B714A316867617931502F335830316252553D')
        params = {
        'sender': '',
        'receptor': '',
        'message': f'{code}کد تاییدیه',
    } 
        response = api.sms_send(params)
        print (response)
    except APIException as e: 
            print(e)
    except HTTPException as e: 
            print(e)

class isAdminUserMixin(UserPassesTestMixin):
      def test_func(self):
            return self.request.user.is_authenticated and self.request.user.is_admin

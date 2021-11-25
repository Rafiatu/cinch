from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from lib.lower_strip import strip_and_lower
from api.lib.response import Response
from app.emails.send_otp import SendOTP
from app.emails.otp_verification import VerifyEmailVerify
from app.phone.send_phone_otp import PhoneOtpAction


class OtpsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def send(self, request, otp=None):
        email = strip_and_lower(request.data.get('email', ''))
        
        otp = SendOTP.call(email=email, otp=otp)

        if otp.value:
            return Response(data={"otp": otp.value}, status=status.HTTP_201_CREATED)
        else:
            return Response(errors=dict(errors={"error": otp.error.value}), status=status.HTTP_400_BAD_REQUEST)
            
    @action(methods=['post'], detail=False)
    def verify(self, request):
        email = strip_and_lower(request.data.get('email', ''))
        otp_code = request.data.get('otp_code', '')

        verify_email = VerifyEmailVerify.call(email=email, otp=otp_code)

        if verify_email.failed:
            return Response(
                errors=dict(errors=verify_email.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data=verify_email.value)

    @action(methods=['post'], detail=False, url_path='send/phone')
    def send_sms(self, request, otp=None):
        data = request.data

        send_otp = PhoneOtpAction.call(otp=otp, data=data)

        if send_otp.failed:
            return Response(errors=dict(errors=send_otp.error.value), status=status.HTTP_400_BAD_REQUEST)

        return Response(data=send_otp.value, status=status.HTTP_200_OK)

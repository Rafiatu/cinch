from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.lib.response import Response
from payment.get_bank_list import BankList


class BankListViewSet(ViewSet):
    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated], url_path='*')
    def get_bank_list(self, request):
        banks = BankList.call()
        return Response({'banks':banks.value}, status=status.HTTP_200_OK)
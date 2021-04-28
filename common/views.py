from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from zeep import Client


class TipoCambioView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        wsdl = "http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?wsdl"
        client = Client(wsdl)
        response = client.service.TipoCambioDia()
        return Response(response['CambioDolar']['VarDolar'][0]['referencia'])


class GetGroups(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        groups = request.user.groups.values_list('name', flat=True)  # QuerySet Object
        return Response(list(groups))

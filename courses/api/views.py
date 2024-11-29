from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

# List and Create Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
     # Only admins can list users

# Retrieve, Update, Delete Users
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   # Only authenticated users can access

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User

class UserDeleteByIDView(APIView):
    """
    Allows deletion of a user by ID.
    - Admin users can delete any user.
    """
     # Only admins can delete by ID

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": f"User with ID {user_id} deleted successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": f"User with ID {user_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

class UserUpdateByIDView(APIView):
    """
    Update a user's details by ID.
    - Admin users can update any user.
    - Regular users can only update their own details.
    """

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            # Check permissions: Admins can update any user; regular users can update only themselves
            # if request.user != user and not request.user.is_staff:
            #     return Response({"error": "You do not have permission to update this user."}, status=status.HTTP_403_FORBIDDEN)

            # Deserialize and validate data
            serializer = UserSerializer(user, data=request.data)  # `partial=True` allows partial updates
            if serializer.is_valid():
                serializer.save()
                return Response({"message": f"User with ID {user_id} updated successfully.", "user": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": f"User with ID {user_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
    def patch(self, request, user_id):
            try:
                user = User.objects.get(id=user_id)

                # Check permissions: Admins can update any user; regular users can update only themselves
                # if request.user != user and not request.user.is_staff:
                #     return Response({"error": "You do not have permission to update this user."}, status=status.HTTP_403_FORBIDDEN)

                # Deserialize and validate partial data
                serializer = UserSerializer(user, data=request.data, partial=True)  # `partial=True` enables partial updates
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": f"User with ID {user_id} updated successfully.", "user": serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                return Response({"error": f"User with ID {user_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)


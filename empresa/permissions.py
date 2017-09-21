from rest_framework import permissions

class IsOnwerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      if obj.funcionario.user == request.user:
        if request.method == 'DELETE':
          return True
      return False


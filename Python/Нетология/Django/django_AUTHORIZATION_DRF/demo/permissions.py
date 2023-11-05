from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    # имеет ли пользователь право на работу с ресурсом
    # мы этот метод менять не будем
    # def has_permission(self, request, view):
    #    pass

    # имеет ли пользователь на взаимодействие с объектом
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.user

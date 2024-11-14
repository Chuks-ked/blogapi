from rest_framework import permissions



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and 
            obj.author == request.user
        )


# class IsAuthorOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#     # Authenticated users only can see list view
#         if request.user.is_authenticated:
#             return True
#         return False
#     def has_object_permission(self, request, view, obj):
#     # Read permissions are allowed to any request so we'll always
#     # allow GET, HEAD, or OPTIONS requests
#         if request.method in permissions.SAFE_METHODS:
#             return True
#             # Write permissions are only allowed to the author of a post
#         return obj.author == request.user
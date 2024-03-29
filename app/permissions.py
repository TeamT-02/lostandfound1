from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina ko'rish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # xulas bir gap bilan admin uchun ruxsat bor
        return obj.author == request.user

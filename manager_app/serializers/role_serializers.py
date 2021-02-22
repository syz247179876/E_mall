# -*- coding: utf-8 -*-
# @Time  : 2021/2/15 下午8:28
# @Author : 司云中
# @File : role_serializers.py
# @Software: Pycharm

from rest_framework import serializers

from universal_app.models import Role


class RoleSerializer(serializers.ModelSerializer):
    """角色序列化器"""

    pid_list = serializers.ListField(child=serializers.CharField(max_length=8), allow_empty=True, write_only=True)

    class Meta:
        model = Role
        fields = ('pk', 'role_name', 'description', 'pid_list', 'rid')
        read_only_fields = ('pk',)

    def add_role(self):
        """添加角色信息"""
        credential = self.get_credential
        pid_list = self.validated_data.pop('pid_list')
        role = self.Meta.model.objects.create(**credential)
        role.permission.add(*pid_list)

    def modify_role(self):
        """修改角色信息"""
        credential = self.get_credential
        pk = self.validated_data.pop('pk')
        permission_list = self.validated_data.pop('permission')
        role = self.Meta.model.objects.filter(pk=pk).update(**credential)
        role.set(permission_list)

    @property
    def get_credential(self):
        return {
            'role_name': self.validated_data.pop('role_name'),
            'description': self.validated_data.pop('description'),
        }


class RoleDeleteSerializer(serializers.Serializer):
    pk_list = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)
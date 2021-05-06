# -*- coding: utf-8 -*-
# @Time : 2020/5/8 18:37
# @Author : 司云中
# @File : response_code.py
# @Software: PyCharm

"""
自定义业务逻辑Code
"""

# 1.验证码验证成功
VERIFICATION_CODE_SUCCESS = 1001

# 2.登录成功
LOGIN_VERIFICATION_SUCCESS = 1002

# 3.注册成功
REGISTER_VERIFICATION_SUCCESS = 1003

# 4.邮件验证成功
EMAIL_VERIFICATION_SUCCESS = 1004

# 5.手机号验证成功
PHONE_VERIFICATION_SUCCESS = 1005

# 6.找回密码验证成功
FIND_PASSWORD_VERIFICATION_SUCCESS = 1006

# 7.修改密码验证成功
MODIFY_PASSWORD_VERIFICATION_SUCCESS = 1007

# 8.保存用户信息成功
USER_INFOR_CHANGE_SUCCESS = 1008

# 9.绑定手机成功
BIND_SUCCESS = 1009

# 10.认证真实用户成功
VERIFY_ID_CARD_SUCCESS = 1010

# 11.密保设置成功
SECRET_SECURITY_SUCCESS = 1011

# 12.图片实名认证成功
REAL_NAME_AUTHENTICATION_SUCCESS = 1012

# 13.添加收货地址成功
ADD_ADDRESS_SUCCESS = 1013

# 14.修改收获地址成功
MODIFY_ADDRESS_SUCCESS = 1014

# 15.修改默认地址成功
MODIFY_DEFAULT_SUCCESS = 1015

# 16.删除地址成功
DELETE_ADDRESS_SUCCESS = 1016

# 17.修改地址成功
REVISE_ADDRESS_SUCCESS = 1017

# 18.删除订单成功
DELETE_ORDER_SUCCESS = 1018

# 19.删除收藏夹成功
DELETE_FAVORITES_SUCCESS = 1019

# 20.添加收藏夹成功
ADD_FAVORITES_SUCCESS = 1020

# 21.添加足迹成功
ADD_FOOT_SUCCESS = 1021

# 22.删除足迹成功
DELETE_FOOT_SUCCESS = 1022

# 23.删除购物车商品成功
DELETE_SHOP_CART_GOOD_SUCCESS = 1023

# 24.修改购物车商品数量成功
EDIT_SHOP_CART_GOOD_SUCCESS = 1024

# 25.创建订单成功
CREATE_ORDER_SUCCESS = 1025

# 27.添加进购物车成功
ADD_GOOD_INTO_SHOP_CART_SUCCESS = 1027

# 28,创建商家成功

CREATE_SHOPPER_SUCCESS = 1028

# 29.删除评论成功
DELETE_REMARK_SUCCESS = 1029

# 30.修改头像成功
MODIFY_HEAD_IMAGE_SUCCESS = 1030

# 31.评论点赞/差评成功
ADD_ACTION_REMARK_SUCCESS = 1031

# 32.获取优惠卷成功
ACQUIRE_COUPON_SUCCESS = 1032

# 33.获取优惠卷失败
ACQUIRE_COUPON_ERROR = 1033

# 34.修改密码成功
MODIFY_PASSWORD_SUCCESS = 1034

# 35.删除历史记录成功
DELETE_HISTORY_SUCCESS = 1035

# 36.删除角色成功
DELETE_ROLE_SUCCESS = 1036

# 37.修改角色成功
MODIFY_ROLE_SUCCESS = 1037

# 38.修改角色
ADD_ROLE_SUCCESS = 1038

# 39.添加权限
ADD_PERMISSION_SUCCESS = 1039

# 40.添加商品类别
ADD_COMMODITY_CATEGORY = 1040

# 41.删除商品类别
DELETE_COMMODITY_CATEGORY = 1041

# 42.修改商品类别
MODIFY_COMMODITY_CATEGORY = 1042

# 43.添加商品分组
ADD_COMMODITY_GROUP = 1043

# 44.删除商品分组
DELETE_COMMODITY_GROUP = 1044

# 45.修改成功
MODIFY_COMMODITY_GROUP = 1045

# 46.删除权限
DELETE_PERMISSION_SUCCESS = 1046

# 47.修改权限
MODIFY_PERMISSION_SUCCESS = 1047

# 48.创建店铺
CREATE_STORE = 1048

# 49.添加商品规格
ADD_COMMODITY_PROPERTY = 1049

# 50.修改商品规格
MODIFY_COMMODITY_PROPERTY = 1050

# 51.删除商品规格
DELETE_COMMODITY_PROPERTY = 1051

# 52.修改运费模板
MODIFY_COMMODITY_FREIGHT = 1052

# 53.删除运费模板
DELETE_COMMODITY_FREIGHT = 1053

# 54.增加运费模板
ADD_COMMODITY_FREIGHT = 1054

# 55.修改用户角色
MODIFY_USER_ROLE = 1055

# 56.为用户所属角色添加权限
ADD_ROLE_PERMISSION = 1056

# 57.为用户所属角色修改权限
MODIFY_ROLE_PERMISSION = 1057

# 58.为用户所属角色删除权限
DELETE_ROLE_PERMISSION = 1058

# 59.商家添加商品
ADD_COMMODITY = 1059

# 60.商家修改商品
MODIFY_COMMODITY = 1060

# 61.管理员添加轮播图
ADD_CAROUSEL = 1061

# 62.管理员删除轮播图
DELETE_CAROUSEL = 1062

# 63.管理员修改轮播图
MODIFY_CAROUSEL = 1063

# 64.商家添加有效SKU
ADD_EFFECTIVE_SKU = 1064

# 65.商家删除有效SKU
DELETE_EFFECTIVE_SKU = 1065

# 66.商家修改有效SKU
MODIFY_EFFECTIVE_SKU = 1066

# 67.删除购物车中商品记录
DELETE_CART_COMMODITY = 1067

# 68.向购物车中添加商品
ADD_CART_COMMODITY = 1068

# 69.修改购物车中商品信息
MODIFY_CART_COMMODITY = 1069

# 70.验证码发送
VERIFICATION_CODE_SEND = 1070

# 71.注销账户
DISCARD_USER = 1071

# 72.修改店铺信息
MODIFY_SELLER_STORE = 1072


class ResponseCode:

    def result(self, code, msg, **extra):
        result = {
            'code': code,
            'msg': msg,
            'status': 'success'
        }
        result.update(extra)
        return result


response_code = ResponseCode()

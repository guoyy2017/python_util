#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/4.下午3:06
'''

'''
权限管理
'''

import rbac.acl

acl = rbac.acl.Registry()

acl.add_role("member")
acl.add_role("student", ["member"])
acl.add_role("teacher", ["member"])
acl.add_role("junior-student", ["student"])

acl.add_resource("course")
acl.add_resource("senior-course", ["course"])

acl.allow("member", "view", "course")
acl.allow("student", "learn", "course")
acl.allow("teacher", "teach", "course")
acl.deny("junior-student", "learn", "senior-course")

if acl.is_allowed("student", "view", "course"):
    print("Students chould view courses.")
else:
    print("Students chould not view courses.")

if acl.is_allowed("junior-student", "learn", "senior-course"):
    print("Junior students chould learn senior courses.")
else:
    print("Junior students chould not learn senior courses.")

#装饰校验
from rbac.context import IdentityContext, PermissionDenied
context = IdentityContext(acl)

@context.check_permission("edit", "article", message="can not edit")
def test():
    pass

if __name__ == '__main__':
    pass
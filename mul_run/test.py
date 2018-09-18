#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 下午11:35
# @Author  : maidou
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from cubes.tutorial.sql import create_table_from_csv
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(engine,
                      "IBRD_Balance_Sheet__FY2010.csv",
                      table_name="ibrd_balance",
fields=[
("category", "string"),
("category_label", "string"),
("subcategory", "string"),
("subcategory_label", "string"),
("line_item", "string"),
("year", "integer"),
("amount", "integer")],
create_id=True
)

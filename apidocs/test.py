#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/6/24.下午5:10
'''

from flask import Flask,request,jsonify

from flasgger import Swagger
from flasgger.utils import swag_from


app = Flask(__name__)
Swagger(app)

@app.route("/test")
def test():
    """
        This is the language awesomeness API
        Call this api passing a language name and get back its features
        ---
        tags:
          - Awesomeness Language API
        parameters:
          - name: language
            in: path
            type: string
            required: true
            description: The language name
          - name: size
            in: query
            type: integer
            description: size of awesomeness
        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: A language with its awesomeness
            schema:
              id: awesome
              properties:
                language:
                  type: string
                  description: The language name
                  default: Lua
                features:
                  type: array
                  description: The awesomeness list
                  items:
                    type: string
                  default: ["perfect", "simple", "lovely"]

        """
    return jsonify({'name':'nihao'})

if __name__ == '__main__':
    app.run()
    pass
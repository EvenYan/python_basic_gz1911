# -*- coding: utf-8 -*-
import hashlib


def gen_secret(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

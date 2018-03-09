# -*- coding: utf-8 -*
def _init():
    global _global_dict
    _global_dict={}

        
def set_value(key,value):
    _global_dict[key]=value


def add_value(key):
    _global_dict[key]+=1


def dec_value(key):
    _global_dict[key]-=1

    
def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

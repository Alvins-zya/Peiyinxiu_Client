#coding=utf-8
'''
create on 2020年2月21日
@author : Alvin_zhu
'''
import json
import os
import re
def get_conn_device_info():
    device  = os.popen('adb devices')
    out_str = device.read()
    connect_device_id = re.findall(r'(\w+)\s+device\s', out_str)[0]
    # return connectdeviceid
    system_version = os.popen('adb shell getprop ro.build.version.release').read().strip()

    device_info = {
        "device_id": connect_device_id,
        "version":system_version
    }
    return device_info


def get_connect_device_version():
    system_version = os.popen('adb shell getprop ro.build.version.release').read().strip()
    return system_version


def get_connect_device_id():
    device = os.popen('adb devices')
    out_str = device.read()
    connect_device_id = re.findall(r'(\w+)\s+device\s', out_str)[0]
    return connect_device_id


def check_if_exist_in_config(connecting_device_id):
    configs_file_name = '/device_infos.json'
    config_infos = ""
    with open(configs_file_name, 'r') as file_obj:
        config_infos = json.load(file_obj)
    for config_info in config_infos:
        if connecting_device_id == config_info['device_id']:
            return config_info['version']
    else:
        return False

def  get_device_info_from_config_file(connecting_device_id):
    device_info =check_if_exist_in_config(connecting_device_id)
    if device_info:
        return device_info
    else:
        configs_file_name = '/device_infos.json'
        device_version = get_connect_device_version
        with open(configs_file_name, 'r') as file_obj:
            config_infos = json.load(file_obj)
        connecting_device_info ={
            "device_id": connecting_device_id,
            "version": device_version
        }
        config_infos.append(connecting_device_info)
        with open(configs_file_name, 'w') as file_obj:
            json.dump(config_infos, configs_file_name)
        return connecting_device_info









if __name__ == '__main__':
    print(get_conn_device_info())
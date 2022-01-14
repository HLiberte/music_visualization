from flask import Flask
import json
from flask_cors import CORS
from Analysis import AnalysisNet

app = Flask(__name__)
CORS(app)

"""
top10
"""
@app.route("/get_max_play", methods=["GET"])
def check():
    res_max_play_name, res_max_play_value = analysis_net.get_play_max()
    return_data = {'name': res_max_play_name, 'value': res_max_play_value}
    return json.dumps(return_data, ensure_ascii=False)

"""
每个月创建歌单的数量
"""
@app.route("/get_per_create", methods=["GET"])
def check_1():
    data, value = analysis_net.get_per_month_create()
    return_data = {'data': data, 'value': value}
    return json.dumps(return_data, ensure_ascii=False)

"""
词云图
"""
@app.route("/get_max_author", methods=["GET"])
def check_2():
    return_data = analysis_net.get_max_author(50)  
    return_data_dict = [{'name': k, 'value': v} for k, v in return_data[0].items()]
    return_data = {'data': return_data_dict}
    return json.dumps(return_data, ensure_ascii=False)

"""
饼图
"""
@app.route("/get_rose", methods=["GET"])
def check_3():
    name, return_data_1 = analysis_net.rose_img()
    return_data = {'name': name, 'return_data': return_data_1}
    return json.dumps(return_data, ensure_ascii=False)

"""
评论和转发量的结合图
"""
@app.route("/get_stack_img", methods=["GET"])
def check_4():
    transfrom_value, pinglun_value, zuhe_name = analysis_net.stack_img()
    return_data = {'transfrom_value': transfrom_value, 'pinglun_value': pinglun_value, 'zuhe_name': zuhe_name}
    return json.dumps(return_data, ensure_ascii=False)

"""
总的转发量 总的歌曲数 等
"""
@app.route("/get_all_num", methods=["GET"])
def check_5():
    return_data = analysis_net.get_all_num()
    return json.dumps(return_data, ensure_ascii=False)


if __name__ == '__main__':
    analysis_net: AnalysisNet = AnalysisNet()
    app.run(debug=True, host='127.0.0.1', port=8080, threaded=True)

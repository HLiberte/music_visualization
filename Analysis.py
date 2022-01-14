import pandas as pd
from sqlalchemy import create_engine


class AnalysisNet(object):
    def __init__(self):
        self.musci_df = None
        self.languageType = {'华语': '华语', '欧美': '欧美', '粤语': '粤语', '日语': '日语', '韩语': '韩语'}
        self.get_df()

    def get_connect(self):
        Con = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format("root", "root", '127.0.0.1', '3306', 'music'), echo=False)
        sql = "select * from music_clear1"
        df = pd.read_sql(sql, con=Con)
        return df

    def get_df(self):
        self.musci_df = self.get_connect()
        self.musci_df.columns = ['序号', '歌单标题', '歌单作者', '日期', '标签', '歌单收藏量', '转发量', '评论数', '歌曲数', '播放量']
        self.musci_df['歌单收藏量'] = self.musci_df['歌单收藏量'].map(lambda x: str(x).replace('万', '0000'))
        self.musci_df['创建歌单数量(本月)'] = 1
        self.musci_df['语种'] = self.musci_df['标签'].map(lambda x: self.resetlanguageType(x))

    def get_play_max(self):
        """
        获得播放量最大的top10
        """
        play_max_df = self.musci_df.sort_values(by="播放量", ascending=False)
        res_max_play_name = [i for i in play_max_df['歌单标题'].values[0:10]]
        res_max_play_value = [int(i) // 10000 for i in play_max_df['播放量'].values[0:10]]
        return res_max_play_name, res_max_play_value

    def stack_img(self):
        """
        评论数 转发量
        """
        transfrom_value = [int(i) for i in self.musci_df['转发量'].values[:20]]
        pinglun_value = [int(i) for i in self.musci_df['评论数'].values[:20]]
        zuhe_name = [i for i in self.musci_df['歌单标题'].values[:20]]
        return transfrom_value, pinglun_value, zuhe_name

    def resetlanguageType(self, x):
        x_split = x.split('-')
        for i in x_split:
            if i in self.languageType.keys():
                return self.languageType[i]
        return '无语种'

    def rose_img(self):
        res2 = self.musci_df['创建歌单数量(本月)'].groupby(self.musci_df['语种']).sum().sort_values(ascending=False)
        return_res2 = []
        for k, v in zip(res2.index, res2.values):
            if k == '无语种':
                continue
            return_res2.append({'value': int(v), 'name': k})
        name = [i for i in self.languageType.keys()]
        return name, return_res2

    def get_max_author(self, num):
        """
        获得创建歌单最多的作者
        """
        test_df = self.musci_df['序号'].groupby(self.musci_df['歌单作者'])
        test = test_df.count().sort_values(ascending=False)[0:num]
        resp_dict = {k: int(v) for k, v in zip(test.index, test.values)}
        name = [i for i in test.index]
        return resp_dict, name

    def get_per_month_create(self):
        """
        每个月创建歌单的数量
        """
        self.musci_df['日期'] = pd.to_datetime(self.musci_df['日期'])
        grouper = pd.Grouper(key='日期', freq='M')
        res1 = self.musci_df.groupby(grouper)['创建歌单数量(本月)'].sum()
        data = [str(i)[:7] for i in res1.index]
        value = [int(i) for i in res1.values]
        return data, value

    """
    总的转发量 总的歌曲数 等
    """
    def get_all_num(self):
        res_dict = {'all_shouchang_num': int(self.musci_df['歌单收藏量'].astype(int).sum()),
                    'all_transform_num': int(self.musci_df['转发量'].astype(int).sum()),
                    'all_pinglun_num': int(self.musci_df['评论数'].astype(int).sum()),
                    'all_music_num': int(self.musci_df['歌曲数'].sum())}
        return res_dict
if __name__ == '__main__':

    test = AnalysisNet()
    data, value = test.get_per_month_create()
    print(data)
    print(value)
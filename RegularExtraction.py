# -*- coding:utf-8*-
import re
from itertools import groupby

class regularExtrator():

    def __init__(self, text):
        self.text = text

    def remove_chinese(self):
        if self.text == "":
            return ""
        pattern = re.compile(u'[\u4E00-\u9FA5]')
        text_without_chinese = pattern.sub(r"", self.text)
        return text_without_chinese

    #email抽取
    def extract_email(self):
        if self.text == "":
            return []
        text_without_chinese = self.remove_chinese()
        text_without_chinese = text_without_chinese.replace(' at ', '@').replace(' dot ', '.')
        sep = ',!?:; ，。！？《》、|\\/'
        eng_split_texts = [''.join(g) for k, g in groupby(text_without_chinese, sep.__contains__) if not k]
        email_pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z_-]+)+$'
        emails = []
        for eng_text in eng_split_texts:
            result = re.match(email_pattern, eng_text, flags=0)
            if result:
                emails.append(result.string)
        return emails

    #电话号码抽取
    def extract_chinese_cellphone(self):
        if self.text == "":
             return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele) >= 7 and len(ele) < 17]
        phone_pattern = r'^((\+86)?([- ])?)?(|(13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9])|(19[0-9]))([- ])?\d{3}([- ])?\d{4}([- ])?\d{4}$'
        phones = []
        for eng_text in eng_split_texts_clean:
            result = re.match(phone_pattern, eng_text, flags=0)
            if result:
                phones.append(result.string.replace('+86', '').replace('-', ''))
        return phones

    #身份证抽取
    def extract_indentity_ids(self):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele) == 18]
        id_pattern = r'^[1-9][0-7]\d{4}((19\d{2}(0[13-9]|1[012])(0[1-9]|[12]\d|30))|(19\d{2}(0[13578]|1[02])31)|(19\d{2}02(0[1-9]|1\d|2[0-8]))|(19([13579][26]|[2468][048]|0[48])0229))\d{3}(\d|X|x)?$'
        phones = []
        for eng_text in eng_split_texts_clean:
            result = re.match(id_pattern, eng_text, flags=0)
            if result:
                phones.append(result.string.replace('+86', '').replace('-', ''))
        return phones

    #ipv4地址抽取
    def extract_ipv4_addresses(self):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele) == 32]
        ip_pattern = r'^(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)$'
        ip_addresses = []
        for eng_text in eng_split_texts_clean:
            result = re.match(ip_pattern, eng_text, flags=0)
            if result:
                ip_addresses.append(result.string)
        return ip_addresses

    #QQ号码抽取
    def extract_QQ_number(self):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele) >= 5 and len(ele) <= 10]
        QQ_pattern = r'^[1-9]([0-9]{5,11})$'
        QQ_numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(QQ_pattern, eng_text, flags=0)
            if result:
                QQ_numbers.append(result.string)
        return QQ_numbers

    #国内固话抽取
    def extract_china_fixed_number(self):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 7 or len(ele) == 8 or len(ele) == 11)]
        fixed_number_pattern = r'^[0-9-()（）]{7,18}$'
        fixed_numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(fixed_number_pattern, eng_text, flags=0)
            if result:
                fixed_numbers.append(result.string)
        return fixed_numbers

    #国内移动电话号码抽取
    def extract_china_mobile_phone_number(self, pattern):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 11 or len(ele) == 13)]
        if pattern == "all":
            pattern = r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[35678]\d{2}|4(?:0\d|1[0-2]|9\d))|9[01356789]\d{2}|66\d{2})\d{6}$'
        elif pattern == "china_mobile":
            pattern = r'^(?:\+?86)?1(?:3(?:4[^9\D]|[5-9]\d)|5[^3-6\D]\d|8[23478]\d|(?:78|98)\d)\d{7}$'
        elif pattern == "china_unicom":
            pattern = r'^(?:\+?86)?1(?:3[0-2]|[578][56]|66)\d{8}$'
        elif pattern == "china_telecom":
            pattern = r'^(?:\+?86)?1(?:3(?:3\d|49)\d|53\d{2}|8[019]\d{2}|7(?:[37]\d{2}|40[0-5])|9[139]\d{2})\d{6}$'
        elif pattern == "inmarsat":#国际海事卫星电话
            pattern = r'^(?:\+?86)?1749\d{7}$'
        elif pattern == "emergency_communications":#紧急电话
            pattern = r'^(?:\+?86)?174(?:0[6-9]|1[0-2])\d{6}$'
        numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(pattern, eng_text, flags=0)
            if result:
                numbers.append(result.string.replace('+86', '').replace('-', ''))
        return numbers

    #虚拟号码
    def extract_china_mvno_number(self, pattern):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 11 or len(ele) == 13)]
        if pattern == "all":
            pattern = r'^(?:\+?86)?1(?:7[01]|6[257])\d{8}$'
        elif pattern == "china_mobile":
            pattern = r'^(?:\+?86)?1(?:65\d|70[356])\d{7}$'
        elif pattern == "china_unicom":
            pattern = r'^(?:\+?86)?1(?:70[4789]|71\d|67\d)\d{7}$'
        elif pattern == "china_telecom":
            pattern = r'^(?:\+?86)?1(?:70[012]|62\d)\d{7}$'
        numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(pattern, eng_text, flags=0)
            if result:
                numbers.append(result.string.replace('+86', '').replace('-', ''))
        return numbers

    #物联网号码
    def extract_china_IoT_number(self, pattern):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 11 or len(ele) == 13)]
        if pattern == "all":
            pattern = r'^(?:\+?86)?14(?:[14]0\d|[68]\d{2})\d{8}$'
        elif pattern == "china_mobile":
            pattern = r'^(?:\+?86)?14(?:40|8\d)\d{9}$'
        elif pattern == "china_unicom":
            pattern = r'^(?:\+?86)?146\d{10}$'
        elif pattern == "china_telecom":
            pattern = r'^(?:\+?86)?1410\d{9}$'
        numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(pattern, eng_text, flags=0)
            if result:
                numbers.append(result.string.replace('+86', '').replace('-', ''))
        return numbers

    #上网卡
    def extract_china_data_only_number(self, pattern):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 11 or len(ele) == 13)]
        if pattern == "all":
            pattern = r'^(?:\+?86)?14[579]\d{8}$'
        elif pattern == "china_mobile":
            pattern = r'^(?:\+?86)?147\d{8}$'
        elif pattern == "china_unicom":
            pattern = r'^(?:\+?86)?145\d{8}$'
        elif pattern == "china_telecom":
            pattern = r'^(?:\+?86)?149\d{8}$'
        numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(pattern, eng_text, flags=0)
            if result:
                numbers.append(result.string.replace('+86', '').replace('-', ''))
        return numbers

    #所有号码
    def extract_all_china_phone_number(self):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 11 or len(ele) == 13)]
        pattern = "^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[01356789]\d{2}|4(?:0\d|1[0-2]|9\d))|9[01356789]\d{2}|6[2567]\d{2}|4(?:[14]0\d{3}|[68]\d{4}|[579]\d{2}))\d{6}$"
        numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(pattern, eng_text, flags=0)
            if result:
                numbers.append(result.string.replace('+86', '').replace('-', ''))
        return numbers

    #所有支持短信功能的号码
    def extract_all_china_phone_number_support_message(self):
        if self.text == '':
            return []
        eng_texts = self.remove_chinese()
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if (len(ele) == 11 or len(ele) == 13)]
        pattern = "^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[01356789]\d{2}|4(?:0\d|1[0-2]|9\d))|9[01356789]\d{2}|6[2567]\d{2}|4[579]\d{2})\d{6}$"
        numbers = []
        for eng_text in eng_split_texts_clean:
            result = re.match(pattern, eng_text, flags=0)
            if result:
                numbers.append(result.string.replace('+86', '').replace('-', ''))
        return numbers




if __name__ == "__main__":
    text = '急寻特朗普，男孩，于2018年11月27号11时在陕西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：18100065143，132-6156-2938，baizhantang@sina.com.cn 和yangyangfuture at gmail dot com'
    ex = regularExtrator(text)
    print("chinese cellphone:")
    print(ex.extract_chinese_cellphone())
    print("email:")
    print(ex.extract_email())
    print("id:")
    print(ex.extract_indentity_ids())
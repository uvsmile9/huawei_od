# -*- coding = utf-8 -*-
# @Time : 2023/4/13 16:28
# @Author : uvsmile9
# @File :HJ18-IP分类统计.py
# @Software : PyCharm

ipClassSum = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'W': 0,
    'P': 0
}


def check_ip(ip: str):
    ip_l = ip.split('.')
    if len(ip_l) != 4 or '' in ip_l:
        return False
    for i in ip_l:
        if int(i) < 0 or int(i) > 255:
            return False
    return True


def check_mask(mask: str):
    if not check_ip(mask):
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        return False
    mask_l = mask.split('.')
    mask_b = []
    for i in mask_l:
        ib = bin(int(i))[2:]
        mask_b.append(ib.zfill(8))
    r_mask = ''.join(mask_b)
    print(r_mask)
    f0_find = r_mask.find("0")
    l1_rfind = r_mask.rfind("1")
    if l1_rfind + 1 == f0_find:
        return True
    else:
        return False


def check_prip(ip: str):
    ip_l = ip.split('.')
    if ip_l[0] == '10': return True
    if ip_l[0] == '172' and 16 <= int(ip_l[1]) <= 31: return True
    if ip_l[0] == '192' and ip_l[1] == '168': return True
    return False


while True:
    try:
        s=input()
        ip = s.split('~')[0]
        mask = s.split('~')[1]
        if check_ip(ip):
            fst = int(ip.split('.')[0])
            if fst == 127 or fst == 0:
                continue
            if check_mask(mask):
                if check_prip(ip):
                    ipClassSum['P'] += 1
                if 0 < fst < 127:
                    ipClassSum['A'] += 1
                elif 127 < fst < 192:
                    ipClassSum['B'] += 1
                elif 191 < fst < 224:
                    ipClassSum['C'] += 1
                elif 223 < fst < 240:
                    ipClassSum['D'] += 1
                elif 239 < fst < 256:
                    ipClassSum['E'] += 1
            else:
                ipClassSum['W'] += 1
        else:
            ipClassSum['W'] += 1
    except:
        break

for v in ipClassSum.values():
    print(v, end=' ')

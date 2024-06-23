#!/usr/bin/python3

import nmcli
import requests
import subprocess
from pathlib import Path
import os

surfshark_user = '2E5E9JNJT7hCUQ23wzw5gCdg'
surfshark_pass = 'k24bgURS3TcRBRkGVHUUwf5U'

surfshark_ca = """
-----BEGIN CERTIFICATE-----
MIIFTTCCAzWgAwIBAgIJAMs9S3fqwv+mMA0GCSqGSIb3DQEBCwUAMD0xCzAJBgNV
BAYTAlZHMRIwEAYDVQQKDAlTdXJmc2hhcmsxGjAYBgNVBAMMEVN1cmZzaGFyayBS
b290IENBMB4XDTE4MDMxNDA4NTkyM1oXDTI4MDMxMTA4NTkyM1owPTELMAkGA1UE
BhMCVkcxEjAQBgNVBAoMCVN1cmZzaGFyazEaMBgGA1UEAwwRU3VyZnNoYXJrIFJv
b3QgQ0EwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDEGMNj0aisM63o
SkmVJyZPaYX7aPsZtzsxo6m6p5Wta3MGASoryRsBuRaH6VVa0fwbI1nw5ubyxkua
Na4v3zHVwuSq6F1p8S811+1YP1av+jqDcMyojH0ujZSHIcb/i5LtaHNXBQ3qN48C
c7sqBnTIIFpmb5HthQ/4pW+a82b1guM5dZHsh7q+LKQDIGmvtMtO1+NEnmj81BAp
FayiaD1ggvwDI4x7o/Y3ksfWSCHnqXGyqzSFLh8QuQrTmWUm84YHGFxoI1/8AKdI
yVoB6BjcaMKtKs/pbctk6vkzmYf0XmGovDKPQF6MwUekchLjB5gSBNnptSQ9kNgn
TLqi0OpSwI6ixX52Ksva6UM8P01ZIhWZ6ua/T/tArgODy5JZMW+pQ1A6L0b7egIe
ghpwKnPRG+5CzgO0J5UE6gv000mqbmC3CbiS8xi2xuNgruAyY2hUOoV9/BuBev8t
tE5ZCsJH3YlG6NtbZ9hPc61GiBSx8NJnX5QHyCnfic/X87eST/amZsZCAOJ5v4EP
SaKrItt+HrEFWZQIq4fJmHJNNbYvWzCE08AL+5/6Z+lxb/Bm3dapx2zdit3x2e+m
iGHekuiE8lQWD0rXD4+T+nDRi3X+kyt8Ex/8qRiUfrisrSHFzVMRungIMGdO9O/z
CINFrb7wahm4PqU2f12Z9TRCOTXciQIDAQABo1AwTjAdBgNVHQ4EFgQUYRpbQwyD
ahLMN3F2ony3+UqOYOgwHwYDVR0jBBgwFoAUYRpbQwyDahLMN3F2ony3+UqOYOgw
DAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAgEAn9zV7F/XVnFNZhHFrt0Z
S1Yqz+qM9CojLmiyblMFh0p7t+Hh+VKVgMwrz0LwDH4UsOosXA28eJPmech6/bjf
ymkoXISy/NUSTFpUChGO9RabGGxJsT4dugOw9MPaIVZffny4qYOc/rXDXDSfF2b+
303lLPI43y9qoe0oyZ1vtk/UKG75FkWfFUogGNbpOkuz+et5Y0aIEiyg0yh6/l5Q
5h8+yom0HZnREHhqieGbkaGKLkyu7zQ4D4tRK/mBhd8nv+09GtPEG+D5LPbabFVx
KjBMP4Vp24WuSUOqcGSsURHevawPVBfgmsxf1UCjelaIwngdh6WfNCRXa5QQPQTK
ubQvkvXONCDdhmdXQccnRX1nJWhPYi0onffvjsWUfztRypsKzX4dvM9k7xnIcGSG
EnCC4RCgt1UiZIj7frcCMssbA6vJ9naM0s7JF7N3VKeHJtqe1OCRHMYnWUZt9vrq
X6IoIHlZCoLlv39wFW9QNxelcAOCVbD+19MZ0ZXt7LitjIqe7yF5WxDQN4xru087
FzQ4Hfj7eH1SNLLyKZkA1eecjmRoi/OoqAt7afSnwtQLtMUc2bQDg6rHt5C0e4dC
LqP/9PGZTSJiwmtRHJ/N5qYWIh9ju83APvLm/AGBTR2pXmj9G3KdVOkpIC7L35dI
623cSEC3Q3UZutsEm/UplsM=
-----END CERTIFICATE-----
"""

surfshark_ta = """
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
b02cb1d7c6fee5d4f89b8de72b51a8d0
c7b282631d6fc19be1df6ebae9e2779e
6d9f097058a31c97f57f0c35526a44ae
09a01d1284b50b954d9246725a1ead1f
f224a102ed9ab3da0152a15525643b2e
ee226c37041dc55539d475183b889a10
e18bb94f079a4a49888da566b9978346
0ece01daaf93548beea6c827d9674897
e7279ff1a19cb092659e8c1860fbad0d
b4ad0ad5732f1af4655dbd66214e552f
04ed8fd0104e1d4bf99c249ac229ce16
9d9ba22068c6c0ab742424760911d463
6aafb4b85f0c952a9ce4275bc821391a
a65fcd0d2394f006e3fba0fd34c4bc4a
b260f4b45dec3285875589c97d3087c9
134d3a3aa2f904512e85aa2dc2202498
-----END OpenVPN Static key V1-----
"""

# 通过 DNS-over-HTTPS 解析 IP 地址，尽可能避免 DNS 污染
def resolve(domain: str, dns = '1.1.1.1') -> list[str]:
    api_url = f'https://{dns}/dns-query?type=A&name={domain}'
    try:
        res = requests.get(api_url, headers={'Accept': 'application/dns-json'}, timeout=5)
        data = res.json()
        ip_list: list[str] = []
        for record in data['Answer']:
            ip_list.append(record['data'])
        return ip_list
    except:
        return None

def cross_resolve(domain: str) -> list[str] | None:
    for dns in ['1.1.1.1', 'dns.alidns.com', 'doh.pub', 'dns.twnic.tw', 'dns.google', 'dns.quad9.net', 'doh.sb']:
        ip_list = resolve(domain, dns)
        if ip_list:
            return ip_list
    return None

def ping(ip: str) -> bool:
    try:
        if subprocess.call(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, timeout=1) == 0:
            return True
        else:
            return False
    except:
        return False

def surfshark():
    cert_dir = Path.joinpath(Path.home(), '.cert', 'nm-openvpn')
    Path(cert_dir).mkdir(parents=True, exist_ok=True)

    ca_path = Path.joinpath(cert_dir, 'surfshark-ca.pem')
    ca_file = open(ca_path, 'w')
    ca_file.write(surfshark_ca)
    ca_file.close()

    ta_path = Path.joinpath(cert_dir, 'surfshark-tls-auth.pem')
    ta_file = open(ta_path, 'w')
    ta_file.write(surfshark_ta)
    ta_file.close()

    servers = [
        { 'domain': 'au-bne.prod.surfshark.com', 'name': '澳大利亚・布里斯班' },
        { 'domain': 'au-syd.prod.surfshark.com', 'name': '澳大利亚・悉尼' },
        { 'domain': 'az-bak.prod.surfshark.com', 'name': '阿塞拜疆・巴库' },
        { 'domain': 'ba-sjj.prod.surfshark.com', 'name': '波斯尼亚和黑塞哥维那・萨拉热窝' },
        { 'domain': 'be-anr.prod.surfshark.com', 'name': '比利时・安特卫普' },
        { 'domain': 'br-sao.prod.surfshark.com', 'name': '巴西・圣保罗' },
        { 'domain': 'ca-tor.prod.surfshark.com', 'name': '加拿大・多伦多' },
        { 'domain': 'ca-van.prod.surfshark.com', 'name': '加拿大・温哥华' },
        { 'domain': 'cl-san.prod.surfshark.com', 'name': '智利・圣地亚哥' },
        { 'domain': 'co-bog.prod.surfshark.com', 'name': '哥伦比亚・波哥大' },
        { 'domain': 'de-ber.prod.surfshark.com', 'name': '德国・柏林' },
        { 'domain': 'de-fra.prod.surfshark.com', 'name': '德国・法兰克福' },
        { 'domain': 'es-bcn.prod.surfshark.com', 'name': '西班牙・巴塞罗那' },
        { 'domain': 'es-vlc.prod.surfshark.com', 'name': '西班牙・巴伦西亚' },
        { 'domain': 'fr-par.prod.surfshark.com', 'name': '法国・巴黎' },
        { 'domain': 'gr-ath.prod.surfshark.com', 'name': '希腊・雅典' },
        { 'domain': 'hk-hkg.prod.surfshark.com', 'name': '香港' },
        { 'domain': 'hr-zag.prod.surfshark.com', 'name': '克罗地亚・萨格勒布' },
        { 'domain': 'id-jak.prod.surfshark.com', 'name': '印度尼西亚・雅加达' },
        { 'domain': 'ie-dub.prod.surfshark.com', 'name': '爱尔兰・都柏林' },
        { 'domain': 'im-iom.prod.surfshark.com', 'name': '马恩岛・道格拉斯' },
        { 'domain': 'in-del.prod.surfshark.com', 'name': '印度・新德里' },
        { 'domain': 'in-mum.prod.surfshark.com', 'name': '印度・孟买' },
        { 'domain': 'it-mil.prod.surfshark.com', 'name': '意大利・米兰' },
        { 'domain': 'jp-tok.prod.surfshark.com', 'name': '日本・东京' },
        { 'domain': 'kr-seo.prod.surfshark.com', 'name': '韩国・首尔' },
        { 'domain': 'lt-vno.prod.surfshark.com', 'name': '立陶宛・维尔纽斯' },
        { 'domain': 'lv-rig.prod.surfshark.com', 'name': '拉脱维亚・里加' },
        { 'domain': 'mc-mcm.prod.surfshark.com', 'name': '摩纳哥・蒙特卡洛' },
        { 'domain': 'mm-nyt.prod.surfshark.com', 'name': '缅甸・内比都' },
        { 'domain': 'mx-qro.prod.surfshark.com', 'name': '墨西哥・克雷塔罗' },
        { 'domain': 'my-kul.prod.surfshark.com', 'name': '马来西亚・吉隆坡' },
        { 'domain': 'nz-akl.prod.surfshark.com', 'name': '新西兰・奥克兰' },
        { 'domain': 'ph-mnl.prod.surfshark.com', 'name': '菲律宾・马尼拉' },
        { 'domain': 'pt-lis.prod.surfshark.com', 'name': '葡萄牙・里斯本' },
        { 'domain': 'si-lju.prod.surfshark.com', 'name': '斯洛文尼亚・卢布尔雅那' },
        { 'domain': 'th-bkk.prod.surfshark.com', 'name': '泰国・曼谷' },
        { 'domain': 'tr-ist.prod.surfshark.com', 'name': '土耳其・伊斯坦布尔' },
        { 'domain': 'tw-tai.prod.surfshark.com', 'name': '台湾・台中' },
        { 'domain': 'uk-edi.prod.surfshark.com', 'name': '英国・爱丁堡' },
        { 'domain': 'uk-gla.prod.surfshark.com', 'name': '英国・格拉斯哥' },
        { 'domain': 'uk-man.prod.surfshark.com', 'name': '英国・曼彻斯特' },
        { 'domain': 'uk-lon.prod.surfshark.com', 'name': '英国・伦敦' },
        { 'domain': 'us-sfo.prod.surfshark.com', 'name': '美国・旧金山' },
        { 'domain': 'us-slc.prod.surfshark.com', 'name': '美国・盐湖城' },
        { 'domain': 'us-lax.prod.surfshark.com', 'name': '美国・洛杉矶' },
        { 'domain': 'us-ltm.prod.surfshark.com', 'name': '美国・莱瑟姆' },
        { 'domain': 'us-bos.prod.surfshark.com', 'name': '美国・波士顿' },
        { 'domain': 'us-nyc.prod.surfshark.com', 'name': '美国・纽约' },
        { 'domain': 'us-dal.prod.surfshark.com', 'name': '美国・达拉斯' },
        { 'domain': 'us-clt.prod.surfshark.com', 'name': '美国・夏洛特' },
        { 'domain': 'us-atl.prod.surfshark.com', 'name': '美国・亚特兰大' },
        { 'domain': 'us-hou.prod.surfshark.com', 'name': '美国・休斯敦' },
        { 'domain': 'us-mia.prod.surfshark.com', 'name': '美国・迈阿密' },
        { 'domain': 'uy-mvd.prod.surfshark.com', 'name': '乌拉圭・蒙得维的亚' },
        { 'domain': 'uz-tas.prod.surfshark.com', 'name': '乌兹别克斯坦・塔什干' },
        { 'domain': 've-car.prod.surfshark.com', 'name': '委内瑞拉・加拉加斯' },
    ]

    for server in servers:
        domain = server['domain']
        name = server['name']
        print('📡 ' + domain)
        ip_list = cross_resolve(domain)

        num = 0

        for ip in ip_list:
            # 检测是否能 ping 通
            if ping(ip):
                num += 1
                vpn_name = f'{name} #{num} 🦈'
                try:
                    nmcli.connection.add(name=vpn_name, conn_type='vpn', options={
                        'connection.permissions': f'user:{os.getlogin()}',
                        'vpn.service-type': 'org.freedesktop.NetworkManager.openvpn',
                        'vpn.data': f'auth = SHA512, ca = {ca_path}, cipher = AES-256-CBC, connection-type = password, dev = tun, mssfix = 1450, password-flags = 1, ping = 15, ping-restart = 0, remote = {ip}:1194, remote-cert-tls = server, remote-random = yes, reneg-seconds = 0, ta = {ta_path}, ta-dir = 1, tunnel-mtu = 1500, username = {surfshark_user}',
                        'vpn.secrets': f'password = {surfshark_pass}',
                    })
                    try:
                        # 检测 OpenVPN 是否能连接
                        nmcli.connection.up(vpn_name, wait=5)
                        nmcli.connection.down(vpn_name)
                        print(f'   ✅ {ip} 连接成功')
                    except:
                        # 不能连接则删除
                        nmcli.connection.delete(vpn_name)
                        print(f'   ❌ {ip} 连接失败')
                except:
                    print(f'   ❌ {ip} 创建失败')
            else:
                print(f'   ❌ {ip} ping 失败')

    return servers

def main():
    nmcli.disable_use_sudo()

    for connection in nmcli.connection():
        if connection.conn_type == 'vpn':
            # 断开当前的 VPN 连接，以便检测服务器可用性
            try:
                nmcli.connection.down(connection.name)
            except:
                pass

            # 删除之前生成的 VPN 连接
            if connection.name.find('🦈') > 0:
                try:
                    nmcli.connection.delete(connection.name)
                except:
                    print(f'删除「{connection.name}」失败，此连接可能无法正常工作，请手动删除')

    surfshark()

main()
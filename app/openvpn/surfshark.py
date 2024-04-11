import requests
import subprocess

def surfshark():
    servers = [
        { 'domain': 'au-bne.prod.surfshark.com', 'name': '澳大利亚・布里斯班' },
        { 'domain': 'au-syd.prod.surfshark.com', 'name': '澳大利亚・悉尼' },
        { 'domain': 'az-bak.prod.surfshark.com', 'name': '阿塞拜疆・Baku' },
        { 'domain': 'ba-sjj.prod.surfshark.com', 'name': '波斯尼亚和黑塞哥维那・萨拉热窝' },
        { 'domain': 'be-anr.prod.surfshark.com', 'name': '比利时・安特卫普' },
        { 'domain': 'br-sao.prod.surfshark.com', 'name': '巴西・圣保罗' },
        { 'domain': 'ca-tor.prod.surfshark.com', 'name': '加拿大・多伦多' },
        { 'domain': 'ca-van.prod.surfshark.com', 'name': '加拿大・温哥华' },
        { 'domain': 'cl-san.prod.surfshark.com', 'name': '智利・圣地亚哥' },
        { 'domain': 'co-bog.prod.surfshark.com', 'name': '哥伦比亚・Bogota' },
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
        { 'domain': 'im-iom.prod.surfshark.com', 'name': '马恩岛・Douglas' },
        { 'domain': 'in-del.prod.surfshark.com', 'name': '印度・新德里' },
        { 'domain': 'in-mum.prod.surfshark.com', 'name': '印度・孟买' },
        { 'domain': 'it-mil.prod.surfshark.com', 'name': '意大利・米兰' },
        { 'domain': 'jp-tok.prod.surfshark.com', 'name': '日本・东京' },
        { 'domain': 'kr-seo.prod.surfshark.com', 'name': '韩国・首尔' },
        { 'domain': 'lt-vno.prod.surfshark.com', 'name': '立陶宛・Vilnius' },
        { 'domain': 'lv-rig.prod.surfshark.com', 'name': '拉脱维亚・里加' },
        { 'domain': 'mc-mcm.prod.surfshark.com', 'name': '摩纳哥・Monte Carlo' },
        { 'domain': 'mm-nyt.prod.surfshark.com', 'name': '缅甸・Naypyidaw' },
        { 'domain': 'mx-qro.prod.surfshark.com', 'name': '墨西哥・Queretaro' },
        { 'domain': 'my-kul.prod.surfshark.com', 'name': '马来西亚・吉隆坡' },
        { 'domain': 'nz-akl.prod.surfshark.com', 'name': '新西兰・奥克兰' },
        { 'domain': 'ph-mnl.prod.surfshark.com', 'name': '菲律宾・马尼拉' },
        { 'domain': 'pt-lis.prod.surfshark.com', 'name': '葡萄牙・里斯本' },
        { 'domain': 'si-lju.prod.surfshark.com', 'name': '斯洛文尼亚・卢布尔雅那' },
        { 'domain': 'th-bkk.prod.surfshark.com', 'name': '泰国・曼谷' },
        { 'domain': 'tr-ist.prod.surfshark.com', 'name': '土耳其・Istanbul' },
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
        { 'domain': 'uy-mvd.prod.surfshark.com', 'name': '乌拉圭・Montevideo' },
        { 'domain': 'uz-tas.prod.surfshark.com', 'name': '乌兹别克斯坦・Tashkent' },
        { 'domain': 've-car.prod.surfshark.com', 'name': '委内瑞拉・Caracas' },
    ]

    for server in servers:
        print('📡 ' + server['domain'])
        api_url = 'https://1.1.1.1/dns-query?type=A&name=' + server['domain']
        res = requests.get(api_url, headers={'Accept': 'application/dns-json'})
        data = res.json()
        server['ips'] = []
        for record in data['Answer']:
            ip = record['data']
            if subprocess.call(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL) == 0:
                print('✅ ' + ip)
                server['ips'].append(ip)
            else:
                print('❌' + ip)

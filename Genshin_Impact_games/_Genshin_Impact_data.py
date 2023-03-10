'''原神的游戏数据'''
from typing import Counter

'''角色名称
遵照格式： id: [官译简体,英文名(罗马音), 常见别称,] （<-依此顺序）目前只写了官译简体及英文
'''

UNUSE_NAME = [100, 128, 132, 134, 135, 139, 146]
CHARA_NAME = {
    101: ["阿贝多", "Albedo"],
    102: ["安柏", "Amber"],
    103: ["芭芭拉", "Barbara"],
    104: ["北斗", "Beidou"],
    105: ["班尼特", "Bennett"],
    106: ["重云", "Chongyun"],
    107: ["迪卢克", "Diluc"],
    108: ["迪奥娜", "Diona", "猫猫"],
    109: ["菲谢尔", "Fischl", "皇女", "小艾咪"],
    110: ["琴", "Jean", "琴团长"],
    111: ["凯亚", "Kaeya" ,"凯子哥"],
    112: ["刻晴", "Keqing", "小白老婆"],
    113: ["可莉", "Klee"],
    114: ["丽莎", "Lisa"],
    115: ["莫娜", "Mona"],
    116: ["凝光", "Ningguang"],
    117: ["七七", "Qiqi"],
    118: ["雷泽", "Razor"],
    119: ["砂糖", "Sucrose"],
    120: ["达达利亚", "Tartaglia"],
    121: ["荧", "Lumine"],
    122: ["空", "Aether"],
    123: ["温迪", "Venti", "巴巴托斯"],
    124: ["香菱", "Xiangling"],
    125: ["行秋", "Xingqiu"],
    126: ["辛焱", "Xinyan"],
    127: ["钟离", "Zhongli"],
    128: ["派蒙", "Paimon"],
    129: ["诺艾尔", "Noelle"],
    130: ["甘雨", "Ganyu"],
    131: ["魈", "Xiao"],
    132: ["派蒙（1）", "Paimon(1)", "派蒙"],
    133: ["胡桃", "Hutao"],
    134: ["派蒙(2)", "Paimon(2)", "派蒙"],
    135: ["派蒙(3)", "Paimon(3)", "派蒙"],
    136: ["罗莎莉亚", "Rosaria"],
    137: ["烟绯", "Yanfei"],
    138: ["优菈", "Eula"],
    139: ["派蒙(4)", "Paimon(4)", "派蒙"],
    140: ["宵宫", "Yoimiya"],
    141: ["神里绫华", "Kamisato_Ayaka", "神里"],
    142: ["早柚", "Sayu"],
    143: ["枫原万叶", "Kaedehara_Kazuha", "万叶"],
    144: ["雷电将军", "Raiden_Shogun", "巴尔泽布", "影", "雷神"],
    145: ["九条裟罗", "Kujou_Sara", "九条"],
    146: ["派蒙(5)", "Paimon(5)", "派蒙"],
    147: ["珊瑚宫心海", "Sangonomiya_Kokomi", "心海"],
    148: ["派蒙(6)","Paimon(6)","派蒙"],
    149: ["荒泷一斗","Arataki_Itto", "一斗"],
    150: ["五郎","Gorou"],
    151: ["申鹤","Shenhe"],
    152: ["云堇","Yunjin"],
    153: ["托马","Thoma"],
    154: ["埃洛伊","Aloy"],
    155: ["八重神子","Yae_Miko","神子"],
    156: ["神里绫人","Kamisato_Ayato","绫人"],
    157: ["戴因斯雷布","Dainsleif","戴因"],
    158: ["夜兰","Yelan","夜阑"],
    159: ["久岐忍","Kuki_Shinobu","阿卡丽"],
    160: ["鹿野院平藏", "Shikanoin_Heizou"],
    161: ["柯莱", "Collei"],
    162: ["提纳里", "Tighnari"],
}

CHARA_PROFILE = {
    101: {"名字": "阿贝多", "所属国家": "蒙德", "生日": "9月13日", "角色属性": "岩", "武器类型": "单手剑", "命之座": "白垩之子座", "发色": "白偏银发", "瞳色": "蓝瞳",
          "日文声优": "野岛健儿", "中文声优": "Mace", "称号": "白垩之子", "池子类型": "限定", "性别": "男"},
    102: {"名字": "安柏", "所属国家": "蒙德", "生日": "8月10日", "角色属性": "火", "武器类型": "弓", "命之座": "小兔座", "发色": "棕发", "瞳色": "金瞳",
          "日文声优": "石见舞菜香", "中文声优": "牛奶君", "称号": "侦查骑士", "池子类型": "常驻", "性别": "女"},
    103: {"名字": "芭芭拉", "所属国家": "蒙德", "生日": "7月5日", "角色属性": "水", "武器类型": "法器", "命之座": "金杯座", "发色": "金发", "瞳色": "蓝瞳",
          "日文声优": "鬼头明里", "中文声优": "宋媛媛", "称号": "内鬼", "池子类型": "常驻和限定", "性别": "女"},
    104: {"名字": "北斗", "所属国家": "璃月", "生日": "2月14日", "角色属性": "雷", "武器类型": "双手剑", "命之座": "南天海山座", "发色": "黑发", "瞳色": "红瞳",
          "日文声优": "小清水亚美", "中文声优": "唐雅菁", "称号": "无冕的龙王", "池子类型": "常驻和限定", "性别": "女"},
    105: {"名字": "班尼特", "所属国家": "蒙德", "生日": "2月29日", "角色属性": "火", "武器类型": "单手剑", "命之座": "险路座", "发色": "白偏金发", "瞳色": "绿瞳",
          "日文声优": "逢坂良太", "中文声优": "穆雪婷", "称号": "命运试金石", "池子类型": "常驻和限定", "性别": "男"},
    106: {"名字": "重云", "所属国家": "璃月", "生日": "9月7日", "角色属性": "冰", "武器类型": "双手剑", "命之座": "乾坤锋座", "发色": "蓝发", "瞳色": "蓝瞳",
          "日文声优": "齐藤壮马", "中文声优": "kinsen", "称号": "雪融有踪", "池子类型": "常驻和限定", "性别": "男"},
    107: {"名字": "迪卢克", "所属国家": "蒙德", "生日": "4月30日", "角色属性": "火", "武器类型": "双手剑", "命之座": "夜枭座", "发色": "红发", "瞳色": "红瞳",
          "日文声优": "小野贤章", "中文声优": "马洋", "称号": "正义人", "池子类型": "常驻", "性别": "男"},
    108: {"名字": "迪奥娜", "所属国家": "蒙德", "生日": "1月18日", "角色属性": "冰", "武器类型": "弓", "命之座": "小猫座", "发色": "粉发", "瞳色": "绿瞳",
          "日文声优": "井泽诗织", "中文声优": "诺亚", "称号": "酒业杀手", "池子类型": "常驻和限定", "性别": "女"},
    109: {"名字": "菲谢尔", "所属国家": "蒙德", "生日": "5月27日", "角色属性": "雷", "武器类型": "弓", "命之座": "幻鸦座", "发色": "金发", "瞳色": "绿瞳",
          "日文声优": "内田真礼", "中文声优": "Mace", "称号": "断罪之皇女", "池子类型": "常驻和限定", "性别": "女"},
    110: {"名字": "琴", "所属国家": "蒙德", "生日": "3月14日", "角色属性": "风", "武器类型": "单手剑", "命之座": "幼狮座", "发色": "金发", "瞳色": "蓝瞳",
          "日文声优": "斋藤千和", "中文声优": "林簌", "称号": "蒲公英骑士", "池子类型": "常驻", "性别": "女"},
    111: {"名字": "凯亚", "所属国家": "蒙德", "生日": "11月30日", "角色属性": "冰", "武器类型": "单手剑", "命之座": "孔雀羽座", "发色": "蓝发", "瞳色": "蓝瞳",
          "日文声优": "鸟海浩辅", "中文声优": "孙晔", "称号": "踏冰渡海真君", "池子类型": "常驻", "性别": "男"},
    112: {"名字": "刻晴", "所属国家": "璃月", "生日": "11月20日", "角色属性": "雷", "武器类型": "单手剑", "命之座": "金紫定垂座", "发色": "紫发", "瞳色": "紫瞳",
          "日文声优": "喜多村英梨", "中文声优": "谢莹", "称号": "小白白老婆", "池子类型": "常驻和限定", "性别": "女"},
    113: {"名字": "可莉", "所属国家": "蒙德", "生日": "7月27日", "角色属性": "火", "武器类型": "法器", "命之座": "四叶草座", "发色": "金发", "瞳色": "红瞳",
          "日文声优": "久野美咲", "中文声优": "fa玲", "称号": "放火烧山真君", "池子类型": "限定", "性别": "女"},
    114: {"名字": "丽莎", "所属国家": "蒙德", "生日": "6月9日", "角色属性": "雷", "武器类型": "法器", "命之座": "沙漏座", "发色": "棕发", "瞳色": "绿瞳",
          "日文声优": "田中理惠", "中文声优": "钟可", "称号": "蔷薇魔女", "池子类型": "常驻", "性别": "女"},
    115: {"名字": "莫娜", "所属国家": "蒙德", "生日": "8月31日", "角色属性": "水", "武器类型": "法器", "命之座": "映天座", "发色": "紫发", "瞳色": "绿瞳",
          "日文声优": "小原好美", "中文声优": "陈婷婷", "称号": "星天水镜", "池子类型": "常驻", "性别": "女"},
    116: {"名字": "凝光", "所属国家": "璃月", "生日": "8月26日", "角色属性": "岩", "武器类型": "法器", "命之座": "玑衡仪座", "发色": "银发", "瞳色": "红瞳",
          "日文声优": "大原沙耶香", "中文声优": "杜冥鸦", "称号": "天权星", "池子类型": "常驻和限定", "性别": "女"},
    117: {"名字": "七七", "所属国家": "璃月", "生日": "3月3日", "角色属性": "冰", "武器类型": "单手剑", "命之座": "三清铃座", "发色": "紫发", "瞳色": "粉瞳",
          "日文声优": "田村由香里", "中文声优": "宴宁", "称号": "冻冻回魂夜", "池子类型": "常驻", "性别": "女"},
    118: {"名字": "雷泽", "所属国家": "蒙德", "生日": "9月9日", "角色属性": "雷", "武器类型": "双手剑", "命之座": "小狼座", "发色": "银发", "瞳色": "红瞳",
          "日文声优": "内山昂辉", "中文声优": "周帅", "称号": "奔狼领的传说", "池子类型": "常驻和限定", "性别": "男"},
    119: {"名字": "砂糖", "所属国家": "蒙德", "生日": "11月26日", "角色属性": "风", "武器类型": "法器", "命之座": "烧瓶座", "发色": "绿发", "瞳色": "橙瞳",
          "日文声优": "藤田茜", "中文声优": "小敢", "称号": "雷莹术士", "池子类型": "常驻和限定", "性别": "女"},
    120: {"名字": "达达利亚", "所属国家": "至冬", "生日": "7月20日", "角色属性": "水", "武器类型": "弓", "命之座": "鲸天座", "发色": "黄发", "瞳色": "蓝瞳",
          "日文声优": "木村良平", "中文声优": "鱼冻", "称号": "玩具销售员", "池子类型": "限定", "性别": "男"},
    121: {"名字": "荧", "所属国家": "坎瑞亚", "生日": "???", "角色属性": "???", "武器类型": "单手剑", "命之座": "旅人座", "发色": "金发", "瞳色": "橙瞳",
          "日文声优": "悠木碧", "中文声优": "宴宁", "称号": "妹妹", "池子类型": "???", "性别": "女"},
    122: {"名字": "空", "所属国家": "坎瑞亚", "生日": "???", "角色属性": "???", "武器类型": "单手剑", "命之座": "旅人座", "发色": "金发", "瞳色": "橙瞳",
          "日文声优": "堀江瞬", "中文声优": "鹿喑", "称号": "哥哥", "池子类型": "???", "性别": "男"},
    123: {"名字": "温迪", "所属国家": "蒙德", "生日": "6月16日", "角色属性": "风", "武器类型": "弓", "命之座": "歌仙座", "发色": "绿发", "瞳色": "绿瞳",
          "日文声优": "村濑步", "中文声优": "喵☆酱", "称号": "摸鱼", "池子类型": "限定", "性别": "男"},
    124: {"名字": "香菱", "所属国家": "璃月", "生日": "11月2日", "角色属性": "火", "武器类型": "长柄武器", "命之座": "长杓座", "发色": "蓝发", "瞳色": "金瞳",
          "日文声优": "小泽亚李", "中文声优": "小N", "称号": "洲际导弹真君", "池子类型": "常驻和限定", "性别": "女"},
    125: {"名字": "行秋", "所属国家": "璃月", "生日": "10月9日", "角色属性": "水", "武器类型": "单手剑", "命之座": "锦织座", "发色": "蓝发", "瞳色": "棕瞳",
          "日文声优": "皆川纯子", "中文声优": "唐雅菁", "称号": "古华飞云", "池子类型": "常驻和限定", "性别": "男"},
    126: {"名字": "辛焱", "所属国家": "璃月", "生日": "10月16日", "角色属性": "火", "武器类型": "双手剑", "命之座": "红檀四弦座", "发色": "黑发", "瞳色": "金瞳",
          "日文声优": "高桥智秋", "中文声优": "王雅欣", "称号": "燥热旋律", "池子类型": "常驻和限定", "性别": "女"},
    127: {"名字": "钟离", "所属国家": "璃月", "生日": "12月31日", "角色属性": "岩", "武器类型": "长柄武器", "命之座": "岩王帝君座", "发色": "黑发", "瞳色": "金瞳",
          "日文声优": "前野智昭", "中文声优": "彭博", "称号": "未来战士", "池子类型": "限定", "性别": "男"},
    128: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    129: {"名字": "诺艾尔", "所属国家": "蒙德", "生日": "3月21日", "角色属性": "岩", "武器类型": "双手剑", "命之座": "心护座", "发色": "银发", "瞳色": "绿瞳",
          "日文声优": "高尾奏音", "中文声优": "宴宁", "称号": "山吹", "池子类型": "常驻和限定", "性别": "女"},
    130: {"名字": "甘雨", "所属国家": "璃月", "生日": "12月2日", "角色属性": "冰", "武器类型": "弓", "命之座": "仙麟座", "发色": "蓝发", "瞳色": "紫瞳",
          "日文声优": "上田丽奈", "中文声优": "林簌", "称号": "椰羊", "池子类型": "限定", "性别": "女"},
    131: {"名字": "魈", "所属国家": "璃月", "生日": "4月17日", "角色属性": "风", "武器类型": "长柄武器", "命之座": "金翅鹏王座", "发色": "绿发", "瞳色": "黄瞳",
          "日文声优": "松冈祯丞", "中文声优": "Kinsen", "称号": "打桩机", "池子类型": "限定", "性别": "男"},
    132: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    133: {"名字": "胡桃", "所属国家": "璃月", "生日": "7月15日", "角色属性": "火", "武器类型": "长柄武器", "命之座": "引蝶座", "发色": "褐发", "瞳色": "红",
          "日文声优": "高桥李依", "中文声优": "陶典", "称号": "雪霁梅香（暂定）", "池子类型": "限定", "性别": "女"},
    134: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    135: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    136: {"名字": "罗莎莉亚", "所属国家": "蒙德", "生日": "4月6日", "角色属性": "冰", "武器类型": "长柄武器", "命之座": "荆冠座", "发色": "白发", "瞳色": "紫瞳",
          "日文声优": "加隈亚衣", "中文声优": "张安琪", "称号": "白色史莱姆", "池子类型": "常驻UP", "性别": "女"},
    137: {"名字": "烟绯", "所属国家": "璃月", "生日": "7月28日", "角色属性": "火", "武器类型": "法器", "命之座": "法兽座", "发色": "粉发",
          "瞳色": "绿瞳",
          "日文声优": "花守由美里", "中文声优": "苏子芜", "称号": "璃月罗翔", "池子类型": "常驻UP", "性别": "女"},
    138: {"名字": "优菈", "所属国家": "蒙德", "生日": "10月25日", "角色属性": "冰", "武器类型": "双手剑", "命之座": "浪沫座", "发色": "蓝发",
          "瞳色": "棕瞳",
          "日文声优": "佐藤利奈", "中文声优": "子音", "称号": "游击小队队长", "池子类型": "限定", "性别": "女"},
    139: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    140: {"名字": "宵宫", "所属国家": "稻妻", "生日": "6月21日", "角色属性": "火", "武器类型": "弓", "命之座": "琉金座", "发色": "金发",
          "瞳色": "金瞳",
          "日文声优": "植田佳奈", "中文声优": "金娜", "称号": "火安柏", "池子类型": "限定", "性别": "女"},
    141: {"名字": "神里绫华", "所属国家": "稻妻", "生日": "9月28日", "角色属性": "冰", "武器类型": "单手剑", "命之座": "雪鹤座", "发色": "白发",
          "瞳色": "金瞳",
          "日文声优": "早见沙织", "中文声优": "小N", "称号": "白鹭公主", "池子类型": "限定", "性别": "女"},
    142: {"名字": "早柚", "所属国家": "稻妻", "生日": "10月19日", "角色属性": "风", "武器类型": "双手剑", "命之座": "小貉座", "发色": "(偏)绿发",
          "瞳色": "紫瞳",
          "日文声优": "洲崎绫", "中文声优": "Sakula小舞", "称号": "忍里之貉", "池子类型": "常驻UP", "性别": "女"},
    143: {"名字": "枫原万叶", "所属国家": "稻妻", "生日": "10月29日", "角色属性": "风", "武器类型": "单手剑", "命之座": "枫红座", "发色": "白发",
          "瞳色": "棕瞳",
          "日文声优": "岛崎信长", "中文声优": "斑马", "称号": "红叶逐荒波", "池子类型": "限定", "性别": "男"},
    144: {"名字": "雷电将军", "所属国家": "稻妻", "生日": "6月26日", "角色属性": "雷", "武器类型": "长柄武器", "命之座": "天下人座", "发色": "紫发",
          "瞳色": "紫瞳",
          "日文声优": "泽城美雪", "中文声优": "菊花花", "称号": "一心净土", "池子类型": "限定", "性别": "女"},
    145: {"名字": "九条裟罗", "所属国家": "稻妻", "生日": "7月14日", "角色属性": "雷", "武器类型": "弓", "命之座": "羽团扇座", "发色": "蓝发",
          "瞳色": "棕瞳",
          "日文声优": "濑户麻沙美", "中文声优": "杨梦露", "称号": "黑羽鸣镝", "池子类型": "常驻UP", "性别": "女"},
    146: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    147: {"名字": "珊瑚宫心海", "所属国家": "稻妻", "生日": "2月22日", "角色属性": "水", "武器类型": "法器", "命之座": "眠龙座", "发色": "粉白发", "瞳色": "蓝瞳",
          "日文声优": "三森铃子", "中文声优": "龟娘", "称号": "可她是粉色水母欸", "池子类型": "限定", "性别": "女"},
    148: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???", "发色": "白发", "瞳色": "蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品", "池子类型": "???", "性别": "女"},
    149: {"名字": "荒泷一斗", "所属国家": "稻妻", "生日": "6月1日", "角色属性": "岩", "武器类型": "双手剑", "命之座": "天牛座", "发色": "白发",
          "瞳色": "红瞳",
          "日文声优": "西川贵教", "中文声优": "刘照坤", "称号": "花坂豪快", "池子类型": "限定", "性别": "男"},
    150: {"名字": "五郎", "所属国家": "稻妻", "生日": "5月18日", "角色属性": "岩", "武器类型": "弓", "命之座": "柴犬座", "发色": "棕发", "瞳色": "青瞳",
          "日文声优": "畠中祐", "中文声优": "杨昕燃", "称号": "希娜小姐", "池子类型": "常驻UP", "性别": "男"},
    151: {"名字": "申鹤", "所属国家": "璃月", "生日": "3月10日", "角色属性": "冰", "武器类型": "长柄武器", "命之座": "愁疏座", "发色": "白发", "瞳色": "黄瞳",
          "日文声优": "川澄绫子", "中文声优": "秦紫翼", "称号": "中野三玖", "池子类型": "限定", "性别": "女"},
    152: {"名字": "云堇", "所属国家": "璃月", "生日": "5月21日", "角色属性": "岩", "武器类型": "长柄武器", "命之座": "虹章座", "发色": "紫发", "瞳色": "红瞳",
          "日文声优": "小岩井小鸟", "中文声优": "贺文潇", "称号": "先生", "池子类型": "常驻UP", "性别": "女"},
    153: {"名字": "托马", "所属国家": "稻妻", "生日": "1月09日", "角色属性": "火", "武器类型": "长柄武器", "命之座": "赤楯座", "发色": "黄发", "瞳色": "绿瞳",
          "日文声优": "森田成一", "中文声优": "张沛", "称号": "地头蛇", "池子类型": "限定", "性别": "男"},
    154: {"名字": "埃洛伊", "所属国家": "？？？", "生日": "4月4日", "角色属性": "冰", "武器类型": "弓", "命之座": "诺拉勇者座", "发色": "棕发", "瞳色": "绿瞳",
          "日文声优": "高垣彩阳", "中文声优": "沐霏", "称号": "异界的救世主", "池子类型": "???", "性别": "女"},
    155: {"名字": "八重神子", "所属国家": "稻妻", "生日": "6月27日", "角色属性": "雷", "武器类型": "法器", "命之座": "仙狐座", "发色": "粉发", "瞳色": "紫瞳",
          "日文声优": "佐仓绫音", "中文声优": "杜冥鸦", "称号": "屑狐狸", "池子类型": "限定", "性别": "女"},  
    156: {"名字": "神里绫人", "所属国家": "稻妻", "生日": "4月6日", "角色属性": "水", "武器类型": "单手剑", "命之座": "神守柏座", "发色": "浅蓝发", "瞳色": "蓝偏紫瞳",
          "日文声优": "石田彰", "中文声优": "赵路", "称号": "小白白大舅子", "池子类型": "限定", "性别": "男"},       
    157: {"名字": "戴因斯雷布", "所属国家": "坎瑞亚", "生日": "???", "角色属性": "???", "武器类型": "单手剑", "命之座": "蛇环座", "发色": "金发", "瞳色": "蓝瞳",
          "日文声优": "津田健次郎", "中文声优": "孙晔", "称号": "末光之剑", "池子类型": "???", "性别": "男"},
    158: {"名字": "夜兰", "所属国家": "璃月", "生日": "4月20日", "角色属性": "水", "武器类型": "弓", "命之座": "幽客座",
          "发色": "蓝发",
          "瞳色": "绿瞳", "日文声优": "远藤绫", "中文声优": "徐慧", "称号": "天后", "池子类型": "限定", "性别": "女"},
    159: {"名字": "久岐忍", "所属国家": "稻妻", "生日": "7月27日", "角色属性": "雷", "武器类型": "单手剑",
          "命之座": "烦恼刈座", "发色": "绿发", "瞳色": "紫瞳",
          "日文声优": "水桥香织", "中文声优": "杨凝", "称号": "茄子形态的宵宫姐姐", "池子类型": "常驻", "性别": "女"},
    160: {"名字": "鹿野院平藏", "所属国家": "稻妻", "生日": "7月24日", "角色属性": "风", "武器类型": "法器",
          "命之座": "幼鹿座", "发色": "红发", "瞳色": "黄瞳",
          "日文声优": "井口祐一", "中文声优": "林景", "称号": "名侦探", "池子类型": "常驻", "性别": "男"},
    161: {"名字": "柯莱", "所属国家": "须弥", "生日": "5月8日", "角色属性": "草", "武器类型": "弓", "命之座": "薮猫座",
          "发色": "绿发", "瞳色": "紫瞳",
          "日文声优": "前川凉子", "中文声优": "秦文静", "称号": "柯里安巴", "池子类型": "常驻", "性别": "女"},
    162: {"名字": "提纳里", "所属国家": "须弥", "生日": "12月29日", "角色属性": "草", "武器类型": "弓",
          "命之座": "郭狐座", "发色": "绿发",
          "瞳色": "绿瞳", "日文声优": "小林沙苗", "中文声优": "莫然", "称号": "耳朵很好摸", "池子类型": "常驻",
          "性别": "男"},
}

WEAPON_NAME = {
    1001: ["无锋剑"],
    1002: ["银剑"],
    1003: ["吃虎鱼刀"],
    1004: ["黎明神剑"],
    1005: ["旅行剑"],
    1006: ["暗铁剑"],
    1007: ["冷刃"],
    1008: ["飞天御剑"],
    1009: ["腐殖之剑"],
    1010: ["黑剑"],
    1011: ["试作斩岩"],
    1012: ["暗巷闪光"],
    1013: ["宗室长剑"],
    1014: ["铁蜂刺"],
    1015: ["笛剑"],
    1016: ["祭礼剑"],
    1017: ["匣里龙吟"],
    1018: ["降临之剑"],
    1019: ["西风剑"],
    1020: ["黑岩长剑"],
    1021: ["磐岩结绿"],
    1022: ["风鹰剑"],
    1023: ["斫峰之刃"],
    1024: ["天空之刃"],
    1025: ["训练大剑"],
    1026: ["佣兵重剑"],
    1027: ["沐浴龙血的剑"],
    1028: ["白铁大剑"],
    1029: ["铁影阔剑"],
    1030: ["飞天大御剑"],
    1031: ["以理服人"],
    1032: ["雨裁"],
    1033: ["白影剑"],
    1034: ["黑岩斩刀"],
    1035: ["宗室大剑"],
    1036: ["祭礼大剑"],
    1037: ["雪葬的星银"],
    1038: ["螭骨剑"],
    1039: ["试作古华"],
    1040: ["西风大剑"],
    1041: ["钟剑"],
    1042: ["千岩古剑"],
    1043: ["天空之傲"],
    1044: ["无工之剑"],
    1045: ["狼的末路"],
    1046: ["猎弓"],
    1047: ["历练的猎弓"],
    1048: ["信使"],
    1049: ["弹弓"],
    1050: ["反曲弓"],
    1051: ["神射手之誓"],
    1052: ["鸦羽弓"],
    1053: ["黑岩战弓"],
    1054: ["试作澹月"],
    1055: ["宗室长弓"],
    1056: ["祭礼弓"],
    1057: ["苍翠猎弓"],
    1058: ["绝弦"],
    1059: ["风花之颂"],
    1060: ["钢轮弓"],
    1061: ["西风猎弓"],
    1062: ["弓藏"],
    1063: ["终末嗟叹之诗"],
    1064: ["天空之翼"],
    1065: ["阿莫斯之弓"],
    1066: ["学徒笔记"],
    1067: ["口袋魔导书"],
    1068: ["异世界行记"],
    1069: ["翡玉法球"],
    1070: ["甲级宝珏"],
    1071: ["魔导绪论"],
    1072: ["讨龙英杰谭"],
    1073: ["万国诸海图谱"],
    1074: ["昭心"],
    1075: ["暗巷的酒与诗"],
    1076: ["宗室秘法录"],
    1077: ["流浪乐章"],
    1078: ["匣里日月"],
    1079: ["西风秘典"],
    1080: ["忍冬之果"],
    1081: ["试作金珀"],
    1082: ["祭礼残章"],
    1083: ["黑岩绯玉"],
    1084: ["四风原典"],
    1085: ["天空之卷"],
    1086: ["尘世之锁"],
    1087: ["新手长枪"],
    1088: ["铁尖枪"],
    1089: ["黑缨枪"],
    1090: ["钺矛"],
    1091: ["白缨枪"],
    1092: ["流月针"],
    1093: ["匣里灭辰"],
    1094: ["千岩长枪"],
    1095: ["试作星镰"],
    1096: ["黑岩刺枪"],
    1097: ["西风长枪"],
    1098: ["龙脊长枪"],
    1099: ["决斗之枪"],
    1100: ["宗室猎枪"],
    1101: ["护摩之杖"],
    1102: ["和璞鸢"],
    1103: ["天空之脊"],
    1104: ["贯虹之槊"],
}

WEAPON_PROFILE = {
    1001: {"名字": "无锋剑", "类型": "单手剑", "稀有度": "1星"
        , "获取途径": "初始武器赠送, 宝箱, 商店购买"
        , "初始基础攻击力": "23", "副属性": "无"},
    1002: {"名字": "银剑", "类型": "单手剑", "稀有度": "2星"
        , "获取途径": "宝箱, 商店购买"
        , "初始基础攻击力": "33", "副属性": "无"},
    1003: {"名字": "吃虎鱼刀", "类型": "单手剑", "稀有度": "3星"
        , "获取途径": "宝箱"
        , "初始基础攻击力": "39", "副属性": "攻击力"},
    1004: {"名字": "黎明神剑", "类型": "单手剑", "稀有度": "3星"
        , "获取途径": "祈愿, 任务, （海盗密保孔雀羽之章）"
        , "初始基础攻击力": "39", "副属性": "暴击伤害"},
    1005: {"名字": "旅行剑", "类型": "单手剑", "稀有度": "3星"
        , "获取途径": "宝箱"
        , "初始基础攻击力": "40", "副属性": "防御力"},
    1006: {"名字": "暗铁剑", "类型": "单手剑", "稀有度": "3星"
        , "获取途径": "与璃月港小吃摊摊主快刀陈对话“鱼卖得怎样”, 对话"
        , "初始基础攻击力": "39", "副属性": "元素精通"},
    1007: {"名字": "冷刃", "类型": "单手剑", "稀有度": "3星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "39", "副属性": "攻击力"},
    1008: {"名字": "飞天御剑", "类型": "单手剑", "稀有度": "3星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "38", "副属性": "元素充能效率"},
    1009: {"名字": "腐殖之剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "活动"
        , "初始基础攻击力": "42", "副属性": "元素充能效率"},
    1010: {"名字": "黑剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "纪行"
        , "初始基础攻击力": "42", "副属性": "暴击率"},
    1011: {"名字": "试作斩岩", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "锻造"
        , "初始基础攻击力": "44", "副属性": "物理伤害加成"},
    1012: {"名字": "暗巷闪光", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "限定祈愿"
        , "初始基础攻击力": "45", "副属性": "元素精通"},
    1013: {"名字": "宗室长剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "商城兑换"
        , "初始基础攻击力": "42", "副属性": "攻击力"},
    1014: {"名字": "铁蜂刺", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "锻造"
        , "初始基础攻击力": "42", "副属性": "元素精通"},
    1015: {"名字": "笛剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "42", "副属性": "攻击力"},
    1016: {"名字": "祭礼剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "41", "副属性": "元素充能效率"},
    1017: {"名字": "匣里龙吟", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "42", "副属性": "攻击力"},
    1018: {"名字": "降临之剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "PS4特典奖励"
        , "初始基础攻击力": "39", "副属性": "攻击力"},
    1019: {"名字": "西风剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "41", "副属性": "元素充能效率"},
    1020: {"名字": "黑岩长剑", "类型": "单手剑", "稀有度": "4星"
        , "获取途径": "商城兑换"
        , "初始基础攻击力": "44", "副属性": "暴击伤害"},
    1021: {"名字": "磐岩结绿", "类型": "单手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "44", "副属性": "暴击率"},
    1022: {"名字": "风鹰剑", "类型": "单手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "48", "副属性": "物理伤害加成"},
    1023: {"名字": "斫峰之刃", "类型": "单手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "46", "副属性": "百分比攻击力"},
    1024: {"名字": "天空之刃", "类型": "单手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "46", "副属性": "元素充能效率"},
    1025: {"名字": "训练大剑", "类型": "双手剑", "稀有度": "1星"
        , "获取途径": "初始武器赠送, 宝箱, 商店购买"
        , "初始基础攻击力": "23", "副属性": "无"},
    1026: {"名字": "佣兵重剑", "类型": "双手剑", "稀有度": "2星"
        , "获取途径": "宝箱, 商店购买"
        , "初始基础攻击力": "33", "副属性": "无"},
    1027: {"名字": "沐浴龙血的剑", "类型": "双手剑", "稀有度": "3星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "38", "副属性": "元素精通"},
    1028: {"名字": "白铁大剑", "类型": "双手剑", "稀有度": "3星"
        , "获取途径": "宝箱"
        , "初始基础攻击力": "39", "副属性": "防御力"},
    1029: {"名字": "铁影阔剑", "类型": "双手剑", "稀有度": "3星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "39", "副属性": "生命值"},
    1030: {"名字": "飞天大御剑", "类型": "双手剑", "稀有度": "3星"
        , "获取途径": "孤云阁附近拔出, 宝箱"
        , "初始基础攻击力": "39", "副属性": "物理伤害加成"},
    1031: {"名字": "以理服人", "类型": "双手剑", "稀有度": "3星"
        , "获取途径": "祈愿, 宝箱"
        , "初始基础攻击力": "39", "副属性": "攻击力"},
    1032: {"名字": "雨裁", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "42", "副属性": "元素精通"},
    1033: {"名字": "白影剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "锻造"
        , "初始基础攻击力": "42", "副属性": "防御力"},
    1034: {"名字": "黑岩斩刀", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "商城兑换"
        , "初始基础攻击力": "42", "副属性": "暴击伤害"},
    1035: {"名字": "宗室大剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "商城兑换"
        , "初始基础攻击力": "44", "副属性": "百分比攻击力"},
    1036: {"名字": "祭礼大剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "44", "副属性": "元素充能效率"},
    1037: {"名字": "雪葬的星银", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "锻造, 任务"
        , "初始基础攻击力": "44", "副属性": "物理伤害加成"},
    1038: {"名字": "螭骨剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "纪行"
        , "初始基础攻击力": "42", "副属性": "暴击率"},
    1039: {"名字": "试作古华", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "锻造"
        , "初始基础攻击力": "44", "副属性": "百分比攻击力"},
    1040: {"名字": "西风大剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "41", "副属性": "元素充能效率"},
    1041: {"名字": "钟剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "42", "副属性": "生命值"},
    1042: {"名字": "千岩古剑", "类型": "双手剑", "稀有度": "4星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "42", "副属性": "攻击力"},
    1043: {"名字": "天空之傲", "类型": "双手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "48", "副属性": "元素充能效率"},
    1044: {"名字": "无工之剑", "类型": "双手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "46", "副属性": "百分比攻击力"},
    1045: {"名字": "狼的末路", "类型": "双手剑", "稀有度": "5星"
        , "获取途径": "祈愿"
        , "初始基础攻击力": "46", "副属性": "百分比攻击力"},
    # 1046: {"名字":"猎弓","类型":"单手剑","稀有度":"1星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"},
    # 1047: {"名字":"无锋剑","类型":"单手剑","稀有度":"1星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"历练的猎弓"],
    # 1048: {"名字":"无锋剑","类型":"单手剑","稀有度":"2星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"信使"],
    # 1049: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"弹弓"],
    # 1050: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"反曲弓"],
    # 1051: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"神射手之誓"],
    # 1052: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"鸦羽弓"],
    # 1053: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"黑岩战弓"],
    # 1054: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"试作澹月"],
    # 1055: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"宗室长弓"],
    # 1056: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"祭礼弓"],
    # 1057: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"苍翠猎弓"],
    # 1058: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"绝弦"],
    # 1059: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"风花之颂"],
    # 1060: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"钢轮弓"],
    # 1061: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"西风猎弓"],
    # 1062: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"弓藏"],
    # 1063: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"终末嗟叹之诗"],
    # 1064: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"天空之翼"],
    # 1065: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"阿莫斯之弓"],
    # 1066: {"名字":"无锋剑","类型":"单手剑","稀有度":"1星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"学徒笔记"],
    # 1067: {"名字":"无锋剑","类型":"单手剑","稀有度":"2星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"口袋魔导书"],
    # 1068: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"异世界行记"],
    # 1069: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"翡玉法球"],
    # 1070: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"甲级宝珏"],
    # 1071: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"魔导绪论"],
    # 1072: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"讨龙英杰谭"],
    # 1073: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"万国诸海图谱"],
    # 1074: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"昭心"],
    # 1075: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"暗巷的酒与诗"],
    # 1076: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"宗室秘法录"],
    # 1077: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"流浪乐章"],
    # 1078: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"匣里日月"],
    # 1079: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"西风秘典"],
    # 1080: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"忍冬之果"],
    # 1081: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"试作金珀"],
    # 1082: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"祭礼残章"],
    # 1083: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"黑岩绯玉"],
    # 1084: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"四风原典"],
    # 1085: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"天空之卷"],
    # 1086: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"尘世之锁"],
    # 1087: {"名字":"无锋剑","类型":"单手剑","稀有度":"1星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"新手长枪"],
    # 1088: {"名字":"无锋剑","类型":"单手剑","稀有度":"2星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"铁尖枪"],
    # 1089: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"黑缨枪"],
    # 1090: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"钺矛"],
    # 1091: {"名字":"无锋剑","类型":"单手剑","稀有度":"3星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"白缨枪"],
    # 1092: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"流月针"],
    # 1093: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"匣里灭辰"],
    # 1094: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"千岩长枪"],
    # 1095: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"试作星镰"],
    # 1096: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"黑岩刺枪"],
    # 1097: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"西风长枪"],
    # 1098: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"龙脊长枪"],
    # 1099: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"决斗之枪"],
    # 1100: {"名字":"无锋剑","类型":"单手剑","稀有度":"4星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"宗室猎枪"],
    # 1101: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"护摩之杖"],
    # 1102: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"和璞鸢"],
    # 1103: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"天空之脊"],
    # 1104: {"名字":"无锋剑","类型":"单手剑","稀有度":"5星"
    #        ,"获取途径":"祈愿"
    #        ,"初始基础攻击力":"23","副属性":"无"}"贯虹之槊"],
}

MONSTER_NAME = {
    301: ["深海龙蜥·原种", "水深海龙蜥"],
    302: ["深海龙蜥·吞雷", "雷深海龙蜥"],
    303: ["深渊咏者·渊火", "火深渊咏者","火咏者"],
    304: ["火飘浮灵"],
    305: ["冰飘浮灵"],
    306: ["深海龙蜥·啮冰", "冰深海龙蜥"],
    307: ["深海龙蜥之群"],
    308: ["雷飘浮灵"],
    309: ["魔化骗骗花","骗骗花王"],
    310: ["黄金王兽", "王兽"],
    311: ["嗜岩·兽境幼兽", "岩兽境幼兽"],
    312: ["嗜雷·兽境幼兽", "雷兽境幼兽"],
    313: ["嗜岩·兽境猎犬", "岩兽境猎犬"],
    314: ["嗜雷·兽境猎犬", "雷兽境猎犬"],
    315: ["岩飘浮灵"],
    316: ["风飘浮灵"],
    317: ["水飘浮灵"],
    318: ["雷音权现", "雷鸟"],
    319: ["无相之水", "无相水"],
    320: ["女士", "炎之魔女"],
    321: ["雷弹丘丘人"],
    322: ["野伏·火付番", "火野伏众","火野伏"],
    323: ["野伏·机巧番", "雷野伏众","雷野伏"],
    324: ["野伏·阵刀番", "野伏众","野伏"],
    325: ["愚人众·藏镜仕女", "藏镜仕女","仕女"],
    326: ["雷斧丘丘暴徒"],
    327: ["遗迹侦察者"],
    328: ["遗迹防卫者"],
    329: ["无相之火", "无相火"],
    330: ["恒常机关阵列"],
    331: ["遗迹巡弋者"],
    332: ["遗迹歼击者"],
    333: ["丘丘雷兜王"],
    334: ["雷丘丘萨满"],
    335: ["雷深渊法师"],
    336: ["海乱鬼·炎威", "火海乱鬼"],
    337: ["海乱鬼·雷腾", "雷海乱鬼"],
    338: ["电气骗骗花", "雷骗骗花"],
    339: ["魔偶剑鬼"],
    340: ["深渊咏者·紫电", "雷深渊咏者","雷咏者"],
    341: ["若陀龙王", "若陀"],
    342: ["无相之冰", "无相冰"],
    343: ["深渊使徒·激流", "水深渊使徒", "水使徒"],
    344: ["古岩龙蜥"],
    345: ["岩龙蜥"],
    346: ["自律守护机关"],
    347: ["大雪猪王"],
    348: ["丘丘霜铠王"],
    349: ["冰萤"],
    350: ["愚人众·冰萤术士","冰萤术士"],
    351: ["冰弹丘丘人"],
    352: ["冰盾丘丘暴徒"],
    353: ["冰丘丘萨满"],
    354: ["遗迹重机"],
    355: ["奇怪的丘丘人","大伟丘"],
    356: ["公子"],
    #357: ["愚人众先遣队·岩使游击兵","岩先遣队","岩使游击兵"],
    #358: ["愚人众先遣队·风拳前锋军","风先遣队","风拳前锋军"],
    #359: ["愚人众先遣队·冰铳重卫士","冰先遣队","冰铳重卫士"],
    #360: ["愚人众先遣队·火铳游击兵","火先遣队","火铳游击兵"],
    #361: ["愚人众先遣队·雷锤前锋军","雷先遣队","雷锤前锋军"],
    #362: ["炽热骗骗花","火骗骗花"],
    #363: ["冰霜骗骗花","冰骗骗花"],
    #364: ["爆炎树"],
    #365: ["幼岩龙蜥"],
    #366: ["纯水精灵·洛蒂娅"],
    #367: ["急冻树"],
    #368: ["愚人众先遣队·水铳重卫士","水先遣队","水铳重卫士"],
    #369: ["雷萤"],
    #370: ["水萤"],
    #371: ["岩史莱姆"],
    #372: ["冰史莱姆"],
    #373: ["草史莱姆"],
    #374: ["雷史莱姆"],
    #375: ["风史莱姆"],
    #376: ["水史莱姆"],
    #377: ["火史莱姆"],
    #378: ["盗宝团·冰之药剂师","冰盗宝团"],
    #379: ["盗宝团·火之药剂师","火盗宝团"],
    #380: ["盗宝团·雷之药剂师","雷盗宝团"],
    #381: ["盗宝团·水之药剂师","水盗宝团"],
    #382: ["草丘丘萨满"],
    #383: ["岩丘丘萨满"],
    #384: ["风丘丘萨满"],
    #385: ["水丘丘萨满"],
    #386: ["冰箭丘丘人"],
    #387: ["火箭丘丘人"],
    #388: ["雷箭丘丘人"],
    #389: ["冲锋丘丘人"],
    #390: ["爆弹丘丘人"],
    #391: ["丘丘岩盔王"],
    #392: ["火斧丘丘暴徒"],
    #393: ["愚人众·火之债务处理人","债务处理人","讨债人"],
    #393: ["遗迹守卫"],
    #393: ["遗迹猎者"],
    #393: ["无相之岩","无相岩"],
    #393: ["北风的王狼","狼王","安德留斯"],
    #393: ["裂空的魔龙","风魔龙","特瓦林"],
    #393: ["愚人众·雷萤术士","雷萤术士"],
    #393: ["火深渊法师"],
    #393: ["冰深渊法师"],
    #393: ["水深渊法师"],
    #393: ["无相之风","无相风"],
    #393: ["狂风之核"],
    #393: ["无相之雷","无相雷"],
    #393: ["岩盾丘丘暴徒"],
    #393: ["木盾丘丘暴徒"],
 
}




MONSTER_PROFILE = {
    301: {"名字": "深海龙蜥·原种", "所在区域": "渊下宫", "原魔类型": "精英怪", "元素属性": "水", "攻击方式": "混合", "掉落物品": "脆弱的骨片", "称号": "涤魔喷吐", "种族": "异种魔兽","经典台词":"无"},
    302: {"名字": "深海龙蜥·吞雷", "所在区域": "渊下宫", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "脆弱的骨片", "称号": "涤魔喷吐", "种族": "异种魔兽","经典台词":"无"},
    303: {"名字": "深渊咏者·渊火", "所在区域": "马克斯礁", "原魔类型": "精英怪", "元素属性": "火", "攻击方式": "远程", "掉落物品": "无", "称号": "真理哥", "种族": "深渊教团","经典台词":"炽热的箴言"},      
    304: {"名字": "火飘浮灵", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "火", "攻击方式": "混合", "掉落物品": "浮游干核", "称号": "火晶蝶", "种族": "元素生命","经典台词":"无"},
    305: {"名字": "冰飘浮灵", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "冰", "攻击方式": "远程", "掉落物品": "浮游干核", "称号": "冰晶蝶", "种族": "元素生命","经典台词":"无"},
    306: {"名字": "深海龙蜥·啮冰", "所在区域": "渊下宫", "原魔类型": "精英怪", "元素属性": "冰", "攻击方式": "混合", "掉落物品": "脆弱的骨片", "称号": "涤魔喷吐", "种族": "异种魔兽","经典台词":"无"},    
    307: {"名字": "深海龙蜥之群", "所在区域": "渊下宫", "原魔类型": "Boss", "元素属性": "冰、雷", "攻击方式": "混合", "掉落物品": "龙嗣伪鳍", "称号": "伏特加少女", "种族": "异种魔兽","经典台词":"无"},
    308: {"名字": "雷飘浮灵", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "浮游干核", "称号": "雷晶蝶", "种族": "元素生命","经典台词":"无"},
    309: {"名字": "魔化骗骗花", "所在区域": "雪山活动限时", "原魔类型": "Boss", "元素属性": "冰", "攻击方式": "混合", "掉落物品": "无", "称号": "假阿贝多", "种族": "异种魔兽","经典台词":"无"},
    310: {"名字": "黄金王兽", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "岩", "攻击方式": "混合", "掉落物品": "兽境王器", "称号": "兽境如来佛", "种族": "深渊教团","经典台词":"无"},
    311: {"名字": "嗜岩·兽境幼兽", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "岩", "攻击方式": "近战", "掉落物品": "隐兽指爪", "称号": "岩流血狗", "种族": "深渊教团","经典台词":" 嗷~~"},
    312: {"名字": "嗜雷·兽境幼兽", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "近战", "掉落物品": "隐兽指爪", "称号": "雷流血狗", "种族": "深渊教团","经典台词":" 嗷~~"},
    313: {"名字": "嗜岩·兽境猎犬", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "岩", "攻击方式": "混合", "掉落物品": "隐兽指爪", "称号": "岩流血狗", "种族": "深渊教团","经典台词":" 嗷~~"},
    314: {"名字": "嗜雷·兽境猎犬", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "隐兽指爪", "称号": "雷流血狗", "种族": "深渊教团","经典台词":" 嗷~~"},
    315: {"名字": "岩飘浮灵", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "岩", "攻击方式": "混合", "掉落物品": "浮游干核", "称号": "岩晶蝶", "种族": "元素生命","经典台词":"无"},
    316: {"名字": "风飘浮灵", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "风", "攻击方式": "远程", "掉落物品": "浮游干核", "称号": "风晶蝶", "种族": "元素生命","经典台词":"无"},
    317: {"名字": "水飘浮灵", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "水", "攻击方式": "远程", "掉落物品": "浮游干核", "称号": "水晶蝶", "种族": "元素生命","经典台词":"无"},
    318: {"名字": "雷音权现", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "雷霆数珠", "称号": "千年的怨恨", "种族": "元素生命","经典台词":"无"},
    319: {"名字": "无相之水", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "水", "攻击方式": "远程", "掉落物品": "排异之露", "称号": "希伊", "种族": "元素生命","经典台词":"无"},
    320: {"名字": "女士", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "冰、火", "攻击方式": "远程", "掉落物品": "狱火之蝶", "称号": "苍白少女", "种族": "值得铭记的强敌","经典台词":"你在瑟瑟发抖啊，是因为这极寒，还是恐惧呢？"},
    321: {"名字": "雷弹丘丘人", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "雷", "攻击方式": "远程", "掉落物品": "破损的面具", "称号": "雷史莱姆杀手", "种族": "丘丘部族","经典台词":"呀~"},
    322: {"名字": "野伏·火付番", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "火", "攻击方式": "混合", "掉落物品": "破旧的刀镡", "称号": "稻妻浮浪人", "种族": "人类","经典台词":"别想看见（后撤）"},
    323: {"名字": "野伏·机巧番", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "破旧的刀镡", "称号": "稻妻浮浪人", "种族": "人类","经典台词":"往哪儿逃"},
    324: {"名字": "野伏·阵刀番", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "物理", "攻击方式": "近战", "掉落物品": "破旧的刀镡", "称号": "稻妻浮浪人", "种族": "人类","经典台词":"这次是条大的"},
    325: {"名字": "愚人众·藏镜仕女", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "水", "攻击方式": "远程", "掉落物品": "黯淡棱镜", "称号": "讨债人之妻", "种族": "愚人众","经典台词":"不敬之人，必将得到惩罚"},
    326: {"名字": "雷斧丘丘暴徒", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "沉重号角", "称号": "避雷针", "种族": "丘丘部族","经典台词":"呼呼（旋转战斧~）"},
    327: {"名字": "遗迹侦察者", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "物理", "攻击方式": "混合", "掉落物品": "混沌机关", "称号": "机械水母", "种族": "自律机关","经典台词":"无"},
    328: {"名字": "遗迹防卫者", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "物理", "攻击方式": "混合", "掉落物品": "混沌机关", "称号": "盾山（bushi）", "种族": "自律机关","经典台词":"无"},
    329: {"名字": "无相之火", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "火", "攻击方式": "混合", "掉落物品": "阴燃之珠", "称号": "亚因", "种族": "元素生命","经典台词":"无"},
    330: {"名字": "恒常机关阵列", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "物理", "攻击方式": "混合", "掉落物品": "恒常机关之心", "称号": "无相铁", "种族": "自律机关","经典台词":"无"},
    331: {"名字": "遗迹巡弋者", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "物理", "攻击方式": "远程", "掉落物品": "混沌机关", "称号": "机械后撤怪", "种族": "自律机关","经典台词":"无"},
    332: {"名字": "遗迹歼击者", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "物理", "攻击方式": "远程", "掉落物品": "混沌机关", "称号": "机械钻地龙", "种族": "自律机关","经典台词":"无"},
    333: {"名字": "丘丘雷兜王", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "近战", "掉落物品": "沉重号角", "称号": "雷暴中漫行的神秘「王者」", "种族": "丘丘部族","经典台词":"无"},
    334: {"名字": "雷丘丘萨满", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "雷", "攻击方式": "混合", "掉落物品": "异能绘卷", "称号": "雷祭司", "种族": "丘丘部族","经典台词":"gusha~gusha~"},
    335: {"名字": "雷深渊法师", "所在区域": "稻妻", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "远程", "掉落物品": "地脉的旧枝", "称号": "雷法", "种族": "深渊教团","经典台词":"ika yaya~"},
    336: {"名字": "海乱鬼·炎威", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "火", "攻击方式": "近战", "掉落物品": "破旧的刀镡", "称号": "稻妻贼寇", "种族": "人类","经典台词":"给我倒下！"},
    337: {"名字": "海乱鬼·雷腾", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "雷", "攻击方式": "近战", "掉落物品": "破旧的刀镡", "称号": "稻妻贼寇", "种族": "人类","经典台词":"给我倒下！"},
    338: {"名字": "电气骗骗花", "所在区域": "稻妻", "原魔类型": "普通怪", "元素属性": "雷", "攻击方式": "远程", "掉落物品": "骗骗花蜜", "称号": "（伪）甜甜花", "种族": "异种魔兽","经典台词":"无"},
    339: {"名字": "魔偶剑鬼", "所在区域": "稻妻", "原魔类型": "Boss", "元素属性": "冰、风、物理", "攻击方式": "混合", "掉落物品": "魔偶机心", "称号": "嘟嘟大魔王", "种族": "自律机关","经典台词":"无"},
    340: {"名字": "深渊咏者·紫电", "所在区域": "马克斯礁", "原魔类型": "精英怪", "元素属性": "雷", "攻击方式": "远程", "掉落物品": "无", "称号": "恩典哥", "种族": "深渊教团","经典台词":"感受恩典！"},
    341: {"名字": "若陀龙王", "所在区域": "璃月", "原魔类型": "Boss", "元素属性": "岩、雷、火、冰、水", "攻击方式": "混合", "掉落物品": "龙王之冕", "称号": "伏龙树之底", "种族": "值得铭记的强敌","经典台词":"凡人，休得僭越！"},
    342: {"名字": "无相之冰", "所在区域": "雪山", "原魔类型": "Boss", "元素属性": "冰", "攻击方式": "混合", "掉落物品": "晶凝之华", "称号": "塔勒特", "种族": "元素生命","经典台词":"无"},
    343: {"名字": "深渊使徒·激流", "所在区域": "马克斯礁", "原魔类型": "精英怪", "元素属性": "水", "攻击方式": "混合", "掉落物品": "无", "称号": "冰系的儿子", "种族": "深渊教团","经典台词":"侍奉深渊吧！"},
    344: {"名字": "古岩龙蜥", "所在区域": "璃月", "原魔类型": "Boss", "元素属性": "雷、火、水、冰", "攻击方式": "混合", "掉落物品": "未熟之玉", "称号": "经常自杀", "种族": "异种魔兽","经典台词":"无"},
    345: {"名字": "岩龙蜥", "所在区域": "璃月", "原魔类型": "精英怪", "元素属性": "水、火、冰、雷", "攻击方式": "近战", "掉落物品": "脆弱的骨片", "称号": "跳跳虎", "种族": "异种魔兽","经典台词":"无"},
    346: {"名字": "自律守护机关", "所在区域": "雪山", "原魔类型": "普通怪", "元素属性": "冰", "攻击方式": "远程", "掉落物品": "无", "称号": "雪山小风扇", "种族": "自律机关","经典台词":"无"},
    347: {"名字": "大雪猪王", "所在区域": "雪山", "原魔类型": "普通怪", "元素属性": "冰", "攻击方式": "混合", "掉落物品": "冷冻肉", "称号": "雪山真正的Boss", "种族": "动物","经典台词":"无"},
    348: {"名字": "丘丘霜铠王", "所在区域": "雪山", "原魔类型": "精英怪", "元素属性": "冰", "攻击方式": "近战", "掉落物品": "沉重号角", "称号": "雪雾中漫行的神秘王者", "种族": "丘丘部族","经典台词":"无"},
    349: {"名字": "冰萤", "所在区域": "雪山", "原魔类型": "普通怪", "元素属性": "冰", "攻击方式": "远程", "掉落物品": "无", "称号": "冰蚊子", "种族": "小型生物","经典台词":"无"},
    350: {"名字": "愚人众·冰萤术士", "所在区域": "雪山", "原魔类型": "精英怪", "元素属性": "冰", "攻击方式": "近战", "掉落物品": "雾虚花粉", "称号": "冰砂糖", "种族": "愚人众","经典台词":"去吧，漂亮的小宝贝~"},
    351: {"名字": "冰弹丘丘人", "所在区域": "雪山", "原魔类型": "普通怪", "元素属性": "冰", "攻击方式": "远程", "掉落物品": "破损的面具", "称号": "冰史莱姆杀手", "种族": "丘丘部族","经典台词":"呀~"},
    352: {"名字": "冰盾丘丘暴徒", "所在区域": "雪山", "原魔类型": "精英怪", "元素属性": "冰", "攻击方式": "混合", "掉落物品": "沉重号角", "称号": "冰大丘丘", "种族": "丘丘部族","经典台词":"呼呼（野蛮冲撞~）"},
    353: {"名字": "冰丘丘萨满", "所在区域": "雪山", "原魔类型": "普通怪", "元素属性": "冰", "攻击方式": "混合", "掉落物品": "异能绘卷", "称号": "冰祭司", "种族": "丘丘部族","经典台词":"gusha~gusha~"},
    354: {"名字": "遗迹重机", "所在区域": "雪山", "原魔类型": "精英怪", "元素属性": "物理", "攻击方式": "混合", "掉落物品": "混沌装置", "称号": "雪山小宝", "种族": "自律机关","经典台词":"无"},
    355: {"名字": "奇怪的丘丘人", "所在区域": "蒙德、璃月", "原魔类型": "普通怪", "元素属性": "物理", "攻击方式": "混合", "掉落物品": "卷心菜", "称号": "别墅之灾", "种族": "丘丘部族","经典台词":"nini~dala~dala~"},
    356: {"名字": "公子", "所在区域": "璃月", "原魔类型": "Boss", "元素属性": "雷、水", "攻击方式": "混合", "掉落物品": "吞天之鲸·只角", "称号": "魔王武装", "种族": "值得铭记的强敌","经典台词":"这机会还挺难得的，就让我好好享受一下吧"},
          }


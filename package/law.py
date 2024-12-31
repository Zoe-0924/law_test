# 憲法條文資料 (範例)
constitution = {
    1: "中華民國基於三民主義，為民有、民治、民享之民主共和國。",
    2: "中華民國之主權屬於國民全體。",
    3: "有依法律規定年滿二十歲之國民，不分性別，具有選舉權。",
    4: "中華民國領土，依其固有疆域，非經國民大會之決議，不得變更之。",
}

def search_specific_law(num):
    try:
        if num in constitution:
            return f"第{num}條: {constitution[num]}"
        else:
            return print("查無此條文!")
    except ValueError:
        return print("請輸入有效的數字!")

def search_by_keyword(keyword):
    results = [f"第{key}條: {value}" for key, value in constitution.items() if keyword in value]
    if results:
        pump = "\n搜尋結果:\n"
        for result in results:
            pump += result
        return pump
    else:
        return "查無相關條文!"

def print_all_law():
    pump = "\n憲法條文:\n"
    for key, value in constitution.items():
        pump += f"第{key}條: {value}\n"
    return pump


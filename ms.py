# 憲法條文資料 (範例)
constitution = {
    1: "中華民國基於三民主義，為民有、民治、民享之民主共和國。",
    2: "中華民國之主權屬於國民全體。",
    3: "有依法律規定年滿二十歲之國民，不分性別，具有選舉權。",
    4: "中華民國領土，依其固有疆域，非經國民大會之決議，不得變更之。",
}

def search_constitution():
    while True:
        print("\n--- 憲法檢索器 ---")
        print("1. 查詢特定條文")
        print("2. 搜尋關鍵字")
        print("3. 顯示所有條文")
        print("4. 離開")
        
        choice = input("請選擇功能 (1-4): ")
        
        if choice == '1':
            # 查詢特定條文
            try:
                article = int(input("請輸入條號: "))
                if article in constitution:
                    print(f"第{article}條: {constitution[article]}")
                else:
                    print("查無此條文!")
            except ValueError:
                print("請輸入有效的數字!")
        
        elif choice == '2':
            # 搜尋關鍵字
            keyword = input("請輸入關鍵字: ")
            results = [f"第{key}條: {value}" for key, value in constitution.items() if keyword in value]
            if results:
                print("\n搜尋結果:")
                for result in results:
                    print(result)
            else:
                print("查無相關條文!")
        
        elif choice == '3':
            # 顯示所有條文
            print("\n憲法條文:")
            for key, value in constitution.items():
                print(f"第{key}條: {value}")
        
        elif choice == '4':
            # 離開
            print("感謝使用憲法檢索器，再見!")
            break
        
        else:
            print("請輸入有效的選項!")

# 執行程式
search_constitution()
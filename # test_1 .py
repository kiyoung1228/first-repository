# test_!
product1_name = "사과"
product1_price = 3000

product2_name = "바나나"
product2_price = 2500

product3_name = "우유"
product3_price = 4000

product4_name = "빵"
product4_price = 5500

product5_name = "계란"
product5_price = 6000

product6_name = "치즈"
product6_price = 7000

product7_name = "감자"
product7_price = 2000

product8_name = "양파"
product8_price = 1500

product9_name = "닭고기"
product9_price = 12000

product10_name = "소고기"
product10_price = 25000

# 총 금액 저장
total = 0

# 제품 목록 출력
print("번호 | 제품명   | 가격")
print("1", product1_name, product1_price, "원")
print("2", product2_name, product2_price, "원")
print("3", product3_name, product3_price, "원")
print("4", product4_name, product4_price, "원")
print("5", product5_name, product5_price, "원")
print("6", product6_name, product6_price, "원")
print("7", product7_name, product7_price, "원")
print("8", product8_name, product8_price, "원")
print("9", product9_name, product9_price, "원")
print("10", product10_name, product10_price, "원")
print("0을 누르면 구매를 종료합니다.")

# 반복문으로 100번까지 반복하도록 함
for i in range(100):
    num = int(input("\n제품 번호를 입력하세요 (0 입력 시 종료): "))

    if num == 0:
        break

    quantity = int(input("수량을 입력하세요: "))

    if num == 1:
        total = total + product1_price * quantity
    elif num == 2:
        total = total + product2_price * quantity
    elif num == 3:
        total = total + product3_price * quantity
    elif num == 4:
        total = total + product4_price * quantity
    elif num == 5:
        total = total + product5_price * quantity
    elif num == 6:
        total = total + product6_price * quantity
    elif num == 7:
        total = total + product7_price * quantity
    elif num == 8:
        total = total + product8_price * quantity
    elif num == 9:
        total = total + product9_price * quantity
    elif num == 10:
        total = total + product10_price * quantity
    else:
        print("없는 번호입니다.")
        continue

    print("현재까지 총 금액:", total, "원")

# 할인 계산
if total >= 100000:
    discount = 0.10
elif total >= 50000:
    discount = 0.05
else:
    discount = 0.0

discount_amount = int(total * discount)
final_price = total - discount_amount

# 결제 정보 출력
print("\n 결제 정보")
print("할인 전 총 금액 :", total, "원")
print("할인율 :", int(discount * 100), "%")
print("최종 결제 금액 :", final_price, "원")

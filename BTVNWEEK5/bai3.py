def create_item(name: str, qty: int, price: float) -> dict:
    return {"name": name, "qty": qty, "price": price}

def calc_total(items: list[dict]) -> float:
    return sum(map(lambda x: x["qty"] * x["price"], items))

def format_invoice(customer: str, items: list[dict]):
    print(f"Khách hàng: {customer}")
    print("-" * 45) 

    print(f"{'Sản phẩm':<15} {'SL':>5} {'Đơn giá':>10} {'Thành tiền':>12}")
    print("-" * 45)

    for item in items:
        subtotal = item["qty"] * item["price"]
        print(f"{item['name']:<15} {item['qty']:>5} {item['price']:>10.2f} {subtotal:>12.2f}")
    
    print("-" * 45)
    total = calc_total(items)
    print(f"{'TỔNG CỘNG:':<32} {total:>12.2f}")


items = [
    {"name": "Pen", "qty": 2, "price": 5.0},
    {"name": "Notebook", "qty": 1, "price": 15.0},
    {"name": "USB 32GB", "qty": 3, "price": 120.5} 
]

format_invoice("Nguyen Van A", items)
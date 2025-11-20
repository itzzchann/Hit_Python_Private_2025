students = [
    {"id": 1, "name": "An", "score": 8.5},
    {"id": 2, "name": "Bình", "score": 7.2},
    {"id": 3, "name": "Chi", "score": 9.0}
]
def find_by_id(data: list[dict], id: int) -> dict | None:
    for item in data:
        if item["id"] == id:
            return item
    return None
def filter_by_score(data: list[dict], min_score: float) -> list[dict]:
    return [item for item in data if item["score"] >= min_score]
def sort_by_score(data: list[dict], reverse=False) -> list[dict]:
    return sorted(data, key=lambda x: x["score"], reverse=reverse)
def add_student(data: list[dict], student_dict: dict) -> list[dict]:
    if not find_by_id(data, student_dict["id"]):
        data.append(student_dict)
        print(f"Đã thêm sinh viên: {student_dict['name']}")
    else:
        print(f"Lỗi: ID {student_dict['id']} đã tồn tại!")
    return data
def remove_student(data: list[dict], id: int) -> list[dict]:
    found = find_by_id(data, id)
    if found:
        data.remove(found)
        print(f"Đã xóa sinh viên ID: {id}")
    else:
        print(f"Không tìm thấy sinh viên ID: {id} để xóa")
    return data
def statistics(data: list[dict]) -> tuple:
    if not data: 
        return 0.0, None, None
    scores = [s["score"] for s in data] 
    mean_score = sum(scores) / len(scores)
    
    highest_score_student = max(data, key=lambda x: x["score"])
    lowest_score_student = min(data, key=lambda x: x["score"])
    
    return mean_score, highest_score_student, lowest_score_student

print(filter_by_score(students, 8.0))


print(sort_by_score(students))


new_student = {"id": 4, "name": "Dung", "score": 6.8}
add_student(students, new_student)

add_student(students, {"id": 1, "name": "Fake An", "score": 5.0})
print("\n--- Xóa ---")
remove_student(students, 1)
mean, high, low = statistics(students)
print(f"Điểm TB: {mean:.2f}") 
print(f"Cao nhất: {high['name']} ({high['score']})")
print(f"Thấp nhất: {low['name']} ({low['score']})")
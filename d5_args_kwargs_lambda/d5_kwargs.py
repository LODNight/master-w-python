# 2. **kwargs: Keyword Arguments
# Dấu 2 sao ** sẽ gom các tham số có tên (key=value) thành một Dictionary.

def create_student(name, id, **details):
    print(f"Dang tao ho so cho: {name} ({id})")
    
    for key,value in details.items():
        print(f"- {key} : {value}")

create_student("An", "SV01", email="an@gmail.com", city="HCM")
create_student("Binh", "SV02", age = 18)
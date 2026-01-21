# Tình huống: Viết module gửi email thông báo. Yêu cầu: Viết hàm send_email(subject, *recipients, **options):

# subject: Tiêu đề (bắt buộc).

# recipients: Danh sách email nhận (bao nhiêu người cũng được).

# options: Cấu hình thêm (VD: cc=['boss@gmail.com'], urgent=True...). Cách dùng thử:

# Gửi cho 1 người, không option
# Output: Print ra log mô phỏng việc gửi là được.

def send_email(subject, *recipients, **options):
    to_str = ", ".join(recipients)

    print(f"SENDING: '{subject}")
    print(f"  to: {to_str}")

    cc_list = options.get('cc')
    if cc_list:
        print(f"  CC: {', '.join(cc_list)}")

    if options.get('urgent') == True:
        print("Flag: Khan cap")
    print("-"*30)


send_email("Hop lop", "a@gmail.com") 

# Gửi cho 3 người, có CC và đánh dấu khẩn cấp
send_email("Deadline!", "a@gmail.com", "b@gmail.com", "c@gmail.com", 
           cc=["boss@company.com"], urgent=True)

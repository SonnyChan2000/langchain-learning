def validate_password(password):
    if len(password) < 8:
        raise ValueError("密码至少8位")

    has_upper = False
    has_digit = False

    for c in password:
        if c.isupper():
            has_upper = True
        if c.isdigit():
            has_digit = True

    if not has_upper:
        raise ValueError("密码必须包含大写字母")
    if not has_digit:
        raise ValueError("密码必须包含数字")
    return True

while True:
    try:
        if validate_password(input("请输入密码: ")):
            print("密码设置成功")
            break
    except ValueError as e:
        print(f"错误! {e}")
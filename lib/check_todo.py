# def check_todo(text):
#     if "#TODO" in text:
#         return True
#     else:
#         return False

def check_todo(text):
    for word in text:
        if "#TODO" not in text:
            return False
        else:
            return True
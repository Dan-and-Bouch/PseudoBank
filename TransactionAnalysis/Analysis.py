def analysis(pos_data, phone_data):
    pos_list = pos_data.split(',')[:3]
    phone_list = phone_data.split(',')[:3]

    if abs(float(pos_list[0]) - float(phone_list[0])) > 1:
        return False

    if abs(float(pos_list[1]) - float(phone_list[1])) > 1:
        return False

    if abs(float(pos_list[2]) - float(phone_list[2])) > 1000000:
        return False

    return True

import requests
from bs4 import BeautifulSoup

# Mã ANSI cho màu sắc
RED = "\033[31m"  # Màu đỏ
GREEN = "\033[32m"  # Màu xanh lá
YELLOW = "\033[33m"  # Màu vàng
BLUE = "\033[34m"  # Màu xanh dương
MAGENTA = "\033[35m"  # Màu hồng
CYAN = "\033[36m"  # Màu xanh da trời
RESET = "\033[0m"  # Reset màu về mặc định

# In ra màn hình với màu sắc
# print(RED + "Đây là văn bản màu đỏ" + RESET)
# print(GREEN + "Đây là văn bản màu xanh lá" + RESET)
# print(YELLOW + "Đây là văn bản màu vàng" + RESET)

def convert_name(name):
    dict_name =     {"icKeno icLe": "Lẻ",
                    "icKeno icChan": "Chẵn",
                    "icKeno icHoaCL": "Hòa"
                    }
    return dict_name[name]

def is_number(string):
    return string.isdigit()

# Gửi yêu cầu POST với dữ liệu form
url = 'https://www.minhchinh.com/xo-so-dien-toan-keno.html#containerKQKeno'

response = requests.post(url)

# Phân tích HTML
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# Tìm div với id 'pagenav'
pagenav_div = soup.find('div', id='pagenav')
# Tìm tất cả các liên kết trong div này
links = pagenav_div.find_all('a')
countCLontemp = 0
countCNhotemp = 0
countCL = 0
countC = 0
countL = 0
result_short = []
number_short = []
# Lặp qua từng liên kết và in ra số trang
for page_number in range(1,9):

    # Giả sử URL này và tham số tương ứng là kết quả của quá trình phân tích
    params = {"page": page_number}

    # Gửi yêu cầu GET
    response = requests.get(url, params=params)

    # Phân tích nội dung HTML của trang web
    soup = BeautifulSoup(response.text, 'html.parser')

    all_elements = soup.find_all(class_=["wrapperKQKeno", "wrapperKQKeno odd"])
    # print(all_elements)
    if len(all_elements) == 0:
        break

    print(f"\n<==== Trang số: {page_number} ====>")

    # Duyệt qua từng element và xử lý
    for element in all_elements:
        # Lấy thông tin mà bạn muốn từ mỗi element ở đây
        # Ví dụ: Lấy nội dung của class 'kyKQKeno'
        kyKQKeno_element = element.find('div', class_='kyKQKeno')
        if kyKQKeno_element:
            # print(kyKQKeno_element.text.strip())
            div_time_element = element.find('div', class_="timeKQ")
            if (div_time_element):
                time_elements = div_time_element.find_all('div')
                time_value = time_elements[1].text.strip()                

            cl_span_element = element.find('span', class_=["icKeno icChan", "icKeno icLe", "icKeno icHoaCL"])
            # print(span_element)
            if cl_span_element and 'title' in cl_span_element.attrs:
                title = cl_span_element['title']
                # print("title: " ,title)
                class_name = cl_span_element['class']
                class_string = ' '.join(class_name)
                # print("class_string: ", class_string)

            if (title != "Hòa Chẳn Lẻ"):
                number = int(title.split(":")[1].strip())
                # print(number)
                
                if (convert_name(class_string) == "Chẵn"):
                    result_short.append("C")
                    countC += 1
                    if (number == 11 or number == 12):
                        countCLontemp += 1
                        countCNhotemp  = 0
                        print(f"{GREEN} Time: {time_value}, {kyKQKeno_element.text.strip()}, {convert_name(class_string)} \t   {number} {RESET}\t <<< \t {countCLontemp}")
                    else:
                        countCLontemp  = 0
                        countCNhotemp += 1
                        print(f"{GREEN} Time: {time_value}, {kyKQKeno_element.text.strip()}, {convert_name(class_string)} \t   {number} {RESET}\t {countCNhotemp} \t >>>")

                elif (convert_name(class_string) == "Lẻ"):
                    result_short.append("L")
                    countL += 1
                    countCLontemp += 1
                    countCNhotemp += 1
                    print(f"{YELLOW} Time: {time_value}, {kyKQKeno_element.text.strip()}, {convert_name(class_string)} \t   {number} {RESET}\t {countCNhotemp} \t {countCLontemp}")
                
                number_short.append(number)
            else:
                countCLontemp += 1
                countCNhotemp += 1
                result_short.append("H")
                number_short.append("-")
                print(f"{RED} Time: {time_value}, {kyKQKeno_element.text.strip()}, {convert_name(class_string)} \t   -{RESET}\t {countCNhotemp} \t {countCLontemp}")
                countCL += 1

    

print(f"Hòa: {countCL}, Chẵn: {countC}, Lẻ: {countL}")

# result_short.reverse()
# for i in result_short:
#     print(i)

# print("\n====\n")
# number_short.reverse()
# for i in number_short:
#     print(i)

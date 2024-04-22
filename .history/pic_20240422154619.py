import cv2

def increase_resolution(image_path, output_path):
    # Đọc hình ảnh
    img = cv2.imread(image_path)

    # Tính toán kích thước mới
    width = int(img.shape[1] * 4)
    height = int(img.shape[0] * 4)

    # Tăng độ phân giải
    img_high_res = cv2.resize(img, (width, height), interpolation = cv2.INTER_CUBIC)

    # Lưu hình ảnh
    cv2.imwrite(output_path, img_high_res)

# Sử dụng hàm
increase_resolution('./version', './audio')

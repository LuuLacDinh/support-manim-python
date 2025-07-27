#ShowPassingFlash(VALUE, run_time=<float>, time_width=<float>)
#Hiệu ứng tạo cảm giác ánh sáng chạy dọc theo đường đi của một đối tượng
#time_width: Đầu ánh sáng chạy trước, đuôi ánh sáng sẽ "đuổi theo" sau một khoảng thời gian time_width

#MoveAlongPath(VALUE, PATH, rate_func=<>)
#Một đối tượng di chuyển theo một đường dẫn (PATH)
#                             ---rate_func---
# | Tên hàm             | Mô tả đơn giản             | Đặc điểm chuyển động  |
# | ------------------- | -------------------------- | --------------------- |
# | `linear`            | Chuyển động đều đều        | Đều từ đầu tới cuối   |
# | `smooth`            | Chậm → nhanh → chậm (mượt) | Mềm mại               |
# | `rush_into`         | Chậm đầu → nhanh dần       | Lao tới               |
# | `rush_from`         | Nhanh đầu → chậm dần       | Giảm tốc              |
# | `there_and_back`    | Đi rồi quay lại            | Hai chiều             |
# | `wiggle`            | Lắc lư qua lại             | Lắc lư                |
# | `ease_in_sine`      | Vào nhẹ nhàng              | Mượt phần đầu         |
# | `exponential_decay` | Giảm nhanh rồi từ từ       | Dùng cho hiệu ứng tắt |
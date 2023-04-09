# XSS Detection using python
1. Tổng quan
Đây là chương trình phát hiện XSS bằng học máy kết hợp.
2. Cấu tạo thư mục:

*File dataset:
	- raw_dataset là thư mục chứa các dataset thô ban đầu, chưa trích chọn
	- final_ds là thư mục chưa các dataset sau khi được trích chọn (61 đặc trưng)
	- dataset_for_training là dataset để huấn luyện (14 đặc trưng)
	- dataset_for_test là các file để test trên weka
lưu ý: file final_ds.output_raw3_malicious chứa các scipt, url độc hại chưa huấn luyện để, dùng để test

*File trích chọn:
- thư mục bao gồm các đặc trưng: lib/features/features.py
- thư mục để trích chọn: lib/features/feature_extraction.py (14 đặc trung) và lib/features/feature_extraction_old.py (với 61 đặc trưng)

*File lib/model/utils.py gồm tên cột, tên file, thay đổi tên file trong này

*Thư mục sfs
- lib/sfs/SFS.py: dùng để giảm trừ các đặc trưng từ 61 đặc trung còn 14 đặc trưng và xuất ra file test cuối cùng

*Thư mục controller
- lib/controller/analysis_script.py: file này dùng các trích chọn để trích chọn dataset thô thành dataset đã trích chọn, và ghép chúng lại
- lib/controller/create_traning_model.py: File này để huấn luyện và thống kê số liệu với 20% dataset để test
- lib/controller/create_training.py: file này để huấn luyện 100% dataset và lưu model sử dụng cho file lib/UI/test_app.py sử dụng

****Các bước để chạy chương trình****
	bước 1 - Thống kê: chạy chương trình lib/controller/create_traning_model.py
	bước 2 - Tạo model huấn luyện: lib/controller/create_training.py
	bước 3 - Chạy chương trình: lib/UI/test_app.py
	-nên nhớ file XSS thô chưa huấn luyện có thể dùng để test ở XSS_dataset_payloads_raw_malicious.txt 

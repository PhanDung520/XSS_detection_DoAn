import pandas as pd
import lib.features.feature_extraction as feauture_extraction
import lib.model.utils as utils

# df = pd.read_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\raw_dataset\XSS_dataset_raw1.csv")
#
# # list vector
# listRaw = df.values.tolist()
#
# listVectorExtract = []
#
# for line in listRaw:
#     listVectorExtract.append(feauture_extraction.ftrExtract(line[0], line[1]))
# print(listVectorExtract)
# output_processed = pd.DataFrame(listVectorExtract, columns=utils.column_name)
# output_processed.to_csv(r'C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_raw1.csv',
#                         index=False,
#                         )
#   -------------------------------------------------------------------------------------------------------------------
# df = pd.read_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\raw_dataset\XSS_dataset_raw2.csv")
#
# # list vector
# listRaw = df.values.tolist()
#
# listVectorExtract = []
#
# for line in listRaw:
#     listVectorExtract.append(feauture_extraction.ftrExtract(line[0], line[1]))
# print(listVectorExtract)
# output_processed = pd.DataFrame(listVectorExtract, columns=utils.column_name)
# output_processed.to_csv(r'C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_raw2.csv',
#                         index=False,
#                         )
#   -------------------------------------------------------------------------------------------------------------------
# xss_features = []
# k = 1
# label = 1
# with open(r'C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\raw_dataset\XSS_dataset_payloads_raw_malicious.txt', encoding='utf8') as file:
#     for line in file:
#         line = line.strip()
#         xss_features.append(feauture_extraction.ftrExtract(line, label))
#         print('x' + str(k))
#         k += 1
#
# output_processed = pd.DataFrame(xss_features, columns=utils.column_name)
# output_processed.to_csv(r'C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_raw3_malicious.csv',
#                         index=False,
#                         )
#   -------------------------------------------------------------------------------------------------------------------
#
# df1 = pd.read_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\raw_dataset\XSS_dataset_processed1.csv")
# df2 = pd.read_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\raw_dataset\XSS_dataset_processed2.csv")
# df3 = pd.read_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_raw1.csv")
# df4 = pd.read_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_raw2.csv")
#
# fullDatasetDf = pd.concat([df1, df2, df3, df4])
# print(fullDatasetDf)
# fullDatasetDf.to_csv(r"C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_full.csv", index=False)


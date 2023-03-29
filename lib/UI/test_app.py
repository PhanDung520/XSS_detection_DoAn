import joblib
import lib.features.feature_extraction as featureExtraction
from tkinter import *
import lib.model.utils as utils

# load trainModel
loaded_clf = joblib.load(utils.training_model_file_name)

# tkinter GUI
root = Tk()

root.title('XSS-detection')

canvas = Canvas(root, width=600, height=200)
canvas.pack()

# URL
label = Label(root, text='SCRIPT:', font=1)
canvas.create_window(70, 50, window=label)

entry = Entry(root, width=40, font=1)
canvas.create_window(330, 50, window=entry)


def values():
    global Script
    Script = str(entry.get())

    if loaded_clf.predict([featureExtraction.ftrExtract2(Script)]) == 0:
        Prediction_result = "SCRIPT vừa nhập là Lành tính!"
        label_Prediction = Label(root, text=Prediction_result, fg='green', font=1)
    else:

        Prediction_result = "SCRIPT vừa nhập là XSS!"
        label_Prediction = Label(root, text=Prediction_result, fg='red', font=1)
    canvas.create_window(300, 160, window=label_Prediction)


button = Button(root, text='      Check      ', command=values, bg='blue', fg='black', font=1)
canvas.create_window(300, 110, window=button)

root.mainloop()

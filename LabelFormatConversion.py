import cv2
import os
import glob

labelList = ["car", "bus", "track", "bikeperson", "tricycle", "person"]


def YoloLabelConversion(labelPath, saveDir, imgWidth, imgHight):
    txtList = glob.glob(labelPath + "/" + "*.txt")
    for file in txtList:
        txtName = file.split("/")[-1]
        saveFile = saveDir + os.path.sep + txtName
        wf = open(saveFile, "w")
        with open(file, "r") as f:
            for line in f:
                line = line.split("\n")[0]
                listLen = len(line.split(" "))
                if listLen == 5:
                    label, cx, cy, w, h = line.split(" ")
                elif listLen == 6:
                    label, cx, cy, w, h, prob = line.split(" ")

                labelName = labelList[int(label)]
                left = (float(cx) - float(w) / 2) * imgWidth
                top = (float(cy) - float(h) / 2) * imgHight
                right = (float(cx) + float(w) / 2) * imgWidth
                bottom = (float(cy) + float(h) / 2) * imgHight
                if listLen == 5:
                    writeLabel = str(labelName) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + "\n"
                elif listLen == 6:
                    writeLabel = str(labelName) + " " + str(prob) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + "\n"
                wf.write(writeLabel)


if __name__ == "__main__":
    YoloLabelConversion("/media/linhan/Elements1/交通数据集/data-fix-equal/tianjin-data/tianjin-data-fix-0426/84/day/84-1/0418-0/txt", "./input/detection-results", 1920, 1080)


import cv2

# VideoCaptureのインスタンス作成. 0は内部カメラ
cap = cv2.VideoCapture(0)

while True:
    # 1フレーム読み込む
    ret, frame = cap.read()
    cv2.imshow("Raw Frame", frame)

    # 処理（文字列hoghogeを追加）
    edframe = frame
    cv2.putText(edframe, "hogehoge", (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3, cv2.LINE_AA)

    # キー入力を待ち、k が27(esc)だったらBreak
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリース、windowをすべて閉じる
cap.release()
cv2.destroyAllWindows()

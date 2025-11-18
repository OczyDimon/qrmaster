import cv2
import webbrowser
import time


def main():
    # настройка захвата с камеры
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 24)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    # подключение нужных классов для работы с QR и штрихкодами
    qcd = cv2.QRCodeDetector()
    bd = cv2.barcode.BarcodeDetector()

    # бесконечный цикл обработки кадров с камеры
    while True:
        ret, img = cap.read()

        # попытки распознать QR и штрихкоды
        qr_retval, qr_decoded_info, qr_points, qr_straight_qrcode = qcd.detectAndDecodeMulti(img)

        bc_retval, bc_decoded_info, bc_decoded_type, bc_points = bd.detectAndDecodeMulti(img)

        # если QR-код найден
        if qr_retval:
            print(qr_decoded_info)
            for s, p in zip(qr_decoded_info, qr_points):
                # если QR-код распознан (не просто обнаружен, а распознан) - открыть ссылку
                if s:
                    color = (0, 255, 0)
                    webbrowser.open(qr_decoded_info[0])
                else:
                    color = (0, 0, 255)
                img = cv2.polylines(img, [p.astype(int)], True, color, 8)

        # если штрихкод найден
        if bc_retval:
            print(bc_decoded_info)
            for s, p in zip(bc_decoded_info, bc_points):
                if s:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                img = cv2.polylines(img, [p.astype(int)], True, color, 8)

        # вывод кадра на экран (он будет изменен, если что-то нашлось, иначе - просто кадр с камеры)
        cv2.imshow('QR-code master', img)

        if qr_retval or bc_retval:
            time.sleep(1)

        if cv2.waitKey(10) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

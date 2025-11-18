import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk


def main(main_root):
    def generate_qr():
        url = root.url_entry.get()

        # создание QR-кода
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("temp_qr.png")

        # отображаем QR-код в окне
        img_pil = Image.open("temp_qr.png")
        img_tk = ImageTk.PhotoImage(img_pil)

        root.qr_label.config(image=img_tk)
        root.qr_label.image = img_tk

    # создаем еще одно окно

    root = tk.Toplevel(main_root)

    root.title('QR-code master')

    ttk.Label(root, text='QR-code master.').pack()

    tk.Label(root, text="Введите ссылку:").pack(pady=5)

    # окошко для ввода ссылки
    root.url_entry = tk.Entry(root, width=40)
    root.url_entry.pack(pady=5)

    # кнопка для генерации QR-кода
    tk.Button(root, text="Сгенерировать", command=generate_qr).pack(pady=10)

    # место для вывода QR-кода (изначально пустое)
    root.qr_label = tk.Label(root)
    root.qr_label.pack(pady=10)

    root.geometry('800x600')

    root.mainloop()


if __name__ == '__main__':
    main(None)

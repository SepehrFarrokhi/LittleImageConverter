import sys
import os
from PIL import Image, ImageOps


def main():
    try:
        if len(sys.argv) != 3:
            sys.exit("Usage: python program.py input output")

        input_path = sys.argv[1]
        output_path = sys.argv[2]

        # If input is a single file
        if os.path.isfile(input_path):
            check_extension(input_path)
            check_extension(output_path)
            process_single(input_path, output_path)

        # If input is a folder
        elif os.path.isdir(input_path):
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            process_folder(input_path, output_path)

        else:
            sys.exit("Input path is not a valid file or folder.")

    except FileNotFoundError:
        sys.exit("File not found.")


def check_extension(filename):
    ext = filename.split(".")[-1].lower()
    if ext not in ["jpg", "jpeg", "png", "webp"]:
        sys.exit("File must end with .jpg, .jpeg, .png or .webp")
    return ext


def process_single(input_img, output_img):
    sample = Image.open("Sample.png").convert("RGBA")
    sample = ImageOps.fit(sample, (800,800))
    img = image_resizer(input_img, sample)
    img.paste(sample, mask=sample)
    img = img.convert("RGB")
    img.save(output_img, "JPEG")


def process_folder(input_folder, output_folder):
    sample = Image.open("Sample.png").convert("RGBA")
    sample = ImageOps.fit(sample, (800, 800))

    for filename in os.listdir(input_folder):
        path = os.path.join(input_folder, filename)

        if not os.path.isfile(path):
            continue  

        ext = filename.split(".")[-1].lower()
        if ext not in ["jpg", "jpeg", "png", "webp"]:
            continue  

        img = image_resizer(path, sample)
        img.paste(sample, mask=sample)

        out_file = os.path.join(output_folder, filename[:len(filename)-len(ext)-1]+".jpg")
        img = img.convert("RGB")
        img.save(out_file, "JPEG")

    print("Done processing folder.")


def image_resizer(img1, sample):
    img1 = Image.open(img1)
    return ImageOps.fit(img1, sample.size)
# hwkpppp memeeeeee

if __name__ == "__main__":
    main()

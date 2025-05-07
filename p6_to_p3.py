def convert_p6_to_p3(input_path, output_path):
    with open(input_path, "rb") as f:
        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("Not a valid P6 PPM file")

        def read_next_value(file):
            while True:
                line = file.readline()
                if not line:
                    raise ValueError("Unexpected end of file")
                line = line.strip()
                if line.startswith(b'#') or line == b'':
                    continue
                return line

        size_line = read_next_value(f)
        width, height = map(int, size_line.split())
        maxval_line = read_next_value(f)
        maxval = int(maxval_line)

        pixel_data = f.read()
        expected_length = width * height * 3
        if len(pixel_data) < expected_length:
            raise ValueError(f"Incomplete pixel data: expected {expected_length}, got {len(pixel_data)}")

    with open(output_path, "w") as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{maxval}\n")

        for i in range(0, expected_length, 3):
            r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")


if __name__ == "__main__":
    convert_p6_to_p3("/home/s32217540/colorP6File.ppm", "/home/s32217540/convertedP3.ppm")

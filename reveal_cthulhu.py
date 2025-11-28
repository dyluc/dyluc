from PIL import Image
from datetime import datetime
import numpy as np
import calendar

def crossfade(img_a_path, img_b_path, frame_index, total_frames, output_path):
    a = Image.open(img_a_path).convert("RGBA")
    b = Image.open(img_b_path).convert("RGBA")

    a_arr = np.array(a).astype(float)
    b_arr = np.array(b).astype(float)

    t = frame_index / (total_frames - 1)
    blended = (1 - t) * a_arr + t * b_arr
    blended = blended.clip(0, 255).astype("uint8")

    frame = Image.fromarray(blended, mode="RGBA")
    frame.save(output_path)

if __name__ == "__main__":
    today = datetime.today()
    year, month, day = today.year, today.month, today.day

    total_days = calendar.monthrange(year, month)[1]
    frame_index = day - 1

    crossfade(
        img_a_path="cthulhu1banner.png",
        img_b_path="cthulhu2banner.png",
        frame_index=frame_index,
        total_frames=total_days,
        output_path="frame.png"
    )

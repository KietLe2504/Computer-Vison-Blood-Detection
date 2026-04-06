import json
import csv
import os

def convert_json_to_csv(json_path, csv_path, image_name):
    with open(json_path, 'r') as f:
        data = json.load(f)

    rows = []

    for obj in data["objects"]:
        label = obj["classTitle"].lower()  # "RBC" -> "rbc"
        
        (xmin, ymin), (xmax, ymax) = obj["points"]["exterior"]

        rows.append([
            image_name,
            xmin,
            ymin,
            xmax,
            ymax,
            label
        ])

    # ghi CSV
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["image", "xmin", "ymin", "xmax", "ymax", "label"])
        writer.writerows(rows)

    print(f"Saved to {csv_path}")

def batch_convert(folder, output_csv):
    all_rows = []

    for file in os.listdir(folder):
        if file.endswith(".json"):
            json_path = os.path.join(folder, file)
            image_name = file.replace(".json", ".png")

            with open(json_path, 'r') as f:
                data = json.load(f)

            for obj in data["objects"]:
                label = obj["classTitle"].lower()
                (xmin, ymin), (xmax, ymax) = obj["points"]["exterior"]

                all_rows.append([
                    image_name,
                    xmin,
                    ymin,
                    xmax,
                    ymax,
                    label
                ])

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["image", "xmin", "ymin", "xmax", "ymax", "label"])
        writer.writerows(all_rows)

    print("Done!")

# dùng
batch_convert("dataset/BDDC/val/ann", "annotations_eval.csv")

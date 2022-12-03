import pdfplumber
import csv, os, argparse

def process(input, output, password):
    pdf = pdfplumber.open(input, password=password)
    pages = pdf.pages
    
    txns = []
    
    for page in pages:
        if page.extract_text().find("Value Date") > 0:
            for (index, row) in enumerate(page.extract_table()):
                if index == 0 or row[0] == "" or row[0] == None or row[0] == "Date" or row[8] == None:
                    continue

                txns.append({
                    "date": row[0].replace("null",""),
                    "description": row[2],
                    "amount": row[6] if row[7] == "" else row[7],
                    "type": "Dr" if row[7] == "" else "Cr"
                })
        

    print("Processed ")

    # Output to CSV
    fields = ["date", "description", "amount", "type"]
    with open(output, 'w') as file:
        writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL, fieldnames=fields)
        writer.writeheader()

        for row in txns:
            writer.writerow({ key: row[key] for key in fields })


def main(args):
    for file_name in os.listdir(args.in_dir):
        root, ext = os.path.splitext(file_name)
        if ext.lower() != '.pdf':
            continue

        pdf_path = os.path.join(args.in_dir, file_name)

        out_name = root + '.csv'
        out_path = os.path.join(args.out_dir, out_name)

        print(f'Processing: {pdf_path}')
        process(pdf_path, out_path, args.password)
        print(f'Output file: {out_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-dir', type=str, required=True, help='directory to read statement PDFs from.')
    parser.add_argument('--out-dir', type=str, required=True, help='directory to store statement CSV to.')
    parser.add_argument('--password', type=str, default=None, help='password for the statement PDF.')
    args = parser.parse_args()

    main(args)
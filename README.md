# Federal Bank Account Statement Parser

This script will help you copy structured data from your account statements, which is in protected PDFs.

### Inspired from:
Repo: https://github.com/xaneem/hdfc-credit-card-statement-parser

## Usage
1. Initialise your anaconda venv (optional)
    ```
    $ conda activate <YOUR-ENV>
    ```

2. Install requirements
    ```
    $ pip install -r requirements.txt
    ```

3. Copy your statement PDFs to `./input/` folder

4. Update the password in `run.sh`
    ```
    --password=ABCD1234
    ```

5. Run the script `./run.sh`

    Sample output:
    ```
    Processing: ./input/BANK-STATEMENT.PDF
    Processed
    Output file: ./output/BANK-STATEMENT.csv
    ```

6. Cross check the data and make sure the extracted information is correct.

# get_peptide
The script fetches information about a peptide from the UniProt database and writes it to a file. The information that is extracted includes the peptide name, the organism, and any OpenTargets identifiers.

## Prerequisites
- Python 3.x
- `unipressed` library:
https://github.com/multimeric/Unipressed

## Installation
```bash
pip install unipressed 
```

## Usage/Examples
To run the script, use the following command in the terminal:

```javascript
python get_peptide_info.py <uniprot_id>
```
where `<uniprot_id>` is the UniProt ID of the protein you want to fetch information for. This will create a file named `<uniprot_id>.out.txt` in the current working directory containing the extracted information.

Note: The script expects exactly one argument (the UniProt ID), and will print a usage message if no argument is given or if more than one argument is given.

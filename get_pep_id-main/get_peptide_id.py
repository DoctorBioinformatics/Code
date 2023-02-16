#!/usr/bin/env python
import sys
from unipressed import UniprotkbClient

def get_peptide_info(uniprot_id):
    """
    This script fetches information about a protein from the UniProt database and writes it to a file.
    The information that is extracted includes the protein name, the organism, and any OpenTargets identifiers.
    The output is written to a file named <uniprot_id>.out.txt in the current working directory.
    """
    # Fetch the record for the given UniProt ID
    record = UniprotkbClient.fetch_one(uniprot_id)

    # Extract the protein name, organism, and OpenTargets identifier from the record
    protein_name = record.get('proteinDescription', {}).get('recommendedName', {}).get('fullName', {}).get('value',{})

    organism = record.get('organism', {}).get('scientificName')

    open_target_records = []
    for key in record.get('uniProtKBCrossReferences',[{}]):
        if key.get('database') == 'OpenTargets':
            open_target_records.append(key.get('id'))

    # Convert open_target_records list to a string
    open_target_records_str = ", ".join(open_target_records)

    # Write the extracted information to a file
    with open(uniprot_id+'.out.txt', "w") as f:
        f.write(f"Protein Name: {protein_name}\n")
        f.write(f"Organism: {organism}\n")
        f.write(f"OpenTargets Identifier: {open_target_records_str}\n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: get_peptide_info.py <uniprot_id>")
        sys.exit(1)
    uniprot_id = sys.argv[1]
    get_peptide_info(uniprot_id)

amino_acid_dict = {"ALA":"A", "ARG":"R", "ASP":"D", "ASN":"N","CYS":"C", "GLU":"E", "GLN":"Q", "GLY":"G", "HIS":"H", "ILE":"I", "LEU":"L", "LYS":"K", "MET":"M", "PHE":"F", "PRO":"P", "SER":"S", "THR":"T", "TRP":"W", "TYR":"Y", "VAL":"V"}

converter = input("Which converter do you want to use?\nFor three letters to one letter, type '321'\nFor one letter to three letters, type '123': ")


def convert_to_one():
  peptide = input("Enter amino acid sequence in the form of 'Gly-Arg-...' etc: ")
  
  peptide_list = peptide.upper().split("-")
  new_peptide_list = []
  for aa in peptide_list:
    new_peptide_list.append(amino_acid_dict[aa])
  new_string_peptide = ",".join(new_peptide_list)
  return print(new_string_peptide)



def convert_to_three():
  new_amino_acid_dict = dict(zip(amino_acid_dict.values(),amino_acid_dict.keys()))
  #print(new_amino_acid_dict)
  peptide = input("Enter amino acid sequence in the form of 'G,A,P...' etc: ")
  new_peptide = peptide.upper().split(',')
  new_peptide_list = []
  for aa in new_peptide:
    new_peptide_list.append(new_amino_acid_dict[aa])
  new_peptide_string = "-".join(new_peptide_list)
  return print(new_peptide_string.title())
  
if converter == '321':
  convert_to_one()
elif converter == '123':
  convert_to_three()
else:
  print("Please type a valid response.")


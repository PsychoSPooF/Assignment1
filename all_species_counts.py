import os;
import fnmatch;
filelist=[]
for filename in os.listdir('./'):
    if fnmatch.fnmatch(filename, 'data_*.txt'):
		allfiles=filelist.append(filename);
print(filelist);
os.system("python species_counts.py "+" ".join(filelist)+" > all_species_counts.txt");
print("----All Species Count----");
os.system("cat all_species_counts.txt");

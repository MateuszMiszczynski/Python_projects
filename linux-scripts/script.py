# In certain dir find how many lines with "WARNING" does all files have in it
import os

dir = "/home/vboxuser/test/log/"
warning_counts = {}

# Iteracja przez pliki w katalogu
for filename in os.listdir(dir):
    fullpath = os.path.join(dir, filename)

    # Sprawdzanie, czy jest to plik
    if os.path.isfile(fullpath):
        warning_count = 0

        try:
            with open(fullpath, "r", encoding="utf-8") as f:
                # Iteracja przez linie w pliku
                for line in f:
                    warning_count += line.count("WARNING")
        except (UnicodeDecodeError, OSError):
            # Obsługuje błędy związane z odczytem pliku
            continue

        # Zapisanie wyniku w słowniku
        warning_counts[filename] = warning_count

# Wydrukowanie wyników
print(warning_counts)

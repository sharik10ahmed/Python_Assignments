def copy_odd_lines(file1, file2):
    # Open source file for reading and destination file for writing
    with open(file1, "r") as f_in, open(file2, "w") as f_out:
        line_no = 1
        for line in f_in:
            # If line number is odd, write it to file2
            if line_no % 2 != 0:
                f_out.write(line)
            line_no += 1

# Example usage
src = "file1.txt"
dst = "file2.txt"
copy_odd_lines(src, dst)
print("Odd-numbered lines copied from file1 to file2.")

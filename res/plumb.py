import pdfplumber
import sys
import psycopg2

# Try to connect

try:
    conn = psycopg2.connect("dbname=CADW user=postgres password=09211290 host=localhost port=5433")
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()

with pdfplumber.open(sys.argv[1]) as pdf:
    first_page = pdf.pages[1]

    # Everything is in a PDF form, so these may not return anything!
    # print(first_page.chars[0])
    # print("TEXT:\n", first_page.extract_text())
    # print("WORDS:\n", first_page.extract_words())
    # print("TABLES:\n", first_page.extract_tables())

    # Requires additional libraries around magickwand.
    # im = first_page.to_image(resolution=150)
    # im.save("first_page", format="PNG")

    fields = pdf.doc.catalog["AcroForm"].resolve()["Fields"]  # Get only form fields.

    form_data = set()

    for field in fields:
        this_field = field.resolve()  # Get the thing.

        field_type = this_field.get("FT", "NA").name  # This is a pdfminer.psparser.PSLiteral with a name property.
        field_name = this_field.get("T", b"NA").decode()  # Name and Values seem to be byte encoded strings.
        field_value = this_field.get("V", b"NA").decode("unicode_escape")  # To handle unicode em-dash in PDF.
        field_options = this_field.get("Opt", [])

        # Only interested in the choice field types.
        if field_type == "Ch":
            # print("FORM FIELD: [", field_type, "]", field_name, " -> ", [x.decode() for x in field_options])
            for this_option in field_options:
                this_option = this_option.decode().strip()
                if len(this_option) > 3:
                    # print("COURSE:", this_option)
                    form_data.add((this_option[:6].strip(), this_option[6:16].strip(), this_option[16:].strip()))
        # else:
        #     print("FORM FIELD: [", field_type, "]", field_name, " -> ", field_value)
sorted_data = sorted(form_data, key=lambda course: course[2])  # Sorted by course name
for thisclass in sorted_data:
    cur.execute("INSERT INTO accounts_availableCourses(coursecredit, courseid, coursename) VALUES(%s,%s,%s)", thisclass)
conn.commit()
cur.close()
conn.close()

print(*sorted_data, sep="\n")

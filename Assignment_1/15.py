# Q2. Customer Data Cleaning 
lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]

def clean_customer(raw):
    # Split the record
    fields = raw.split(';')
    
    # Check exactly 4 fields
    if len(fields) != 4:
        return None

    # Remove extra spaces
    name = fields[0].strip()
    email = fields[1].strip()
    phone = fields[2].strip()
    city = fields[3].strip()

    # A. Validate Name
    name = name.title()
    words = name.split()
    if len(words) == 0:
        return None
    for word in words:
        for ch in word:
            if not ch.isalpha():
                return None

    # Validate City
    if city == '':
        return None
    city = city.title()
    
    # B. Validate Email
    email = email.lower()
    if email.count('@') != 1:
        return None
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    if username == '':
        return None
    if '.' not in domain:
        return None
    if domain.startswith('.') or domain.endswith('.'):
        return None

    # C. Validate Phone Number
    phone = phone.replace(' ', '')
    phone = phone.replace('-', '')
    if phone.startswith('+91'):
        phone = phone[3:]
    elif len(phone) == 12 and phone.startswith('91'):
        phone = phone[2:]

    # Check phone number
    if len(phone) != 10:
        return None
    for digit in phone:
        if not digit.isdigit():
            return None
    if phone[0] not in '6789':
        return None
        
    # Return valid customer dictionary
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }

# Main Program
rejected = 0
for record in lines:
    result = clean_customer(record)
    if result is not None:
        print(result)
    else:
        rejected += 1
print("Rejected:", rejected)
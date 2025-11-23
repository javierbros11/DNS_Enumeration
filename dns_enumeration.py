import dns.resolver

# Definimos el nombre de dominio

target_domain = str(input("Dime un nombre de dominio: "))
record_types = ["A","AAAA","CNAME","MX","NS","SOA","TXT"]

# Creamos un DNS resolver

resolver = dns.resolver.Resolver()

for record_type in record_types:
    try:
        answers = resolver.resolve(target_domain, record_type)
    except dns.resolver.NoAnswer:
        continue

    # Mostramos la información del registro
    print(f"{record_type} registros para {target_domain}")
    for data in answers:
        print(f" {data}")
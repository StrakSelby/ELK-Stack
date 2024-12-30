import client, inserting, mapping, output

def main():
    client.get_client()
    inserting.insert_document()
    mapping.create_mapping()
    output.total_documents()
    output.print_all_documents()
if __name__ == "__main__":
    main()

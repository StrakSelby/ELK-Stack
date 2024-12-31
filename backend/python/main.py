import client, inserting, mapping, output, updating

def main():
    client.get_client()
    inserting.insert_document()
    # mapping.create_mapping()
    output.total_documents()
    output.print_all_documents()
    updating.update_existing_field()
    output.print_all_documents()
if __name__ == "__main__":
    main()

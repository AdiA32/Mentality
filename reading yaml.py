import yaml

with open(r"quotes.yaml") as file:
    quote_file = yaml.safe_load(file)
    print(quote_file)

    # for item, doc in quote_file.items():
    #     print(item)
    #     for ting in doc:
    #         print("---\n",ting)
    print(quote_file["quotes"][5])

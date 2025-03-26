def markdown_to_blocks(raw_string):
    blocks = raw_string.split("\n\n")
    list_blocks = []
    for all in blocks:
        if all == "":
            continue
        all = all.strip()
        list_blocks.append(all)
    return list_blocks
        
                        
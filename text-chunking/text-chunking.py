def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    if not tokens:
        return []
        
    res = []
    i = 0
    step = chunk_size - overlap
    
    while i < len(tokens):
        chunk = tokens[i : i + chunk_size]
        res.append(chunk)
        if i + chunk_size >= len(tokens):
            break
            
        i += step
        
    return res
        
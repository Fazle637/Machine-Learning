def is_positive_review_rule_based(review_text):

    positive_keywords = ["great", "love", "excellent", "recommend"]
    review_lower = review_text.lower()

    for word in positive_keywords:
        if word in review_lower:
            return True
    return False

if __name__=="__main__":
    test_reviews = [
        "I absolutely love this product! It works perfectly",
        "The item arrived late and was broken. Very disappointing.",
        "It's okay, does the jib but nothing excellent or great about it."
    ]    
    
    for review in test_reviews:
        result = is_positive_review_rule_based(review)
        print(f"Review: {review}")
        print(f"Positive? {result}\n")    
        


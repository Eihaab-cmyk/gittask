def unique_word_analyzer():
    para1 = input("Enter first paragraph:\n").lower()
    para2 = input ("Enter second paragraph:\n").lower()

    words1 = set(para1.split())
    words2 = set(para2.split())

    print("\n--- Word Analysis ---")
    print("🔹 Unique words in paragraph 1:", words1)
    print("🔹 Unique words in paragraph 2:", words2)
    print("🔸 Common words:", words1 & words2)
    print("⚡ Words only in paragraph 1:", words1 - words2)
    print("⚡ Words only in paragraph 2:", words2 - words1)
    print("🌍 All distinct words:", words1 | words2)
unique_word_analyzer()
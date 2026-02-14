import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# FAQ Data
faqs = {
    "What is CodeAlpha?": "CodeAlpha is a software development company offering internships.",
    "What is this internship about?": "This internship focuses on Artificial Intelligence projects.",
    "Will I get a certificate?": "Yes, you will receive a QR verified completion certificate.",
    "Is this internship paid?": "This internship is unpaid but provides learning and certification benefits.",
    "How many tasks are required?": "You must complete at least two tasks to receive the certificate."
}

questions = list(faqs.keys())
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def chatbot():
    print("=== FAQ Chatbot ===")
    print("Type 'exit' to end the chat\n")

    while True:
        user_query = input("You: ")

        if user_query.lower() == "exit":
            print("Chatbot: Thank you! Goodbye.")
            break

        user_vector = vectorizer.transform([user_query])
        similarity = cosine_similarity(user_vector, question_vectors)
        best_match = similarity.argmax()

        if similarity[0][best_match] > 0.2:
            print("Chatbot:", answers[best_match])
        else:
            print("Chatbot: Sorry, I couldn't understand your question.")

if __name__ == "__main__":
    chatbot()

from io import StringIO
import os
import fitz
import openai
from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize

load_dotenv()


def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as infile:
        return infile.read()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")


def read_pdf(filename):
    context = ""

    # Open the PDF file
    with fitz.open(filename) as pdf_file:
        # Get the number of pages in the PDF file
        num_pages = pdf_file.page_count

        # Loop through each page in the PDF file
        for page_num in range(num_pages):
            # Get the current page
            page = pdf_file[page_num]

            # Get the text from the current page
            page_text = page.get_text().replace("\n", "")

            # Append the text to context
            context += page_text
    return context


def split_text(text, chunk_size=5000):
    chunks = []
    current_chunk = StringIO()
    current_size = 0
    sentences = sent_tokenize(text)
    for sentence in sentences:
        sentence_size = len(sentence)
        if sentence_size > chunk_size:
            while sentence_size > chunk_size:
                chunk = sentence[:chunk_size]
                chunks.append(chunk)
                sentence = sentence[chunk_size:]
                sentence_size -= chunk_size
                current_chunk = StringIO()
                current_size = 0
        if current_size + sentence_size < chunk_size:
            current_chunk.write(sentence)
            current_size += sentence_size
        else:
            chunks.append(current_chunk.getvalue())
            current_chunk = StringIO()
            current_chunk.write(sentence)
            current_size = sentence_size
    if current_chunk:
        chunks.append(current_chunk.getvalue())
    return chunks


filename = os.path.join(os.path.dirname(__file__), "filename.pdf")
document = read_pdf(filename)
chunks = split_text(document)

text = """Il était une fois, dans un joli jardin, un jardinier nommé Pierre
qui avait une passion pour les plantes. Pierre était connu
pour ses compétences exceptionnelles en jardinage.
Dans son jardin, il possédait de nombreux outils, mais il avait
un sécateur qu'il considérait comme son préféré. Ce sécateur avait
 été fabriqué avec soin et avait une lame tranchante et une prise ergonomique.
Chaque jour, Pierre utilisait son sécateur pour tailler
les rosiers, les buissons, et même les arbres fruitiers.
 Il avait d'autres outils, bien sûr, mais il préférait
le sécateur pour sa précision et sa facilité d'utilisation.
Il savait exactement comment l'utiliser pour obtenir les
meilleurs résultats. Un jour, un voisin curieux, Thomas,
vint lui rendre visite. Thomas observa Pierre en train de
travailler et lui demanda :

— "Pierre, pourquoi utilises-tu toujours ce sécateur,
même quand il y a d'autres outils disponibles ?"

Pierre sourit et répondit :

— "Chaque outil a son usage spécifique, mais ce sécateur est
comme une fonction préférée dans un programme. Il est particulièrement
adapté pour les tâches de taille fine. Quand je l'utilise, je sais que
je vais obtenir le meilleur résultat avec un minimum d'effort. C'est comme
une fonction dans le code : elle est spécialement conçue pour faire un travail
particulier de manière efficace."

Thomas réfléchit à cela et comprit. Il se rendit compte que dans son propre
jardin, il avait également des outils qui étaient plus adaptés à
certaines tâches que d'autres."""


def gpt3_completion(question):
    # Appelle ChatCompletion de l'API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Using this text: " + text},
            {"role": "user", "content": question},
        ],
    )

    # Extraction du texte de la réponse
    return response.choices[0].message.content


# Exemple d'utilisation
question = "resumes moi ça ?"
response = gpt3_completion(question)
print(response)


def ask_question_to_pdf(question):
    return gpt3_completion(question)


ask_question_to_pdf(question)

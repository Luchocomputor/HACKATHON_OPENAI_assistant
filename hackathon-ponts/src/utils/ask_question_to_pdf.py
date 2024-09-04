from io import StringIO
import os
import fitz
import openai
from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize
from openai import OpenAI

client = OpenAI()

load_dotenv()

text = """[Paroles de "Kalash" ft. Kaaris]

[Intro : Booba]
Sors les Kalash' comme à Marseille
Bah ouais, Morray
Izi

[Couplet 1 : Booba]
Tes négros n'ont pas d'oseille, dans la street tout se monnaye
Les vrais savent, on se connaît, anti-hess, on se connecte
J'ai des gros bras, la chatte à Popeye, crache-moi d'ssus, j'te lance une bouteille
Difficilement je trouve le sommeil, menton pointé vers le soleil
M.O.L.O.T.O.V cocktail, j'te baise, j'te laisse à l'hôtel
J'passe au Lamborghini, Maybach, Phantom, tu restes à l'Opel
J'suis dans l'textile Sonia Rykiel, j'gère l'biz à l'américaine
J'me taperais bien une Dominicaine, j'la mettrais ien-b tout le week-end
J'la mettrais ienb' tout le week-end, downtown, j'ai vue sur Brickell
WAllah j'suis frais, j'suis nickel, tirelire est pleine, j'ai haine habituelle
J'parle d'homme à romanichel, t'as l'swag à Sacha Distel
Fortuné tah Elf Aquitaine, t'es sur le banc, j'suis capitaine

[Refrain : Booba & Kaaris]
Montre en diamants, lunettes de soleil
Sors les Kalash' comme à Marseille
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
J'vais faire de tout cet oseille ? J'vais faire de tout cet oseille ?
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
Moi et mes kheys on part sur la Lune, amuse-toi bien en Meurthe-et-Moselle
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
J'vais faire de tout cet oseille ? (Kaaris) J'vais faire de tout cet oseille ? (Kaaris)
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ? (Orh Click)

[Couplet 2 : Kaaris]
2.7.0 toujours plus haut, la République me suce le tuyau
Monsieur l'agent j’t'enfonce le triangle (Sevran !), et le gilet fluo
J'veux faire des sous mais j'suis paresseux, j'aime pas ta gueule, j'te baise ta reu-ssœu
J'n'ai qu'confiance qu'en mon Desert Eagle et en Zizou dans les arrêts d'jeu
Elle est dans la chambre, elle est sous les draps (uh-hum), j'ai des jambes à la place des bras
Elle pense que j'suis en train d'la doigter (uh-hum), j'lui mets mon gros doigt d'pied
Mes deux questions préférées : qu'est-ce j'vais faire de tous ces deniers ?
Si j'te fends le crâne en deux, quel œil va s'fermer le premier ?
Continue à glousser, j'te fume et j'roule un trois feuilles
Tes ongles continuent à pousser tu pourras griffer ton cercueil (2.7)
J'ai la prose qui tue et, même ton corps reconstitué
On n'sait toujours pas qui tu es, ta grand-mère la prostituée

[Refrain : Booba]
Montre en diamants, lunettes de soleil
Sors les Kalash' comme à Marseille
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
J'vais faire de tout cet oseille ? J'vais faire de tout cet oseille ?
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
Moi et mes kheys on part sur la Lune, amuse-toi bien en Meurthe-et-Moselle
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
J'vais faire de tout cet oseille ? J'vais faire de tout cet oseille ?
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?

[Couplet 3 : Booba]
J'ramasse deux-trois galériennes, partie de jambes en l'air
Punchline anti-aérienne, si j'lâche des paroles en l'air
Laisse tomber morray, c'est la guerre, le motif du crime, c'est la 'sère
Nique sa mère, même une sexagénaire, la juge m'a dit que j’exagère
Mais nique sa mère là-celle aussi, son arrière grand-mère aussi
Rien à envier à ces hommes, leur meuf est bonne, la mienne aussi
Scène du crime c'est moi l'reur-ti, j'suis en couleur, t'es mal sorti
J'suis Marlo Stanfield, ta mère la hyène, t'es McNulty
J'te nique ta life gratuit, y a pas d'quoi, j'suis l'meilleur, cela va d'soi
B.2.O.B.A. escroc mafieux comme Cha-arles Pasqua
Vulgaires fautes de grammaire, sirote du Jack, de grosses mamelles
J'voyage en jet, prends l'Eurotunnel, j'me sens comme dans la chatte à ta mère
[Refrain : Booba]
Montre en diamants, lunettes de soleil
Sors les Kalash' comme à Marseille
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
J'vais faire de tout cet oseille ? J'vais faire de tout cet oseille ?
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
Moi et mes kheys on part sur la Lune, amuse-toi bien en Meurthe-et-Moselle
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille ?
J'vais faire de tout cet oseille ? J'vais faire de tout cet oseille ?
Ma question préférée : qu'est-ce j'vais faire de tout cet oseille, huh ?

[Outro]
Back to the Future
"""

# question = "Donne moi la meilleure punchline de ce texte"


def gpt3_completion(question, text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant and you will answer according to the informations included in this text :" + chunks[0] },
            {"role": "system", "content": "You MUST answer like TONY MONTANA "},
            {"role": "user", "content": question},
            # {"role": "assistant", "content": text},
            # {"role": "user", "content": "Where was it played?"}
        ],
    )
    return response.choices[0].message.content


def ask_question_to_pdf(question):
    return gpt3_completion(question, text)


"""""

def gpt3_completion(question):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
        #{"role": "assistant", "content": text},
        #{"role": "user", "content": "Where was it played?"}        
    ]
)
    return(response.choices[0].message.content)
def ask_question_to_pdf(question):
    return gpt3_completion(question)
""" ""


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
# print(chunks[0])
# print(ask_question_to_pdf(question))

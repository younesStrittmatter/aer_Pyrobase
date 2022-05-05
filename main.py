import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

# credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# get db
db = firestore.client()

# get collection ref
trial_sequences_ref = db.collection(u'trial_sequences')

# example sequences
trial_sequence_1 = {'sequence': [{'color': 'red', 'word': 'red'}, {'color': 'green', 'word': 'red'}], 'used': 'false'}
trial_sequence_2 = {'sequence': [{'color': 'green', 'word': 'red'}, {'color': 'green', 'word': 'green'}],
                    'used': 'false'}

# push sequences into db
trial_sequences_ref.add(trial_sequence_1)  # add sequences
trial_sequences_ref.add(trial_sequence_2)

# get sequences where condition is met
docs = trial_sequences_ref.where(u'used', u'==', 'false').stream()

# get random doc
random_doc = random.choice([{'id': doc.id, 'sequence': doc.to_dict()['sequence']} for doc in docs])


# set used to true
trial_sequences_ref.document(f'{random_doc["id"]}').update({u'used': 'true'})

docs_all = trial_sequences_ref.stream()

for doc in docs_all:
    print(doc.to_dict())
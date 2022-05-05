"# aer_Pyrobase"
AER- First steps and example for experimentalist side of database communication with firebase. Setting up an experiment and hosting with firebase will come soon.
Questions: 
- Realtime database or firestore?
- One database for all data (meta-data, trial-sequences, participant-data)
- The hosting of the experiment can be done via firebase or via other means the only importand thing is, that data get stored into a database for the theorist and that data      trial-sequences are retrieved from the database. How much 'handholding' do we want to do for hosting or should we let users use their own solution?

Steps to make this example work:
- Create an account in Firebase,
- go to Firebase Console and create a new project, 
- setting up Private Key file:
  Project settings (gear wheel) -> service accounts -> Generate new private key.
  This will let you download the JSON file. (name it serviceAccountKey.json and copy it into the directory where main.py is) 
- Create firestore database
- create new collection 'trial_sequence'

Install python modules:
pip install firebase_admin

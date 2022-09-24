import warnings
warnings.filterwarnings("ignore")
from parakeet import Parakeet

parakeet = Parakeet()
sequences = [
    "Health professionals say there is no rabies vaccine for humans in Zimbabwe and, even if it was available, it is too expensive for most bitten by infected dogs.",
    "What is the difference in demand and salary for Data Scientist vs Data Engineer?",
    "The first recorded use of Rose Vale as the color name in English was in 1923.",
    "The election of the Oldham Metropolitan Borough Council in 1999 took place on 6 May 1999 to elect the members of the Oldham Council in Greater Manchester, England.",
    "Keeping your dog safe is very important for us.",
    "In fact, it wouldn't be wrong to claim that the success and failure of your campaigns hinge on the email marketing software you choose to employ.",
    "Make text lighthearted by putting yourself in your customer's shoes."
]
for sequence in sequences:
    print("_"*50)
    print(f"Input Sequence: {sequence}")
    result = parakeet.rephrase(sequence)
    for index,(i,j) in enumerate(result.items()):
        print(f"\tOutput Sequence {index}: {i}")
        print(f"\tAdequacy: {j['adequacy']}")
        print(f"\tDiversity: {j['diversity']}")
    print()
    print("#"*50)
    print()
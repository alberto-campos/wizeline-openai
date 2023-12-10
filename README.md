# wizeline-openai
OpenAI Wizeline Sprint December 2023

# WordWize Refiner
Do you ever feel inspired and creative, really wanting to express your ideas, but sense the need to slow down or suppress thoughts just because you fear people won't understand your accent? Well, who cares! Just say it anyway and we'll take care of the rest!

# App's Purpose
Our OpenAI tool analyzes transcripts from Spanish-speaking users and recommends a more natural English version that emphasizes native language usage and semantics. Additionally, it highlights common mistakes, providing a brief explanation along with a recommendation.

Example:

**User Input:** Hello everyone, my name is Mr. Rodrigo Rodriguez. Hope your doing well. How do you call that? I want to make sure because I don't want to do a mistake. The bus is late, no? I guess is not good that the bus is always late.

**AI Output:** 
Hello, Mr. Rodrigo Rodriguez! It's great that you're learning English and seeking to improve your language skills. Firstly, "How do you call that?" might not sound very natural. A more commonly used phrasing would be "What do you call that?" or "What is that called?" When you said "I want to *make sure* because I don't want to *do* a mistake," The more natural way to phrase it is "I want to *be sure* because I don't want to *make* a mistake" Using 'make' and 'do' can be quite tricky in English, just like using 'ser' and 'estar' in Spanish.


# Installation and Requirements
Make sure you have a relatively recent Python version. For testing purposes, we don't need the latest.

`python --version`

Sample output:
```
Python 3.10.4
```

Clone this repository
`gh repo clone alberto-campos/wizeline-openai`

Create an OPENAI_API_KEY key
`echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc`

`source ~/.zshrc`

Confirm your environment key was setup correctly
`echo $OPENAI_API_KEY`

Navigate to the `capstone_project` directory

Install required packages
`pip install -r requirements.txt`

Create a Python virtual environment
`python3 -m venv .venv`

Activate this recently craated environment
`source .venv/bin/activate`

Install Jupyter
`pip install notebook ipywidgets`

Open Jupyter
`jupyter notebook`

Import packages
`pip install numpy openai`

Run the app:
`python main.py`

## Optional/Troubleshooting
You may need to upgrade openAI
`openai migrate`
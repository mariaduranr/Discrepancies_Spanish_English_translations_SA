# Discrepancies_Spanish_English_translations_SA
This project quantifies sentiment alignment between original and translated texts using a Sentiment Analysis ML algorithm. It sets a threshold for discrepancies, triggering a notification for human review if exceeded. This helps ensure translations maintain the intended tone and context.

# Project Directory Structure

### `dataset_creation/`
Contains resources and scripts used to create the datasets required for the project.

### `idioms_web_scraping/`
Includes Python scripts and Jupyter notebooks for web scraping to create datasets of idioms.

### `random_select_podcast/`
Features a Jupyter notebook outlining the method for randomly selecting podcast titles in Spanish. Manual selection was needed due to missing transcripts.

### `transcripts/`
Contains a Python script with transcript text and a notebook, `podcast_to_csv.ipynb`, for chunking and organizing transcripts into structured datasets.

### `translations_deeptranslator/`
Holds tools and notebooks used for translating datasets with the DeepTranslator service.

### `translations_gpt4/`
Contains CSV files with translations done using GPT-4, manually transcribed by a GPT plugin assistant.

### `gpt_assistant/`
Stores two videos demonstrating the fine-tuning and testing for the creation of the GPT-4 assistant.

### `mast_distilbert/`
Includes materials related to using DistilBERT for sentiment analysis, with scripts, results datasets, and performance metrics.

### `sc_pysentimiento/`
Contains scripts and notebooks for sentiment analysis using PySentimiento, optimized for both Spanish and English. Includes scripts, results datasets, and performance metrics.

## Additional Documentation
Each code file is annotated with comments for clarity. For more details on data sources, structures, and methodologies, please refer to the individual files and directories. See the report for a detailed explanation.

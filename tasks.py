# tasks.py
from celery import Celery
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

app = Celery('tasks')
app.config_from_object('celery_config')

@app.task
def run_colab_file():
    # Specify the path to your Jupyter Notebook (.ipynb file)
    notebook_path = 'D:\PROJECTS\EDI PROJECT\back-end\edi_.ipynb'

    # Read the notebook content
    with open(notebook_path, 'r') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Create an ExecutePreprocessor
    execute_preprocessor = ExecutePreprocessor(timeout=-1, kernel_name='python3')  # Use -1 for no timeout

    # Execute the notebook
    try:
        execute_preprocessor.preprocess(notebook_content, {'metadata': {'path': 'D:\PROJECTS\EDI PROJECT\back-end\edi_.ipynb'}})
    except Exception as e:
        print(f"Error executing notebook: {e}")
        raise

    print("Google Colab file executed successfully")

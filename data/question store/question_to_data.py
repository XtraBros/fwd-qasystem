import subprocess
import sys
import os
import pdfplumber
import re
import json

def run_pipeline(input_pdf, output_json):
    """
    Runs the pipeline that converts a PDF to text and then processes the text into a JSON database.
    
    Args:
        input_pdf (str): Path to the input PDF file.
        output_json (str): Path to save the processed JSON output.
    """
    # Step 1: Run pdf_to_text.py to convert PDF to a text file
    print(f"Converting {input_pdf} to text...")
    text = pdf_to_text(input_pdf)
    process_questions(text, output_json)


    print(f"Pipeline completed. The output is saved to {output_json}.")

def pdf_to_text(pdf_path, output_txt=None):
    """
    Extracts all text from a PDF file and optionally saves it to a text file.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_txt (str, optional): Path to save the extracted text as a .txt file.

    Returns:
        str: The extracted text.
    """
    all_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text:
                    all_text += f"--- Page {page_num} ---\n{text}\n\n"
                else:
                    all_text += f"--- Page {page_num} ---\n[No text found]\n\n"
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

    # # Optionally save to a text file
    # if output_txt:
    #     with open(output_txt, "w", encoding="utf-8") as txt_file:
    #         txt_file.write(all_text)
    #         print(f"Text successfully saved to {output_txt}")

    return all_text

def process_questions(txt, output_json):
    """
    Processes questions and related data from a text file and saves them to a JSON database.

    Args:
        txt_path (str): Path to the input .txt file containing extracted PDF text.
        output_json (str): Path to save the structured questions as a JSON file.
    """
    questions = []
    current_question = None
    current_subpart = None

    # Split the raw text into lines
    lines = txt.splitlines()

    for line in lines:
        line = line.strip()

        # DEBUG: Print each line being processed
        # print(f"Processing line: {line}")

        # Match a question number (e.g., "8.")
        question_number_match = re.match(r"^(\d+)\.$", line)
        if question_number_match:
            # print(f"Found question number: {line}")  # DEBUG
            if current_question:
                # Save the current question before starting a new one
                if current_subpart:
                    # Append the last subpart to the question
                    current_question["question"] += f"\n{current_subpart}"
                questions.append(current_question)

            question_id = question_number_match.group(1)
            current_question = {
                "question_id": question_id,
                "question": "",
                "score": 0,  # To be updated
                "correctAnswer": "",
                "data": []
            }
            current_subpart = None  # Reset subpart
            continue

        # Match the score for a question or subpart (e.g., "(10 points)")
        score_match = re.match(r"^\((\d+)\s+points?\)", line)
        if score_match and current_question:
            # print(f"Found score: {line}")  # DEBUG
            current_question["score"] = int(score_match.group(1))
            continue

        # Match subpart (e.g., "(a) (6 points)")
        subpart_match = re.match(r"^\((\w+)\)\s+\((\d+)\s+points?\)", line)
        if subpart_match and current_question:
            # print(f"Found subpart: {line}")  # DEBUG
            if current_subpart:
                # Append previous subpart to the question
                current_question["question"] += f"\n{current_subpart}"

            subpart_id = subpart_match.group(1)
            subpart_score = int(subpart_match.group(2))
            current_subpart = f"({subpart_id}) ({subpart_score} points): "
            continue

        # Collect table or data lines
        if re.search(r"(\d+\s+\d+\s+\d+)", line):  # Simple heuristic for detecting tables
            # print(f"Found table data: {line}")  # DEBUG
            if current_question:
                current_question["data"].append(line)
            continue

        # Append the line to the current question or subpart
        if current_subpart:
            current_subpart += line + " "
        elif current_question:
            current_question["question"] += line + " "

    # Add the last question if it exists
    if current_question:
        if current_subpart:
            # Append the last subpart to the question
            current_question["question"] += f"\n{current_subpart}"
        questions.append(current_question)

    # Save questions to JSON
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(questions, json_file, indent=4, ensure_ascii=False)
        print(f"Questions saved to {output_json}")

# Entry point of the script
if __name__ == "__main__":
    filepath = "/Users/zac/Documents/exam/"
    filename = "spring-2024-ilalpm-exam"
    input_pdf = f"{filepath}{filename}.pdf"
    output_json = f"{filename}.json"
    
    run_pipeline(input_pdf, output_json)

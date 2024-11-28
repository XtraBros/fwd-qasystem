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
    process_solutions(text, output_json)


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

def process_solutions(raw_text, output_json):
    """
    Processes the raw text, extracts solutions and commentary, and saves them to a JSON file
    for each question and subpart.

    Args:
        raw_text (str): The raw text containing the questions, solutions, and commentaries.
        output_json (str): Path to save the solutions and commentaries as a JSON file.
    """
    solutions = []
    current_question = None
    current_subpart = None
    current_solution = None
    current_commentary = None

    # Split the raw text into lines
    lines = raw_text.splitlines()

    for line in lines:
        line = line.strip()

        # Match a question number (e.g., "1.")
        question_number_match = re.match(r"^(\d+)\.$", line)
        if question_number_match:
            # Add the previous question if it exists
            if current_question:
                if current_solution:
                    current_question["solutions"] = current_solution  # Store the combined solution
                if current_commentary:
                    current_question["commentary"] = current_commentary
                solutions.append(current_question)

            # Start a new question entry
            question_id = question_number_match.group(1)
            current_question = {
                "question_id": question_id,
                "solutions": "",  # Single string for the solution
                "commentary": ""  # store commentary
            }
            current_subpart = None
            current_solution = ""  # We'll concatenate all solution parts into this string
            current_commentary = None
            continue

        # Match subpart (e.g., "(a) (6 points)")
        subpart_match = re.match(r"^\((\w+)\)\s+\((\d+)\s+points?\)", line)
        if subpart_match and current_question:
            # Add the current solution to the previous question (if any)
            if current_solution:
                current_question["solutions"] = current_solution  # Store the solution for the previous question

            subpart_id = subpart_match.group(1)
            subpart_score = int(subpart_match.group(2))
            current_subpart = f"({subpart_id}) ({subpart_score} points): "
            # We continue, but current_solution will accumulate all solution text
            continue

        # Extract the solution or commentary (lines following question or subpart)
        if current_solution is not None:
            # Append to the current solution (concatenate all lines under one entry)
            current_solution += line + "\n"
            continue

        # If the line contains commentary (e.g., "Commentary on Question:")
        commentary_match = re.match(r"^Commentary on Question:", line)
        if commentary_match and current_question:
            current_commentary = line + "\n"
            continue

        # If the line is part of the commentary section
        if current_commentary:
            current_commentary += line + "\n"
            continue

        # Ensure the question itself is captured (question description or other content)
        if current_question and not current_subpart:
            if not current_solution:
                current_solution += line + "\n"
            continue

    # Add the last question if it exists
    if current_question:
        if current_solution:
            current_question["solutions"] = current_solution  # Store the final solution
        if current_commentary:
            current_question["commentary"] = current_commentary
        solutions.append(current_question)

    # Save solutions to JSON
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(solutions, json_file, indent=4, ensure_ascii=False)
        print(f"Solutions saved to {output_json}")

# Entry point of the script
if __name__ == "__main__":
    filepath = "/Users/zac/Documents/exam/"
    filename = "spring-2024-ilalam-solutions"
    input_pdf = f"{filepath}{filename}.pdf"
    output_json = f"{filename}.json"
    
    run_pipeline(input_pdf, output_json)
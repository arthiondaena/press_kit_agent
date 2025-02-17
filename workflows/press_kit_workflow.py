def press_kit_workflow(manager, company_info, press_topic, tone):
    final_structure = """
    [Final Structure Preview]
    1. Press Release (Draft)
    2. Company Overview
    3. PR Message
    4. Email Draft
    5. Supplementary Materials (if applicable)
    """

    with open("markdown_example.py", "r") as markdown_file:
        markdown_ex = markdown_file.read()

    tasks = f"""
    (Important: Do not use mdutils for anything except for creating a markdown file at the end.)
    task 1: Collect supplementary information about {company_info} for the topic {press_topic}
    task 2: Preview the summary of supplementary information.
    task 3: Ask the user whether to include the supplementary information for press kit.
    task 4: Generate various text contents including a press release draft, company overview, PR message, and email draft in {tone} tone.
    task 5: Preview the summary of the current draft
    task 6: Ask the user whether to proceed with the current draft or request modification.
    task 7: Reorganize the information in markdown format and display the titles and subtitles which resemble the {final_structure}
    task 8: Preview the current markdown structure
    task 9: Ask the user whether to proceed with the current markdown structure or request modification.
    task 10: Review the press kit by using evaluations like Content consistency, writing style, layout structure, SEO optimization. Rate the evaluations out of 10 and provide overall feedback of the press kit.
    task 11: Save the outputs in markdown file with {final_structure} structure using mdutils. This is the documentation of mdutils: {markdown_ex}.
    """
    manager.agent.run(tasks)
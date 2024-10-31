def compile_final_proposal(use_cases, datasets, additional_resources, industry_data):
    with open("Healthcare_Proposal.md", "w") as file:
        file.write("# AI/ML Proposal for the Healthcare Industry\n\n")
        
        # Industry Overview
        file.write("## Industry Overview\n")
        file.write(industry_data.get('overview', 'No overview found.') + "\n\n")
        
        # Key Offerings
        file.write("## Key Offerings\n")
        for offering in industry_data.get('key_offerings', []):
            file.write(f"- {offering}\n")
        file.write("\n")

        # Strategic Focus Areas
        file.write("## Strategic Focus Areas\n")
        for focus in industry_data.get('strategic_focus', []):
            file.write(f"- {focus}\n")
        file.write("\n")

        # Add use cases
        file.write("## Top AI/ML Use Cases\n")
        for use_case in use_cases:
            file.write(f"- {use_case}\n")

        # Dataset resources
        file.write("\n## Relevant Dataset Resources\n")
        for dataset in datasets:
            file.write(f"- [Dataset Link]({dataset})\n")

        # Additional resources
        file.write("\n## Additional Resources\n")
        for resource in additional_resources:
            file.write(f"- {resource}\n")

    print("Final proposal compiled successfully.")

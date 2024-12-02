import os

def create_cybersecurity_structure(base_dir):
    # Define folders and files
    structure = {
        "Phase_1_Foundational_Knowledge": {
            "Week_1_Understand_Networking_Basics": [
                "01 - OSI_Model_Diagram.md",
                "02 - Networking_Protocols.md",
                "03 - OSI_Layers_Assignment.md"
            ],
            "Week_2_Learn_Packet_Analysis": [
                "01 - Wireshark_Usage_Guide.md",
                "02 - Captured_Traffic_Analysis.md",
                "03 - Assignment_Findings.md"
            ],
            "Week_3_Study_Operating_Systems": [
                "01 - Windows_AD_Notes.md",
                "02 - Linux_Commands_Practice.md",
                "03 - Virtual_Machine_Setup.md"
            ],
            "Week_4_Master_Shell_Scripting": [
                "01 - Bash_Scripting_Tutorial.md",
                "02 - PowerShell_Scripting_Tips.md",
                "03 - Automation_Task_Scripts.md"
            ]
        },
        "Phase_2_Core_Cybersecurity_Skills": {
            "Week_5_Learn_Cybersecurity_Concepts": [
                "01 - CIA_Triad_Notes.md",
                "02 - Threat_Models.md",
                "03 - Cyberattack_Analysis_Report.md"
            ],
            "Week_6_Study_Cryptography_Basics": [
                "01 - Symmetric_vs_Asymmetric.md",
                "02 - Hashing_Examples.md",
                "03 - OpenSSL_Exercise.md"
            ],
            "Week_7_Explore_Vulnerability_Assessment_Tools": [
                "01 - Nmap_Tutorial.md",
                "02 - Nessus_Overview.md",
                "03 - Local_Network_Scan_Report.md"
            ],
            "Week_8_Master_Common_Web_Security_Vulnerabilities": [
                "01 - OWASP_Top_10_Overview.md",
                "02 - DVWA_Setup_Guide.md",
                "03 - SQL_Injection_Exploit_Details.md"
            ]
        },
        "Phase_3_Practical_Skills_Development": {
            "Week_9_Set_Up_a_Lab_Environment": [
                "01 - Lab_Setup_Guide.md",
                "02 - Kali_Linux_Configuration.md",
                "03 - Connectivity_Test_Report.md"
            ],
            "Week_10_Conduct_Basic_Penetration_Tests": [
                "01 - Vulnerable_Environment_Setup.md",
                "02 - SQL_Injection_Attack_Details.md",
                "03 - Vulnerability_Patch_Guide.md"
            ],
            "Week_11_Analyze_Logs_and_Monitor_Traffic": [
                "01 - Splunk_Configuration.md",
                "02 - ELK_Stack_Analysis.md",
                "03 - Anomaly_Detection_Log.md"
            ],
            "Week_12_Complete_Beginner_CTF": [
                "01 - CTF_Solutions.md",
                "02 - Hack_The_Box_Writeups.md",
                "03 - TryHackMe_Progress.md"
            ]
        },
        "Phase_4_Specialized_Skills": {
            "Month_4_Advanced_Threat_Hunting": [
                "01 - SIEM_Tools_Guide.md",
                "02 - Threat_Hunting_Case_Study.md",
                "03 - Log_Analysis_Report.md"
            ],
            "Month_5_Incident_Response_Strategies": [
                "01 - Incident_Response_Basics.md",
                "02 - Ransomware_Simulation.md",
                "03 - Incident_Response_Plan.md"
            ],
            "Month_6_Malware_Analysis_Basics": [
                "01 - Static_vs_Dynamic_Analysis.md",
                "02 - Sandbox_Setup_Guide.md",
                "03 - Malware_Behavior_Report.md"
            ],
            "Month_7_Advanced_Cryptography": [
                "01 - RSA_Encryption_Tutorial.md",
                "02 - Diffie_Hellman_Overview.md",
                "03 - Digital_Signatures.md"
            ]
        },
        "Phase_5_Professional_Growth": {
            "Month_8_Obtain_Industry_Certifications": [
                "01 - Certification_Options.md",
                "02 - Study_Plan.md",
                "03 - Certification_Resources.md"
            ],
            "Month_9_Build_a_Cybersecurity_Portfolio": [
                "01 - Portfolio_Projects.md",
                "02 - Writeups_and_Reports.md",
                "03 - GitHub_Publishing_Guide.md"
            ],
            "Month_10_Contribute_to_Open_Source_Projects": [
                "01 - Open_Source_Projects.md",
                "02 - Contribution_Guide.md",
                "03 - Pull_Request_Template.md"
            ],
            "Month_11_Prepare_for_Job_Interviews": [
                "01 - Case_Study_Solutions.md",
                "02 - Mock_Interview_Notes.md",
                "03 - Resume_and_Cover_Letter_Tips.md"
            ]
        }
    }

    # Create folders and files
    for phase, weeks in structure.items():
        phase_path = os.path.join(base_dir, phase)
        os.makedirs(phase_path, exist_ok=True)
        print(f"Created folder: {phase_path}")

        for week, files in weeks.items():
            week_path = os.path.join(phase_path, week)
            os.makedirs(week_path, exist_ok=True)
            print(f"Created folder: {week_path}")

            for file_name in files:
                file_path = os.path.join(week_path, file_name)
                with open(file_path, "w") as f:
                    f.write(f"# {file_name.split('.')[0].replace('_', ' ')}\n")
                print(f"Created file: {file_path}")

if __name__ == "__main__":
    base_directory = "."  #Current_Directory
    create_cybersecurity_structure(base_directory)

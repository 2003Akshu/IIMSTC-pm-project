from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

def generate_project_charter(file_name, project_details):
    pdf = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Title Section
    pdf.setFont("Helvetica-Bold", 24)
    pdf.setFillColor(HexColor("#003366"))
    pdf.drawCentredString(width / 2, height - 60, "Project Charter")

    # Line below Title
    pdf.setStrokeColor(HexColor("#003366"))
    pdf.setLineWidth(2)
    pdf.line(50, height - 80, width - 50, height - 80)

    # Project Details
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(HexColor("#000000"))
    y_position = height - 120

    for section, content in project_details.items():
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, y_position, f"{section}:")
        pdf.setFont("Helvetica", 12)
        y_position -= 20

        for line in content.split("\n"):
            pdf.drawString(70, y_position, line)
            y_position -= 15
        y_position -= 10

    # Footer
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(50, 40, "Generated using ReportLab - Python PDF Library")
    pdf.save()
    print(f"Project Charter saved as '{file_name}'.")

if __name__ == "__main__":
    project_details = {
        "Project Title": "AI-Based Image Segmentation for Autonomous Vehicles",
        "Project Manager": "Manish Kumar",
        "Description": ("This project aims to develop advanced image segmentation models using "
                        "deep learning techniques to enhance the perception systems of autonomous vehicles."),
        "Objectives": "1. Develop robust segmentation models.\n2. Optimize algorithms for real-time processing.\n3. Validate the system on real-world datasets.",
        "Scope": "The project includes data collection, model training, and deployment testing on autonomous platforms.",
        "Deliverables": "1. Segmentation models.\n2. Validation report.\n3. Deployment package.",
        "Timeline": "Jan 2025 - June 2025",
        "Budget": "$50,000",
    }

    generate_project_charter("Project_Charter1.pdf", project_details)

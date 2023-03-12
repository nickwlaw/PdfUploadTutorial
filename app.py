import gradio as gr


def upload_pdf(pdf):
    file_path = pdf.name
    return file_path


with gr.Blocks() as ui:
    file_output = gr.File()
    upload_button = gr.UploadButton(
        "Click to upload a PDF",
        file_types=[".pdf"]
    )
    upload_button.upload(upload_pdf, upload_button, file_output)

ui.launch()

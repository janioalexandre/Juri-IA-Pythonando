from usuarios.models import Documentos
from django.shortcuts import get_object_or_404
from .agents import JuriAI


def ocr_and_markdown_file(instance_id):
    from docling.document_converter import DocumentConverter

    documentos = Documentos.objects.filter(id=instance_id).first()
    if documentos is None:
        return 'Documento não encontrado'

    try:
        converter = DocumentConverter()
        result = converter.convert(documentos.arquivo.path)
        doc = result.document
        texto = doc.export_to_markdown()

        documentos.content = texto
        documentos.save()
        
    except Exception as e:
        print(f"Erro ao processar OCR: {str(e)}")
        return f'Erro: {str(e)}'

def rag_documentos(instance_id):
    documentos = Documentos.objects.filter(id=instance_id).first()
    if documentos is None:
        return 'Documento não encontrado'
    JuriAI.knowledge.insert(
        name=documentos.arquivo.name,
        text_content=documentos.content,
        metadata={
            "cliente_id": documentos.cliente.id,
            "name": documentos.arquivo.name,
        },
    )

def rag_dados_empresa(instance_id):
    ...

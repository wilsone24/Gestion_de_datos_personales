from datetime import date
import re


def _validate_document_type(document_type):
    valid_document_types = ["Tarjeta de identidad", "Cédula"]
    if document_type not in valid_document_types:
        raise ValueError(
            f"El tipo de documento debe ser uno de: {', '.join(valid_document_types)}."
        )


def _validate_document_number(document_number):
    if not document_number.isdigit():
        raise ValueError("El número de documento debe contener solo números.")
    if len(document_number) > 10:
        raise ValueError("El número de documento no puede tener más de 10 caracteres.")


_NAME_REGEX = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$")


def _validate_name(name, label, max_len, required=True):
    n = (name or "").strip()
    if required and not n:
        raise ValueError(f"El {label} es obligatorio.")
    if not n:
        return
    if len(n) > max_len:
        raise ValueError(f"El {label} no puede tener más de {max_len} caracteres.")
    if not _NAME_REGEX.match(n):
        raise ValueError(f"El {label} solo puede contener letras y espacios.")


def _validate_birth_date(birth_date):
    if not isinstance(birth_date, date):
        raise ValueError("La fecha de nacimiento debe ser un objeto de tipo date.")


def _validate_gender(gender):
    valid_genders = ["Masculino", "femenino", "No binario", "Prefiero no reportar"]
    g = (gender or "").strip()
    if g not in valid_genders:
        raise ValueError(f"El género debe ser uno de: {', '.join(valid_genders)}.")


def _validate_email(email):
    e = (email or "").strip()
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", e):
        raise ValueError("El correo electrónico no tiene un formato válido.")


def _validate_phone(phone):
    p = (phone or "").strip()
    if not p.isdigit():
        raise ValueError("El número de celular debe contener solo números.")
    if len(p) != 10:
        raise ValueError("El número de celular debe tener exactamente 10 dígitos.")


def validate_person_data(data):
    _validate_document_type(data.get("document_type", ""))
    _validate_document_number(data.get("document_number", ""))
    _validate_name(data.get("first_name", ""), "primer nombre", 30, required=True)
    _validate_name(data.get("second_name", ""), "segundo nombre", 30, required=False)
    _validate_name(data.get("last_name", ""), "apellido", 60, required=True)
    _validate_birth_date(data.get("birth_date", ""))
    _validate_gender(data.get("gender", ""))
    _validate_email(data.get("email", ""))
    _validate_phone(data.get("phone_number", ""))
    return True

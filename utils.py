from aiogram.types import CallbackQuery, Message
import decimal
from decimal import (
    localcontext,
)

def answer_message_or_query(message_or_query: CallbackQuery or Message, is_message_from_query: bool = False, send_new_message: bool = True):
    if isinstance(message_or_query, Message):
        if is_message_from_query:
            return message_or_query.edit_text
        return message_or_query.answer
    elif isinstance(message_or_query, CallbackQuery):
        if send_new_message:
            return message_or_query.message.answer
        return message_or_query.message.edit_text
    raise RuntimeError()


def from_units(number: int, unit_value: int):
    with localcontext() as ctx:
        ctx.prec = 999
        d_number = decimal.Decimal(value=number, context=ctx)
        result_value = d_number / (decimal.Decimal('10') ** unit_value)

    return result_value
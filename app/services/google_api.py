from datetime import datetime, timedelta

from aiogoogle import Aiogoogle

from app.constants import (SHEET_COLUMN_COUNT, SHEET_DATETIME_FORMAT, SHEET_ID,
                           SHEET_LOCALE, SHEET_NAME, SHEET_ROW_COUNT,
                           SHEET_TITLE, SHEET_TYPE)
from app.core.config import settings


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now = datetime.now().strftime(SHEET_DATETIME_FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = {
        'properties': {'title': SHEET_NAME.format(now=now),
                       'locale': SHEET_LOCALE},
        'sheets': [{'properties': {'sheetType': SHEET_TYPE,
                                   'sheetId': SHEET_ID,
                                   'title': SHEET_TITLE,
                                   'gridProperties': {
                                       'rowCount': SHEET_ROW_COUNT,
                                       'columnCount': SHEET_COLUMN_COUNT}}}]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']

    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(SHEET_DATETIME_FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    for project in projects:
        new_row = [project.name,
                   str(timedelta(days=project.time_passed)),
                   project.description]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )

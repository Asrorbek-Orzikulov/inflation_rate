import re
from os import path, getcwd
from pandas import concat, ExcelFile, ExcelWriter
from tkinter import messagebox
from numpy import nan, setdiff1d

from .converter import convert_dict


def create_messagebox(text, is_error=True):
    """
    Display a message box with the given `text`.

    Parameters
    ----------
    text : str
        text message to be displayed.
    is_error : bool
        if True, an error message box will be shown.
        Otherwise, displays an information message box.

    Returns
    -------
    None.

    """
    if is_error:
        messagebox.showerror(title='Saving Request', message=text)
    else:
        messagebox.showinfo(title='Saving Request', message=text)


def on_enter(event):
    """Change the background color of a widget to blue."""
    event.widget['background'] = '#33E6FF'


def on_leave(event):
    """Change the background color of a widget to green."""
    event.widget['background'] = '#3DC70D'


def read_sheet(excel_file, sheet_name, skip_columns, use_rows):
    """Read one sheet of an Excel file."""
    df = excel_file.parse(
        sheet_name=sheet_name, skiprows=4,
        skipfooter=2, header=None)
    if df.at[0, 0] is nan:
        if df.at[1, 0] == 'Маҳсулот номи':
            skip_rows = 5
        else:
            skip_rows = 3
        df = excel_file.parse(
            sheet_name=sheet_name, skiprows=skip_rows,
            skipfooter=2, header=None)

    df = df.replace('Туманлар', '')
    df.iloc[0:2] = df.iloc[0:2].fillna('')
    df.columns = df.iloc[0:2].apply(
        lambda column: ''.join([row for row in column]), axis=0)
    df = df.drop(skip_columns, axis=1, errors='ignore')
    df = df.iloc[2:]
    df.set_index('Маҳсулот номи', inplace=True)
    df = df.loc[use_rows, :]
    df = df.transpose()
    return df


def read_file(filename):
    """Read an Excel file containing price information."""
    skip_columns = ['Респуб-лика бўйича ўртача', 'Вилоят бўйича ўртача', 'Шаҳар бўйича ўртача']
    use_rows = [
        'Мол гўшти', 'Сут, 1 литр', 'Тухум, 10 донаси',
        'Картошка', 'Ўсимлик ёғи', 'Гуруч', 'Буғдой уни', 'Шакар'
    ]
    excel_file = ExcelFile(filename)
    df_list = []
    for sheet in excel_file.sheet_names:
        if sheet not in ['laroux', '1700']:
            df_sheet = read_sheet(excel_file, sheet, skip_columns, use_rows)
            df_list.append(df_sheet)

    df_merged = concat(df_list)
    df_merged = df_merged.astype('float64', copy=True, errors='raise')
    temp_index = df_merged.index.to_series().replace(
        {re.compile(r'(.*) \*'): r'\1', re.compile(r'(.*)\*'): r'\1'}, regex=True
        )
    df_merged.index = temp_index.replace(convert_dict)
    df_merged = df_merged[df_merged.index.notnull()]
    return df_merged


def calculate_difference(old_filename, new_filename):
    """Calculate price changes for eight basic products."""
    extension_pattern = '.xlsx'
    if not re.search(extension_pattern, old_filename):
        old_filename += extension_pattern
    if not re.search(extension_pattern, new_filename):
        new_filename += extension_pattern

    date_pattern = r'\d{2}\.\d{2}\.\d{4}'
    old_date = re.search(date_pattern, old_filename)
    new_date = re.search(date_pattern, new_filename)
    if not old_date:
        create_messagebox('Old filename is invalid.')
        return
    elif not new_date:
        create_messagebox('New filename is invalid.')
        return
    elif not path.isfile(old_filename):
        create_messagebox(f'Old file doesn\'t exist in {getcwd()}')
        return
    elif not path.isfile(new_filename):
        create_messagebox(f'New file doesn\'t exist in {getcwd()}')
        return

    old_date = old_date.group()
    new_date = new_date.group()
    try:
        new_file = read_file(new_filename)
    except Exception:
        create_messagebox(f'{new_filename}: ' + str(Exception))
        return
    try:
        old_file = read_file(old_filename)
    except Exception:
        create_messagebox(f'{old_filename}: ' + str(Exception))
        return

    non_matches = setdiff1d(new_file.index, old_file.index)
    if non_matches.size > 0:
        create_messagebox('non-matching names: ' + str(non_matches))
        return

    percentage = new_file.subtract(old_file).div(old_file)
    excel_name = f'{old_date}-{new_date}-inflation.xlsx'
    writer = ExcelWriter(excel_name, engine='xlsxwriter')
    new_file.to_excel(writer, sheet_name='new_data',
                      encoding='utf-8', index_label='place')
    for column in percentage.columns:
        series_sorted = percentage[column].nlargest(10, keep='first')
        series_sorted.to_excel(writer, sheet_name=column,
                               encoding='utf-8', index_label='place')
    writer.save()
    create_messagebox(f'{excel_name} has been created.', False)

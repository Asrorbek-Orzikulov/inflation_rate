from os import path, chdir, mkdir, getcwd, listdir, rename
from re import compile, search
from pandas import DataFrame, concat, ExcelFile, ExcelWriter
from tkinter import messagebox
from numpy import nan


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


def find_files(pattern):
    """
    Find all filenames in the current folder that match the pattern.

    Parameters
    ----------
    pattern : str
        regex pattern to use to match the filenames.

    Returns
    -------
    filenames : list
        list of filenames that match the pattern.

    """
    filenames_pattern = compile(pattern)
    filenames = list(filter(filenames_pattern.match, listdir('./')))
    return filenames


def merge_district_pickles(date):
    """
    Merge pickle files in the `temporary_files` folder of the form
    `date-commission_type-furnished_type-home_type-district.pkl`
    into one pickle file with the name `date-merged.pkl`.

    Creates a `Database` folder if it does not exist and saves the
    merged pickle file there.

    Parameters
    ----------
    date : str
        date of the form `dd-mm-yyyy`.

    Returns
    -------
    None.

    """
    if not path.isdir('temporary_files'):
        create_messagebox('temporary_files folder does not exist.')
        return

    chdir('temporary_files')
    filenames_pattern = f'{date}-' + r'(yes|no)-.*\.pkl$'
    all_filenames = find_files(filenames_pattern)
    if not all_filenames:
        create_messagebox(f'Pickle files do not exist in {getcwd()}')
        chdir('..')
        return

    create_messagebox(f'Found {len(all_filenames)} files to merge.', False)
    merged_data = concat([read_pickle(file) for file in all_filenames])
    chdir('..')

    if not path.isdir('Database'):
        mkdir('Database')
    chdir('Database')
    merged_filename = f'{date}-merged.pkl'
    merged_data.to_pickle(merged_filename)
    create_messagebox(f'{merged_filename} has been created.', False)
    chdir('..')


def merge_month_pickles():
    """
    Merge all pickle files in the current folder of the form
    `dd-mm-yyyy-merged.pkl` into one pandas DataFrame, dropping
    duplicated rows.

    Returns
    -------
    pandas DataFrame.

    """
    filenames_pattern = r'\d{2}-\d{2}-\d{4}-merged\.pkl$'
    all_filenames = find_files(filenames_pattern)
    if not all_filenames:
        return DataFrame()

    create_messagebox(f'Found {len(all_filenames)} files to merge.', False)
    merged_data = concat([read_pickle(file) for file in all_filenames])
    merged_data.drop_duplicates(
        subset=['link', 'price', 'num_rooms', 'area', 'home_type', 'district'],
        inplace=True
    )
    return merged_data


def create_excel(date):
    """
    Merge all pickle files in the `Database` folder of the form
    `dd-mm-yyyy-merged.pkl` into one Excel file, dropping duplicates.

    Creates an Excel file with the name `date-merged.xlsx` and
    saves it in the `Database` folder.

    Parameters
    ----------
    date : str
        date of the form `dd-mm-yyyy`.

    Returns
    -------
    None.

    """
    if not path.isdir('Database'):
        create_messagebox('Database folder does not exist.')
        return

    chdir('Database')
    df = merge_month_pickles()
    if df.empty:
        create_messagebox(f'Pickle files do not exist in {getcwd()}')
        chdir('..')
        return

    filename = f'{date}-merged.xlsx'
    df.to_excel(filename, index=False, encoding='utf-8')
    create_messagebox(f'{filename} has been created.', False)
    chdir('..')


def update_yesterday(yesterday, today):
    """
    Rename all filenames in the `temporary_files` folder of the form
    `yesterday-commission_type-furnished_type-home_type-district.pkl`
    as `today-commission_type-furnished_type-home_type-district.pkl`.

    Parameters
    ----------
    yesterday: str
        yesterday's date of the form `dd-mm-yyyy`.
    today: str
        today's date of the form `dd-mm-yyyy`.

    Returns
    -------
    None.

    """
    if not path.isdir('temporary_files'):
        create_messagebox('temporary_files folder does not exist.')
        return

    chdir('temporary_files')
    yesterday_pattern = f'{yesterday}-' + r'(yes|no)-.*\.pkl$'
    yesterday_files = find_files(yesterday_pattern)
    num_renamed = 0
    for filename in yesterday_files:
        new_filename = filename.replace(f'{yesterday}', f'{today}')
        if not path.isfile(new_filename):
            rename(filename, new_filename)
            num_renamed += 1

    create_messagebox(f'{num_renamed} files have been renamed.', False)
    chdir('..')


def on_enter(event):
    """Change the background color of a widget to blue."""
    event.widget['background'] = '#33E6FF'


def on_leave(event):
    """Change the background color of a widget to green."""
    event.widget['background'] = '#3DC70D'


def read_sheet(excel_file, sheet_name, skip_columns, use_rows):
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
    skip_columns = ['Респуб-лика бўйича ўртача', 'Вилоят бўйича ўртача', 'Шаҳар бўйича ўртача']
    use_rows = [
        'Мол гўшти', 'Сут, 1 литр', 'Тухум, 10 донаси',
        'Картошка', 'Гуруч', 'Ўсимлик ёғи', 'Буғдой уни', 'Шакар'
    ]
    excel_file = ExcelFile(filename)
    df_list = []
    for sheet in excel_file.sheet_names:
        if sheet not in ['laroux', '1700']:
            df_sheet = read_sheet(excel_file, sheet, skip_columns, use_rows)
            df_list.append(df_sheet)

    print(f'{len(df_list)} regions are found.')
    df_merged = concat(df_list)
    df_merged = df_merged.astype('float64', copy=True, errors='raise')
    return df_merged


def calculate_difference(old_filename, new_filename):
    new_file = read_file(new_filename)
    old_file = read_file(old_filename)
    percentage = new_file.subtract(old_file).div(old_file)
    percentage = percentage.mul(100)
    excel_name = 'inflation.xlsx'
    writer = ExcelWriter(excel_name, engine='xlsxwriter')
    new_file.to_excel(writer, sheet_name='new_data',
                      encoding='utf-8', index_label='place')
    for column in percentage.columns:
        series_sorted = percentage[column].nlargest(10, keep='first')
        series_sorted.to_excel(writer, sheet_name=column,
                               encoding='utf-8', index_label='place')
    writer.save()


new_filename = '/Users/asrorbek/Desktop/Inflation_Rate/08.09.2021 сред.цен.xlsx'  # '08.09.2021-сред.цен.xlsx'
old_filename = '/Users/asrorbek/Desktop/Inflation_Rate/31.08.2021 сред.цен.xlsx'
calculate_difference(old_filename, new_filename)


excel_file = ExcelFile(old_filename)
sheet_name = columns[15]
len(read_sheet(excel_file, sheet_name, skip_columns, use_rows).index)

m = search(r'\d{2}\.\d{2}\.\d{4}', fil)
if m:
    found = m.group()

columns = [
    'laroux',
     '1700',
     '1735',
     '1703',
     '1706',
     '1708',
     '1710',
     '1712',
     '1714',
     '1718',
     '1722',
     '1724',
     '1727',
     '1730',
     '1733',
     '1726'
]
let key_reports = false;
const button_reports = document.getElementById("reports");
const arrow = document.getElementById("arrow");
const list_reports = document.getElementById("view-reports");

function show_report() {
    if (!key_reports) {
        button_reports.style.backgroundColor = "#EAAC25";
        list_reports.classList.add("list-reports-visible");
        arrow.classList.add("rotate");
        key_reports = true;

        button_reports.addEventListener('mouseenter', function (e) {
            e.target.style.backgroundColor = '#3078FF';
        });

        button_reports.addEventListener('mouseleave', function (e) {
            e.target.style.backgroundColor = '#EAAC25';
        });
    } else {
        button_reports.style.backgroundColor = "#3078FF";
        list_reports.classList.remove("list-reports-visible");
        arrow.classList.remove("rotate");
        key_reports = false;

        button_reports.addEventListener('mouseenter', function (e) {
            e.target.style.backgroundColor = '#EAAC25';
        });

        button_reports.addEventListener('mouseleave', function (e) {
            e.target.style.backgroundColor = '#3078FF';
        });
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const tables = [document.getElementById('table1'), document.getElementById('table')];
    const contextMenu = document.getElementById('contextMenu');

    // Обработчик события для обеих таблиц
    tables.forEach(table => {
        if (table) { // Проверяем, существует ли таблица
            // Обработчик клика левой кнопкой мыши для выделения строки
            table.addEventListener('click', function (event) {
                if (event.target.tagName === 'TD') {
                    const row = event.target.parentNode;
                    clearSelection(); // Снимаем выделение со всех строк
                    row.classList.add('selected'); // Добавляем класс выделения
                }
            });

            // Обработчик события для правого клика
            table.addEventListener('contextmenu', function (event) {
                event.preventDefault(); // Отменяем стандартное контекстное меню

                // Проверяем, является ли кликнутый элемент ячейкой (td)
                if (event.target.tagName === 'TD') {
                    // Выделяем строку
                    const row = event.target.parentNode;
                    clearSelection(); // Снимаем выделение со всех строк
                    row.classList.add('selected'); // Добавляем класс выделения

                    // Позиционируем контекстное меню
                    contextMenu.style.display = 'block';
                    contextMenu.style.left = event.pageX + 'px';
                    contextMenu.style.top = event.pageY + 'px';

                    // Сохраняем ссылку на строку для дальнейших действий
                    contextMenu.dataset.row = row.rowIndex;
                    contextMenu.dataset.tableId = table.id; // Сохраняем ID таблицы
                }
            });
        }
    });

    // Обработчик клика вне контекстного меню
    document.addEventListener('click', function () {
        contextMenu.style.display = 'none'; // Скрываем меню
    });

    // Функция для снятия выделения со всех строк
    function clearSelection() {
        tables.forEach(table => {
            if (table) {
                const rows = table.querySelectorAll('tr');
                rows.forEach(row => {
                    row.classList.remove('selected'); // Удаляем класс выделения
                });
            }
        });
    }

    // Обработчик клика по элементам контекстного меню
    document.getElementById('editRow').addEventListener('click', function (event) {
        event.preventDefault(); // Отменяем переход по ссылке
        const rowIndex = contextMenu.dataset.row;
        const tableId = contextMenu.dataset.tableId;
        alert('Редактировать строку: ' + rowIndex + ' в таблице ' + tableId); // Здесь можно добавить логику редактирования
        contextMenu.style.display = 'none'; // Скрываем меню
    });

    document.getElementById('deleteRow').addEventListener('click', function (event) {
        event.preventDefault(); // Отменяем переход по ссылке
        const rowIndex = contextMenu.dataset.row;
        const tableId = contextMenu.dataset.tableId;
        const table = document.getElementById(tableId); // Получаем таблицу по ID
        const row = table.rows[rowIndex]; // Находим строку по индексу
        if (row) {
            row.parentNode.removeChild(row); // Удаляем строку
            alert('Строка ' + rowIndex + ' удалена из таблицы ' + tableId + '.'); // Подтверждение удаления
        }
        contextMenu.style.display = 'none'; // Скрываем меню
    });
});






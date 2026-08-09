mkdir -p "$HOME/.config/todo-app"
DB_PATH="$HOME/.config/todo-app/db.sqlite"
sqlite3 "$DB_PATH" "create table if not exists tasks (
    id integer primary key autoincrement,
    task text not null
)"
case "$1" in
    add)
        sqlite3 "$DB_PATH" "insert into tasks (task) values ('$2')"
        ;;
    list)
        sqlite3 "$DB_PATH" "select * from tasks"
        ;;
    remove)
        sqlite3 "$DB_PATH" "delete from tasks where id = $2"
        ;;
    *)
        echo "unknown"
        ;;
esac
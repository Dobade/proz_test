python_work_home=/home/user_00/lijianjun/weibomessage
function start_server() {
    cd $python_work_home
    
    python subscribe.py 
}
function stop_server() {
    ps -ef | grep python.py | cut -c 9-15 | xargs kill -s 9
}
function restart_server () {
    stop_server
    sleep 1
    start_server
}
function contrl_server() {
    ps aux | grep -n subscribe.py & publish.py
}

case "$1" in
    start)
        start_server
        exit $?
        ;;
    stop)
        stop_server
        exit $?
        ;;
    restart)
        restart_server
        exit $?
        ;;
    contrl)
        contrl_server
        exit $?
        ;;
        *)
        echo "Usage: $0 { start | stop | restart |contrl}"
        exit 1
        ;;
esac


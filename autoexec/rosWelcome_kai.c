#include <unistd.h>

int main()
{
    pid_t roscore = fork();
    if(roscore == 0) {
        execl("/bin/sh", "sh", "./shell/roscore.sh", (void*)NULL);
    }

 
    pid_t carstate = fork();
    if(carstate == 0) {
        execl("/bin/sh", "sh", "./shell/carstate.sh", (void*)NULL);
    }

    pid_t publish_gps = fork();
    if(publish_gps == 0) {
        execl("/bin/sh", "sh", "./shell/publish_gps.sh", (void*)NULL);
    }


    pid_t driver_main = fork();
    if(driver_main == 0) {
        execl("/bin/sh", "sh", "./shell/driver_main.sh", (void*)NULL);
    }

    pid_t ui = fork();
    if(ui == 0) {
        execl("/bin/sh", "sh", "./shell/ui.sh", (void*)NULL);
    }

    
    return 0;
}
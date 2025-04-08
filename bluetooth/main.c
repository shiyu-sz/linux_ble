#include <bluetooth/bluetooth.h>
#include <bluetooth/hci.h>
#include <bluetooth/hci_lib.h>
#include <bluetooth/l2cap.h>
#include <bluetooth/gatt.h>
#include <bluetooth/hci.h>

int main() {
    // 初始化蓝牙适配器
    int dev_id = hci_get_route(NULL);
    int sock = hci_open_dev(dev_id);
    
    if (dev_id < 0 || sock < 0) {
        perror("无法打开蓝牙设备");
        exit(1);
    }
    
    // BLE操作代码
    
    close(sock);
    return 0;
}
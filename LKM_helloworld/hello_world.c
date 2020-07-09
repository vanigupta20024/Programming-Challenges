// Header files
#include<linux/init.h>
#include<linux/kernel.h>
#include<linux/module.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Vani Gupta");
MODULE_DESCRIPTION("Task01");

static int __init task1_init(void){
    printk(KERN_INFO "\nHello World");
    return 0;
}

static void __exit task1_exit(void){
    printk(KERN_INFO "\nExit.");
}

module_init(task1_init);
module_exit(task1_exit);

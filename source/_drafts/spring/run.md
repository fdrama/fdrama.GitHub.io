# Spring boot启动步骤

Spring boot启动步骤如下：

```java
public ConfigurableApplicationContext run(String... args) {
    // 记录开始时间戳
    long startTime = System.nanoTime();
    // 创建Bootstrap上下文
    DefaultBootstrapContext bootstrapContext = createBootstrapContext();
    ConfigurableApplicationContext context = null;
    configureHeadlessProperty();
    // 获取SpringApplicationRunListeners 实例 
    SpringApplicationRunListeners listeners = getRunListeners(args);
    listeners.starting(bootstrapContext, this.mainApplicationClass);
    try {
        ApplicationArguments applicationArguments = new DefaultApplicationArguments(args);
        // 准备环境
        ConfigurableEnvironment environment = prepareEnvironment(listeners, bootstrapContext, applicationArguments);
        configureIgnoreBeanInfo(environment);
        Banner printedBanner = printBanner(environment);
        // 创建ApplicationContext 根据不同的web应用类型创建不同的ApplicationContext AnnotationConfigApplicationContext 
        // 	this.reader = new AnnotatedBeanDefinitionReader(this);  // 读取注解Bean定义
        //  this.scanner = new ClassPathBeanDefinitionScanner(this); // 扫描类路径下的Bean定义
        context = createApplicationContext();
        context.setApplicationStartup(this.applicationStartup);
        // 准备上下文
        prepareContext(bootstrapContext, context, environment, listeners, applicationArguments, printedBanner);
        // 刷新上下文
        refreshContext(context);

        // 刷新上下文后的操作
        afterRefresh(context, applicationArguments);
        Duration timeTakenToStartup = Duration.ofNanos(System.nanoTime() - startTime);
        if (this.logStartupInfo) {
            new StartupInfoLogger(this.mainApplicationClass).logStarted(getApplicationLog(), timeTakenToStartup);
        }
        listeners.started(context, timeTakenToStartup);
        // 调用所有的ApplicationRunner和CommandLineRunner
        callRunners(context, applicationArguments);
    }
    catch (Throwable ex) {
        handleRunFailure(context, ex, listeners);
        throw new IllegalStateException(ex);
    }
    try {
        Duration timeTakenToReady = Duration.ofNanos(System.nanoTime() - startTime);
        listeners.ready(context, timeTakenToReady);
    }
    catch (Throwable ex) {
        handleRunFailure(context, ex, null);
        throw new IllegalStateException(ex);
    }
    return context;
}


```
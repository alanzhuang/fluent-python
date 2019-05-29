## 协程
1. 从语法上看，协程和生成器类似，都包含了yield关键字。在协程中，yield通常在表达式右边（datum = yield）
2. 调用方可以通过.send(datum)方法把数据提供给协程，而不是next()函数。(simple.py）
3. yield可以不接收或传出数据，yield后面没有表达式那么生成器产出None，要从根本上把yield看成控制流程的方式

### 协程状态
1. GEN_CREATED 等待开始执行
2. GEN_RUNNINS 解释器正在执行
3. GEN_SUSPENDED 在yield表达处暂停
4. GEN_CLOSED 执行结束

仅当协程处于暂停状态的时候才能调用send方法，不过如果协程还没激活（处于状态1），要调用next(s)激活协程——也可以调用s.send(None)，效果一样


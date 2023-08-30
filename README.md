# temp

```yaml
- name: devprime_stream1
  value: "alias=Stream1|||enable=true|||default=true|||streamtype=RabbitMQ|||hostname=rabbitmq.default.svc|||user=guest|||password=guest|||port=5672|||exchange=devprime|||exchangetype=direct|||retry=3|||fallback=State1|||threads=30|||buffer=5|||publish=[exchange=devprime-fanout-global,exchangetype=fanout]|||subscribe=[exchange=devprime-fanout,exchangetype=fanout,queues=in-fanout-01][queues=ms-order-in]"
 
```

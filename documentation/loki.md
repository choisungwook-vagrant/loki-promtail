# RESTAPI
* data push: http://127.0.0.1:3100/loki/api/v1/push
* example
```sh
# reference: https://grafana.com/docs/loki/latest/api/#post-lokiapiv1push

{
  "streams": [
    {
      "stream": {
        "label": "value"
      },
      "values": [
          [ "<unix epoch in nanoseconds>", "<log line>" ],
          [ "<unix epoch in nanoseconds>", "<log line>" ]
      ]
    }
  ]
}


```

# 참고자료
* 공식문서: https://grafana.com/docs/loki/latest/api/
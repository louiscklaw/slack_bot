# slack bot / messenger

### Purpose
- a slice of script to send messgae using slack from script.

### to use it:
1. setup env_var point to the slack's webhook url
    * stated in .env_tempalte, modify and rename to .env
    * designed to workwith [autoenv](https://github.com/kennethreitz/autoenv)
    * `export FAB_BOT_WEBHOOK_URL=<your_slack_channel_webhook_url>`

1. to apply in your python script
```
from slack_bot import *

# send with default bot account
slack_reporter().sending_message(<name_appear_to_user>, <message_body>)

# send with customized bot account
slack_reporter(<custom_url>).sending_message(<name_appear_to_user>, <message_body>)
```

* testcase/testscript
`python3 test_slack_bot.py`

### Reference:
- https://api.slack.com/incoming-webhooks

from api.config.config import SERVER_ADDRESS,SERVER_PORT,USER_NAME,USER_PASSWORD
from asterisk.ami import SimpleAction, AMIClient
from api.config.config import logger
from api.config.schemas import MSG


async def call_func(manager:int, client_number: str) ->MSG:
    client_number = ''.join(i for i in client_number if i.isdigit())
    if client_number.startswith('7'):
        cl_list = list(client_number)
        cl_list[0] = '8'
        client_number = ''.join(cl_list)
    if len(client_number) > 11 or len(client_number) < 4:
        raise Exception(f'Wrong Number {client_number}')
    client_number = int(client_number)

    client = AMIClient(address=SERVER_ADDRESS, port=SERVER_PORT)
    try:
        client.login(username=USER_NAME, secret=USER_PASSWORD)
    except Exception as e :
        logger.error(f"Invalid AMI username or password error: {e}")
    action1 =  SimpleAction(
        name='SIPshowpeer',
        Peer=manager,
    )
    ext = client.send_action(action1)
    context = ext.response.keys['Context']

    action = SimpleAction(
        name='Originate',
        Channel=f'SIP/{manager}',
        Exten=str(client_number),
        Priority=1,
        Context=context,
        CallerID=f'{manager}',
    )
    ext2=client.send_action(action)
    error = str(ext2.response)
    client.logoff()
    return {"result": error}
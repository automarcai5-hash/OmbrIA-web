import json, os, sys, urllib.request
W = os.path.dirname(os.path.abspath(__file__))
URL = os.environ['N8N_API_URL'] + '/workflows/58WdGeVhd2HAnF2y'
H = {'X-N8N-API-KEY': os.environ['N8N_API_KEY'], 'Content-Type': 'application/json'}
def req(m, data=None):
    r = urllib.request.Request(URL, data=data, method=m, headers=H)
    return json.load(urllib.request.urlopen(r))
actual = req('GET')
copia = json.load(open(sys.argv[2], encoding='utf-8'))
assert actual['updatedAt'] == copia['updatedAt'], 'el flujo ha cambiado desde la copia: parar'
nuevo = json.load(open(sys.argv[1], encoding='utf-8'))
permitidos = {'executionOrder', 'saveDataErrorExecution', 'saveDataSuccessExecution', 'saveManualExecutions', 'saveExecutionProgress', 'timezone', 'errorWorkflow', 'callerPolicy', 'executionTimeout'}
body = {'name': nuevo['name'], 'nodes': nuevo['nodes'], 'connections': nuevo['connections'],
        'settings': {k: v for k, v in nuevo.get('settings', {}).items() if k in permitidos}}
res = req('PUT', json.dumps(body, ensure_ascii=False).encode('utf-8'))
print('subido:', res['name'], '| activo:', res['active'], '| nodos:', len(res['nodes']), '| errorWorkflow:', res['settings'].get('errorWorkflow'))
json.dump(res, open(os.path.join(W, 'flujo-subido.json'), 'w', encoding='utf-8'), ensure_ascii=False)

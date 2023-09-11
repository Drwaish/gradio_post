import gradio as gr
import requests


ky = ["row1","row2", "row3", "row4"," row5", "row6"]
max_textboxes = 6
# re_dict = {ky[counter]: gr.update(visible= True)}
def variable_outputs(k):
    '''
    Change the number of rows dynamically.

    Parameters
    ---------
    k
        number of rows
    
    Return
    ------
    None
    '''
    global act_length
    k = int(k)
    return [gr.Row.update(visible=True)]*k + [gr.Row.update(visible=False)]*(max_textboxes-k)
def sentence_builder(method : str, link : str ,*rows):
    '''
    Process parameters and test apis

    Parameters
    ----------
    method
        Type of method for request.
    link
        URL on which we test.
    rows
        Parameters for payload.
    
    Return
    JSON
    '''
    key = []
    value = []
    type1 = []
    print(len(rows))
    if len(rows) % 3 != 0:
        return "Parameters not complete! Kindly enter valid parameters"
    i = 0
    while i< len(rows):
        if rows[i] !='':
           key.append(rows[i])
        i = i+1
        if rows[i] !='': 
            value.append(rows[i])
        i=i+1
        if rows[i] !='': 
            type1.append(rows[i])
        i = i+1  # for key
    if method == 'POST':
        payload = {
                  key[0]: value[0].eval(),
                  key[1]: value[1]. eval(),
                  key[2]: value[2].eval(),
                  }
        headers = {
                    "content-type": "application/x-www-form-urlencoded",
                    "X-RapidAPI-Key": "06ecb68bbbmsh57c6ccd3cc78306p194f8cjsn18b2c5ce9922",
                    "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
                  }
        result = requests.post(link, data = payload, headers = headers)
        return result.json()
    if method == 'GET':
      headers = {
	              "X-RapidAPI-Key": "06ecb68bbbmsh57c6ccd3cc78306p194f8cjsn18b2c5ce9922",
	              "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
                }
      result = requests.get(link, headers = headers)
      return result.json()


    # return ({"method" : method,
    #          "URL" : link,
    #          "Key(s)" : key,
    #          "Value(s)" : value,
    #          "type" : type1})
with gr.Blocks(theme = gr.themes.Monochrome()) as demo:
    with gr.Row():
        drop = gr.Dropdown(["GET", "POST"], label="Methods", scale = 1  )
        text = gr.Textbox(label="Add Link Here", scale = 2)

    with gr.Row(visible = False) as ky[0]:
        param1 = gr.Textbox(label = "Key", scale =1)
        param2 = gr.Textbox(label = "Value", scale =1)
        param3 = gr.Textbox(label = "Type", scale =1)

    with gr.Row(visible = False) as ky[1]:
        param4 = gr.Textbox(label = "Key", scale =1)
        param5 = gr.Textbox(label = "Value", scale =1)
        param6 = gr.Textbox(label = "Type", scale =1)

    with gr.Row(visible = False) as ky[2]:
        param7 = gr.Textbox(label = "Key", scale =1)
        param8 = gr.Textbox(label = "Value", scale =1)
        param9 = gr.Textbox(label = "Type", scale =1)

    with gr.Row(visible = False) as ky[3]:
        parama = gr.Textbox(label = "Key", scale =1)
        paramb = gr.Textbox(label = "Value", scale =1)
        paramc = gr.Textbox(label = "Type", scale =1)
    with gr.Row(visible = False) as ky[4]:
        paramd = gr.Textbox(label = "Key", scale =1)
        parame = gr.Textbox(label = "Value", scale =1)
        paramf = gr.Textbox(label = "Type", scale =1)
    with gr.Row(visible = False) as ky[5]:
        paramg = gr.Textbox(label = "Key", scale =1)
        paramh = gr.Textbox(label = "Value", scale =1)
        parami = gr.Textbox(label = "Type", scale =1)


    # headers = gr.Textbox(label = "Add header here")
    
    s = gr.Slider(1, max_textboxes, value=max_textboxes, step=1, label="How many Parameters want to enter:")
    rows = []
    for i in range(max_textboxes):
        rows.append(ky[i])
    length = 0
    s.change(variable_outputs, s, rows)
    out = gr.Json(
        label= "Response"
    )
    btn6 = gr.Button("Click Me",  visible = True) 
    btn6.click(sentence_builder, inputs = [drop, text,param1, param2, param3,param4, param5, param6, param7, param8, param9,
                                          parama, paramb, paramc,paramd, parame, paramf, paramg, paramh, parami], outputs = out)

if __name__ == "__main__":
    demo.queue().launch()

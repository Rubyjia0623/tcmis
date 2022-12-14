from flask import Flask, render_template, request, make_response, jsonify,random

@app.route("/webhook3", methods=["POST"])
def webhook3():
    req = request.get_json(force=True)
    action =  req.get("queryResult").get("action")
    if (action == "keywordchoice"):
        keyword =  req.get("queryResult").get("parameters").get("keyword")
        guessnum = int(data.get("queryResult").get("parameters").get("number"))

        collection_ref = db.collection("riddle")
        docs = collection_ref.get()
        dict = doc.to_dict()

        if(keyword==dict["item"]):
            random = random.randint(1,11))
            if(random=dict["num"])
                info+=(dict["Question"])
                if guessnum == target:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return jsonify(reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return jsonify(reply)
                    
        elif(keyword==dict["place"]):
            random = random.randint(1,7))
            if(random=dict["num"])
                info+=(dict["Question"])
                if guessnum == target:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return jsonify(reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return jsonify(reply)

        elif(keyword==dict["random"]):
            random = random.randint(1,11))
            if(random=dict["num"])
                info+=(dict["Question"])
                if guessnum == target:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return jsonify(reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return jsonify(reply)

        elif(keyword==dict["slang"]):
            random = random.randint(1,7))
            if(random=dict["num"])
                info+=(dict["Question"])
                if guessnum == target:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return jsonify(reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return jsonify(reply)

    return make_response(jsonify({"fulfillmentText": info}))

if __name__ == "__main__":
    app.run()
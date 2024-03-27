def solution(queries):
    container = []
    answers = []
    
    for operation, value in queries:
        value = int(value)
        
        if operation == "ADD":
            container.append(value)
            answers.append("")
        
        elif operation == "EXISTS":
            answers.append("true" if value in container else "false")
           
        elif operation == "REMOVE":
            if value in container:
                container.remove(value)
                answers.append("true")
            else:
                answers.append("false")
                
        elif operation == "GET_NEXT":
            greater_values = [num for num in container if num > value]
            answers.append(str(min(greater_values)) if greater_values else "")
        
    return answers

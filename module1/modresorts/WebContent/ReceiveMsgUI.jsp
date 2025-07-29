<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html>
<head>

    <title>Process My PO System Items</title>
    <script type="text/javascript"></script>

<body>

    <h1>Process My PO System Items</h1>

    <br/>
    <%
        String pendingname = request.getParameter("pendingname");
        String pendingquantity = request.getParameter("pendingquantity");

        if (pendingname != null) {
            out.println("<p> Pending item for <b>" + pendingname + " </b> with quantity: <b>" + pendingquantity + " </b></p>");
            out.println("<button onclick=\"setTimeout(function() { ele=document.getElementById('showsuccess'); ele.style.display='block';},1000);\">Process Now</button>");
        } else {
            out.println("<p> No pending items at this time</p>");
        }
    %>

    <br/>
    <br/>

    <form action="receive" method="get">
        <input type="submit" value="Get Next Pending Item">
    </form>

    <p>
        <%
            if (pendingname != null) {
                out.println("<p id=showsuccess style=\"color:grey; display:none\">Message: Item for <b>" + pendingname + " </b>processed successfully.</p>");
            }
        %>
    </p>

    <hr/>
    <p>
        <form action="<%=request.getContextPath()%>/SendMsgUI.jsp" method="get">
            <input type="submit" value="Back to Create Items">
        </form>
    </p>
</body>
</html>

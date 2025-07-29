<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html>
<head>

    <title>Create My PO System Items</title>
    <script type="text/javascript"></script>

<body>

    <h1>Create My PO System Items</h1>

    <p>
        <form action="send" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity"><br><br>

            <input type="submit" value="Submit">
        </form>
    </p>

    <br/>
    <br/>
    <%
        String name = request.getParameter("name");

        if (name != null) {
            out.println("<p style=\"color:grey\">Message: Item for <b>" + name + " </b>submitted</p>");
        } else {
            out.println("<p style=\"color:grey\">Message: &lt;no message&gt;");
        }
    %>

    <hr/>
    <p>
    <form action="<%=request.getContextPath()%>/receive" method="get">
        <input type="submit" value="Go to Pending Items">
    </form>
    </p>

</body>
</html>

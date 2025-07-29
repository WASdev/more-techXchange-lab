package com.acme.modres;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import javax.annotation.Resource;
import javax.jms.*;

@WebServlet("/resorts/send")
public class MyPOSendingServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Inject the connection factory using the @Resource annotation
    @Resource(lookup = "jms/mmxCf")
    private QueueConnectionFactory qcf;

    // Inject the destination queue using the @Resource annotation
    @Resource(lookup = "jms/mmxQueue")
    private Queue queue;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String quantity = request.getParameter("quantity");

        String msg = name + ":" + quantity;

        try {
            System.out.println("[INFO] Sending message on queue: " + msg);
            sendMessage(msg);
            System.out.println("[INFO] Message sent to queue");
        } catch (JMSException e) {
            System.out.println("[ERROR] Unable to send message");
            e.printStackTrace();
        }

        response.sendRedirect("SendMsgUI.jsp?name=" + name);
    }

    public void sendMessage(String messageText) throws JMSException {
        // Create a connection and start it
        QueueConnection connection = qcf.createQueueConnection();
        connection.start();

        // Create a session and a message producer
        QueueSession session = connection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
        QueueSender sender = session.createSender(queue);

        // Create a message and send it
        TextMessage message = session.createTextMessage(messageText);
        sender.send(message);

        // Clean up
        sender.close();
        session.close();
        connection.close();
    }
}
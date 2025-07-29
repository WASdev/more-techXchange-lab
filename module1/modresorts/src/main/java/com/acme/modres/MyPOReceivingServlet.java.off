package com.acme.modres;

import javax.annotation.Resource;
import javax.jms.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/resorts/receive")
public class MyPOReceivingServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Inject the connection factory using the @Resource annotation
    @Resource(lookup = "jms/mmxCf")
    private QueueConnectionFactory qcf;

    // Inject the destination queue using the @Resource annotation
    @Resource(lookup = "jms/mmxQueue")
    private Queue queue;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        String msg = "";
        String name = "";
        String quantity = "";

        try {
            System.out.println("[INFO] Getting message from queue");
            msg = getMessage();
            System.out.println("[INFO] Got message from queue: " + msg);
        } catch (JMSException e) {
            System.out.println("[ERROR] Getting message from queue: " + msg);
            e.printStackTrace();
        }

        if (msg != null && !msg.equals("")) {
            String[] msgParts = msg.split(":");
            name = msgParts[0];
            quantity = msgParts[1];

            response.sendRedirect("ReceiveMsgUI.jsp?pendingname=" + name + "&pendingquantity=" + quantity);
        } else {
            response.sendRedirect("ReceiveMsgUI.jsp");
        }

    }

    public String getMessage() throws JMSException {
        String msg="";

        // Create a connection and start it
        QueueConnection connection = qcf.createQueueConnection();
        connection.start();

        // Create a session and a message producer
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        MessageConsumer consumer = session.createConsumer(queue);


        // Wait for a message for 3 seconds
        Message message = consumer.receive(3000);

        if (message == null) {
            System.out.println("[INFO] No messages found after 3 seconds.");
        } else {
            // Handle the message
            if (message instanceof TextMessage) {
                msg = ((TextMessage) message).getText();
                System.out.println("Received message: " + msg);
            } else {
                System.out.println("Received message of unsupported type: " + message.getClass().getName());
                msg = null;
            }
        }

        // Clean up
        consumer.close();
        session.close();
        connection.close();

        return msg;
    }

}
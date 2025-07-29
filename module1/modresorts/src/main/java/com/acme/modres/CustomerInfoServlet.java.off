package com.acme.modres;


import com.acme.modres.db.ModResortsCustomerInformation;

import java.io.IOException;
import java.io.PrintWriter;

import javax.inject.Inject;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/resorts/customers")
public class CustomerInfoServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Inject
    private ModResortsCustomerInformation customerInfo;

    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response) throws IOException {

        // Call to lib

        PrintWriter writer = response.getWriter();

        String message = "Welcome to ModResorts!";
        writer.println(message);
        writer.println("===============================");

        writer.println("ModResorts Customer Information:");
        for (String ciEntry : customerInfo.getCustomerInformation() ) {
            writer.println(ciEntry);
        }
        writer.println("===============================");
    }
}
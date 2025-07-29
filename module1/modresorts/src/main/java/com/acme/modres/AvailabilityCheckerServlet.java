package com.acme.modres;


import java.io.IOException;
import java.io.PrintWriter;
import java.util.logging.Logger;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import javax.naming.InitialContext;
import jakarta.servlet.annotation.WebServlet;

@WebServlet({ "/resorts/availability" })
public class AvailabilityCheckerServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	private static final Logger logger = Logger.getLogger(AvailabilityCheckerServlet.class.getName());

	private static InitialContext context;

	@Override
	public void init() {
		// TODO Add some migration/java upgrade issue here to cause servlet not to be initialized?
	}

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws IOException, ServletException {

		String methodName = "doGet";
		logger.entering(AvailabilityCheckerServlet.class.getName(), methodName);

		int statusCode = 200;

		Thread t1 = new Thread(new MyThread());
		if(statusCode == 200) {
			try {
				t1.start();
				t1.join();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}

		PrintWriter out = response.getWriter();
		response.setContentType("application/json");
		response.setCharacterEncoding("UTF-8");
		out.print("{\"availability\": \"true\"}");
		response.setStatus(statusCode);
	}

	/**
	 * Returns the weather information for a given city
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		doGet(request, response);
	}

	private class MyThread implements Runnable {
		public void run() {
			System.out.println("I'm running");
		}
	}
}

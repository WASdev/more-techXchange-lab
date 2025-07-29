package com.acme.modres.mbean;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

import com.google.gson.Gson;

public final class IOUtils {
	
	public static OpMetadataList getOpListFromConfig() {
		String opJson = "ops.json";
		InputStream is = IOUtils.class.getClassLoader().getResourceAsStream(opJson);

		Gson gson = new Gson();
		OpMetadataList opList =  new OpMetadataList(); //empty default
		BufferedReader reader = new BufferedReader(new InputStreamReader(is));
		opList = gson.fromJson(reader, OpMetadataList.class);
		
		return opList;
	}

}

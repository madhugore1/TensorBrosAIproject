package com.tejasbhitle.tensorbros01;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.RequestParams;

/**
 * Created by tejas on 9/9/17.
 */

public class RestClient {

    private static final String BASE_URL = "http://172.16.31.151:8888/";

    private static AsyncHttpClient client = new AsyncHttpClient();

    private static final int TIME_OUT = 1000 * 60 * 3;

    public static void get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        try {
            client.setResponseTimeout(TIME_OUT);
            client.get(getAbsoluteUrl(url), params, responseHandler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void post(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        try {
            client.setResponseTimeout(TIME_OUT);
            client.post(getAbsoluteUrl(url), params, responseHandler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void delete(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        try {
            client.delete(getAbsoluteUrl(url), params, responseHandler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static boolean isNetworkConnected(Context context) {
        ConnectivityManager manager = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = manager.getActiveNetworkInfo();
        return (networkInfo != null && networkInfo.isConnected());
    }


    private static String getAbsoluteUrl(String relativeUrl) {
        return BASE_URL + relativeUrl;
    }

}

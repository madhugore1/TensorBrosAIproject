package com.tejasbhitle.tensorbros01;

import android.app.ProgressDialog;
import android.content.Intent;
import android.support.design.widget.FloatingActionButton;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.ActivityOptionsCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;

import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.json.JSONArray;

import java.util.ArrayList;

import cz.msebera.android.httpclient.Header;

public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    ArrayList<VideoModel> videoModels;
    ProgressDialog dialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        dialog = new ProgressDialog(MainActivity.this);
        dialog.setMessage("Loading");

        recyclerView = (RecyclerView)findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        videoModels = new ArrayList<>();
        findViewById(R.id.fetch_all).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fetch("4");
            }
        });
        findViewById(R.id.fetch_cat0).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fetch("0");
            }
        });
        findViewById(R.id.fetch_cat1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fetch("1");
            }
        });
        findViewById(R.id.fetch_cat2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fetch("2");
            }
        });

        findViewById(R.id.fab).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //presentActivity(view);
                startActivity(new Intent(MainActivity.this,VideoUploadActivity.class));
            }
        });

    }

    public void presentActivity(View view) {
        ActivityOptionsCompat options = ActivityOptionsCompat.
                makeSceneTransitionAnimation(this, view, "transition");
        int revealX = (int) (view.getX() + view.getWidth() / 2);
        int revealY = (int) (view.getY() + view.getHeight() / 2);

        Intent intent = new Intent(this, VideoUploadActivity.class);
        intent.putExtra(VideoUploadActivity.EXTRA_CIRCULAR_REVEAL_X, revealX);
        intent.putExtra(VideoUploadActivity.EXTRA_CIRCULAR_REVEAL_Y, revealY);

        ActivityCompat.startActivity(this, intent, options.toBundle());
    }


    @Override
    protected void onResume() {
        super.onResume();
        //fetch();
    }

    private void updateUI(ArrayList<VideoModel> videoModels){
        recyclerView.setAdapter(new VideoAdapter(MainActivity.this,videoModels));
    }

    private void fetch(String id){
        dialog.show();
        RequestParams params = new RequestParams();

        RestClient.get("get_video/"+id, params, new JsonHttpResponseHandler(){
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                super.onSuccess(statusCode, headers, response);
                dialog.cancel();
                Log.e("onSuccess",response.toString());
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, String responseString, Throwable throwable) {
                super.onFailure(statusCode, headers, responseString, throwable);
                dialog.cancel();
                Log.e("OnFailure","Failed");
            }
        });

    }
}

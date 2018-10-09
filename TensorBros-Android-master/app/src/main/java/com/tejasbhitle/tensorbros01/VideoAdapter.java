package com.tejasbhitle.tensorbros01;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by tejas on 9/9/17.
 */

public class VideoAdapter extends RecyclerView.Adapter<VideoAdapter.ViewHolder>{

    private Context context;
    private ArrayList<VideoModel> videoModels;

    VideoAdapter(Context context, ArrayList<VideoModel> videoModels){
        this.context = context;
        this.videoModels = videoModels;
    }

    class ViewHolder extends RecyclerView.ViewHolder{
        TextView nameTextView;
        ViewHolder(View view){
            super(view);
            nameTextView = view.findViewById(R.id.nameTextView);
        }
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        return new ViewHolder(LayoutInflater.from(context).inflate(R.layout.list_item_video, parent, false));
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        VideoModel videoModel = videoModels.get(position);
        holder.nameTextView.setText(videoModel.getName());
    }

    @Override
    public int getItemCount() {
        return videoModels.size();
    }
}

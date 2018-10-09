package com.tejasbhitle.tensorbros01;

/**
 * Created by tejas on 9/10/17.
 */

public class Category {

    public static final String cat0 = "Cookery";
    public static final String cat1 = "Dance";
    public static final String cat2 = "Sports";

    public static String getCat(String cat){
        if(cat.equals("0")) return cat0;
        if(cat.equals("1")) return cat1;
        if(cat.equals("2")) return cat2;
        return cat0;
    }

}

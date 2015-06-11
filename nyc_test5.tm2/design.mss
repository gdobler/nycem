#building[zoom>=12] {
  polygon-fill: #eee;
  line-width: 0.5;
  line-color: #ddd;
}

#nyct2010[zoom>=12] {
//  polygon-fill: #eee;
  line-width: 2;
  line-color: #305d7b;
  line-opacity: .25
}


#fruits {
//  marker-comp-op: screen;
  marker-allow-overlap: true;
  marker-line-width: 0;
  marker-width: 5;
  marker-opacity: .5;
  marker-fill: #fa3500;
  [zoom>=12] { marker-width: 6.5; }
  [zoom>=13] { marker-width: 7; }
  [zoom>=14] { marker-width: 7.5; }
  [zoom>=15] { marker-width: 8.0; }
  [zoom>=16] { marker-width: 8.5; }
  [zoom>=17] { marker-width: 9.0; }
  [zoom>=18] { marker-width: 9.5; }
  [zoom>=19] { marker-width: 10.0; }
}

#landuse[class='park'] {
  polygon-fill: #dec;
}

#poi_label[maki='park'][scalerank<=3][zoom>=15] {
  text-name: @name;
  text-face-name: @sans;
  text-size: 10;
  text-wrap-width: 60;
  text-fill: #686;
  text-halo-fill: #fff;
  text-halo-radius: 1;
  text-halo-rasterizer: fast;
}

#road_label[zoom>=13] {
  text-name: @name;
  text-face-name: @sans;
  text-size: 10;
  text-placement: line;
  text-avoid-edges: true;
  text-fill: #68a;
  text-halo-fill: #fff;
  text-halo-radius: 1;
  text-halo-rasterizer: fast;
}
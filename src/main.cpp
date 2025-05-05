#include <Adafruit_NeoPixel.h>

#define PIN 48
#define NUMPIXELS 1

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
    pixels.begin();
    Serial.begin(115200);
}

void loop() {
    pixels.setPixelColor(0, pixels.Color(0, 125, 0));
    // pixels.show();
    // delay(500);

    // pixels.setPixelColor(0, pixels.Color(0, 0, 0));
    pixels.show();
    // delay(500);
}
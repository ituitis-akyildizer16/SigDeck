package com.akyildizer16.sigdeck

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import java.io.File

class SignActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign)

        val status = findViewById<TextView>(R.id.status)
        val key = File(getFilesDir(), "sigdeck.key")
        status.text = if (key.exists()) {
            "Key found. Pick a file to sign (demo: sign first 64 bytes)."
        } else {
            "No key yet - import one via the QR flow first."
        }
    }
}

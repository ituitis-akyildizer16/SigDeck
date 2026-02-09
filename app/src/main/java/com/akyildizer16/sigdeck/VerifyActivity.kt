package com.akyildizer16.sigdeck

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class VerifyActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_verify)

        findViewById<TextView>(R.id.status).text =
            "Scan the SGDK1:key QR payload to load a public key (demo placeholder)."
    }
}

# draft note 872

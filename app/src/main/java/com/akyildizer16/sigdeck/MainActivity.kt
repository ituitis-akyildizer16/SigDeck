package com.akyildizer16.sigdeck

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<Button>(R.id.sign_btn).setOnClickListener {
            startActivity(Intent(this, SignActivity::class.java))
        }
        findViewById<Button>(R.id.verify_btn).setOnClickListener {
            startActivity(Intent(this, VerifyActivity::class.java))
        }
    }
}

# draft note 865

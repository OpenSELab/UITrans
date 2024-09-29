import json

a = {
    "a": """
    <com.google.android.material.card.MaterialCardView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="16dp"
        app:cardBackgroundColor="#FF018786"
        app:cardCornerRadius="16dp"
        app:cardElevation="8dp"
        app:cardMaxElevation="12dp"
        app:cardPreventCornerOverlap="true"
        app:cardUseCompatPadding="true"
        app:contentPadding="16dp"
        app:strokeColor="#FF03DAC5"
        app:strokeWidth="2dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="16dp">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Card Title"
                android:textColor="#FFBB86FC"
                android:textSize="24sp"
                android:textStyle="bold" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="This is a sample description text for the card."
                android:textColor="#FF6200EE"
                android:textSize="16sp"
                android:paddingTop="8dp" />
        </LinearLayout>
    </com.google.android.material.card.MaterialCardView>
    """
}

print(json.dumps(a))
# caching-proxy

## 📘 Description
**caching-proxy** is a lightweight CLI tool built in Python that caches and retrieves HTTP requests to improve speed and reduce redundant API calls.

It acts as a simple caching layer between your client and the origin server — great for learning, testing, or optimizing APIs.

---

## ⚙️ Installation

### Steps to Install

1. **Clone the repository**
   ```bash
   git clone https://github.com/patrickamowe/caching-proxy.git
   ```
   Open the repository in your favourite code edit (IDE)


2. **Create and activate a virtual environment**

    On **macOS/Linux**:
   ```bash
   python3 -m venv venv
   ```
   
   ```bash
   source venv/bin/activate
   ```

   On **Windows**:
    ```bash
   python -m venv venv
   ```

   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running and Testing

1. **Start the proxy server** on your terminal
   ```bash
   python main.py --port 3000 --origin http://dummyjson.com
   ```
   You should see:
   ```
   🚀 Caching proxy started on port 3000  
   🔗 Forwarding requests to http://dummyjson.com
   ```

2. **Make your first request** on a different terminal
   ```
   curl -i http://localhost:3000/products
   ```
   Output:
   ```
   🌐 Fetching new content
   ```

3. **Send the same request again**
   ```
   curl -i http://localhost:3000/products
   ```
   Output:
   ```
   ✅ Serving from cache (fresh)
   ```

4. **After one minute**, make the same request again:
    
    Output:
    ```
    ♻️ Validated cache (still fresh)
    ```
   
5. **Clear cache**
    ```
   python main.py --clear-cache
   ```
    Output:
    ```
    🧹 All cache cleared
    ```

---

## 🌍 Using a Browser
You can also make requests directly from your browser by visiting:
```
http://localhost:3000/products
```

You can also clear cache directly from your browser by visiting:
```
http://localhost:3000/clear-cache
```

---

## 📘 License
This project is licensed under the MIT License.
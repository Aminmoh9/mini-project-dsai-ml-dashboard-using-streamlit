# 🎬 Sakila DVD Rental Analysis & Movie Prediction System

A comprehensive Streamlit web application that provides exploratory data analysis (EDA) of the Sakila DVD rental database and AI-powered movie recommendations using advanced natural language processing.

## 🌟 Features

### 🏠 Home Page
- **Interactive Dashboard**: Overview of the Sakila DVD rental system
- **Database Connection Status**: Real-time monitoring of Supabase PostgreSQL connection
- **Visual Gallery**: Movie collection showcase with representative images
- **Tech Stack Information**: Detailed breakdown of technologies used

### 📊 EDA Analysis
- **Daily Rentals Visualization**: Interactive line plot showing rental patterns by store in 2005
- **Store Filter Options**: Toggle between viewing All stores, Store 1 only, or Store 2 only
- **Revenue Analysis**: Bar chart comparing total benefit (revenue) between stores
- **Top Movies Rankings**: Data tables showing the top 5 most rented movies per store
- **Summary Statistics**: Key metrics including total rentals, revenue, and unique movies

### 🔮 Movie Recommendations
- **AI-Powered Search**: Enter movie descriptions to find similar films
- **Semantic Matching**: Uses Sentence Transformers for intelligent content-based recommendations
- **Top 3 Results**: Returns the most similar movies with titles, ratings, and similarity scores
- **Movie Browser**: Paginated view of all available movies (10 per page)
- **Visual Indicators**: Color-coded similarity scores and rating badges

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Database**: Supabase (PostgreSQL cloud hosting)
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly (interactive charts)
- **AI/ML**: Sentence Transformers, Scikit-learn
- **Database ORM**: SQLAlchemy
- **Deployment**: Cloud-ready architecture

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Internet connection (for cloud database access)
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aminmoh9/saklia_movies_prediction.git
   cd saklia_movies_prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Streamlit Secrets**
   Create a `.streamlit/secrets.toml` file in your project root:
   ```toml
   SUPABASE_CONNECTION_STRING = "your_supabase_postgresql_connection_string"
   ```

5. **Run the application**
   ```bash
   streamlit run 🏠_Home.py
   ```

6. **Access the app**
   Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
saklia_movies_prediction/
│
├── 🏠_Home.py                 # Main application entry point
├── Backend.py                 # Database connections and AI functions
├── UI_components.py           # Reusable UI components
├── requirements.txt           # Python dependencies
├── README.md                 # Project documentation
│
├── .streamlit/
│   └── secrets.toml          # Configuration secrets
│
├── pages/
│   ├── 1📊_EDA.py           # Exploratory Data Analysis page
│   └── 2📈_Predictions.py   # Movie recommendation page
│
└── images/                   # Static images for the application
    ├── action_movies.jpg
    ├── classic_films.jpg
    ├── drama_romance.jpg
    ├── dvd_store.jpg
    └── cloud_tech.jpg
```

## 🎯 Key Functionalities

### Data Analysis Features
- **Time Series Analysis**: Daily rental patterns across different stores
- **Comparative Analysis**: Store performance metrics and revenue comparison
- **Ranking Systems**: Most popular movies by rental frequency
- **Interactive Filtering**: Dynamic store selection for focused analysis

### AI Recommendation Engine
- **Semantic Search**: Uses `all-MiniLM-L6-v2` model for text embeddings
- **Cosine Similarity**: Calculates content similarity between user queries and movie descriptions
- **Real-time Processing**: Instant recommendations based on natural language input
- **Similarity Scoring**: Visual indicators showing match confidence levels

## 📊 Database Schema

The application uses the Sakila sample database, which includes:
- **Films**: 1000 movies with descriptions, ratings, and categories
- **Rentals**: Complete rental transaction history
- **Stores**: Two rental locations with full operational data
- **Customers**: Customer information and rental patterns
- **Payments**: Financial transaction records

## 🔧 Configuration

### Environment Variables
- `SUPABASE_CONNECTION_STRING`: PostgreSQL connection string for Supabase

### Customization Options
- **Store Filters**: Modify store selection options in EDA page
- **Recommendation Count**: Adjust the number of similar movies returned
- **Visual Themes**: Customize color schemes and layouts
- **Pagination**: Change movies per page in the browser

## 🚦 Usage Examples

### Finding Movie Recommendations
1. Navigate to the "Predictions" page
2. Enter a movie description (e.g., "A space adventure with aliens and spaceships")
3. Click "Get Your Prediction"
4. Review the top 3 similar movies with ratings and similarity scores

### Analyzing Store Performance
1. Go to the "EDA Analysis" page
2. Use the store filter to compare individual store performance
3. Examine the revenue bar chart for financial insights
4. Review top movie rankings by store

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👨‍💻 Author

**Amin Mohammadi**
- GitHub: [@Aminmoh9](https://github.com/Aminmoh9)
- Project: [Sakila Movies Prediction](https://github.com/Aminmoh9/mini-project-dsai-ml-dashboard-using-streamlit)

## 🙏 Acknowledgments

- **MySQL**: For providing the Sakila sample database
- **Supabase**: For cloud PostgreSQL hosting
- **Streamlit**: For the amazing web application framework
- **Hugging Face**: For the Sentence Transformers library
- **Plotly**: For interactive visualization capabilities

## 📈 Future Enhancements

- [ ] Add more sophisticated recommendation algorithms
- [ ] Implement user rating prediction
- [ ] Add customer behavior analysis
- [ ] Include seasonal trend analysis
- [ ] Expand to multiple languages support
- [ ] Add export functionality for reports

---

**Made with ❤️ using Streamlit and AI**

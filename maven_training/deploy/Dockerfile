FROM nginx:1.27-alpine

# Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy site content
COPY index.html /usr/share/nginx/html/
COPY training_schedule.html /usr/share/nginx/html/
COPY DEPENDENCY_MAP.html /usr/share/nginx/html/
COPY USAREUR_Insignia.svg /usr/share/nginx/html/
COPY pdf/ /usr/share/nginx/html/pdf/
COPY pdfjs/ /usr/share/nginx/html/pdfjs/

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]

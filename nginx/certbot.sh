#!/bin/sh

certbot certonly --webroot -w /var/www/certbot --staging --email $EMAIL -d $DOMAIN --agree-tos --force-renewal
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easyread_project.settings")
django.setup()

import pandas as pd
from musiclist.models import songitem


# Retrieve all objects from the model
objects = songitem.objects.all()
df = pd.DataFrame(columns=["Name", "Vote", "id"]);
# Process the retrieved data as needed
i = 0;
for obj in objects:
    # Access object attributes
    df.loc[i] = [obj.songname, obj.votes, obj.id]
    i=i+1;


print(df)

x = df.sort_values(by="Vote", ascending=False)
x = x.reset_index(drop=True)

x = x['Name'][0]
print(x)


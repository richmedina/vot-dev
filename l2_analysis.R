
library(dplyr)
library(ggplot2)



df = read.csv("results.csv", header = T)

eng_df = subset(df, speakerLang == "english")

ggplot(data=df, aes(x=reorder(speakerLang, -vot), y=vot*1000, fill = speakerLang)) + 
  geom_bar(stat="summary", fun="mean") + 
  geom_hline(yintercept = mean(eng_df$vot*1000), linetype="dashed", color = "red") + 
  scale_fill_brewer(palette="Set1") + 
  ggtitle("VOT productions in English\n") + 
  xlab("\nNative Language") + 
  ylab("VOT (ms)\n") + 
  theme_light() + 
  theme(
    plot.title = element_text(size=15, family = "LM Roman 10", hjust = 0.5),
    axis.title.x = element_text(size=12, family = "LM Roman 10"),
    axis.text.x = element_text(size=10, family = "LM Roman 10"),
    axis.title.y = element_text(size=12, family = "LM Roman 10"),
    axis.text.y = element_text(size=10, family = "LM Roman 10"),
    legend.position = "none"
  ) + 
  scale_x_discrete(labels=c("english" = "English", "chinese" = "Chinese", "korean" = "Korean", 
                            "thai" = "Thai", "spanish" = "Spanish", "italian" = "Italian"))

ggsave('results.png', device = 'png', width = 7, height = 4.5, units = ('in'), dpi = 600, bg = "transparent")

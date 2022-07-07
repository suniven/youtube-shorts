namespace classify_1
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.screenshot = new System.Windows.Forms.PictureBox();
            this.linkLabel = new System.Windows.Forms.LinkLabel();
            this.button_load = new System.Windows.Forms.Button();
            this.button_final = new System.Windows.Forms.Button();
            this.button_todo = new System.Windows.Forms.Button();
            this.button_not_sure = new System.Windows.Forms.Button();
            this.label_img_name = new System.Windows.Forms.Label();
            this.label_result = new System.Windows.Forms.Label();
            this.button_pre = new System.Windows.Forms.Button();
            this.label_sql = new System.Windows.Forms.Label();
            this.button_revisit = new System.Windows.Forms.Button();
            this.button_load_classified = new System.Windows.Forms.Button();
            this.button_next = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.screenshot)).BeginInit();
            this.SuspendLayout();
            // 
            // screenshot
            // 
            this.screenshot.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.screenshot.Location = new System.Drawing.Point(13, 13);
            this.screenshot.Name = "screenshot";
            this.screenshot.Size = new System.Drawing.Size(898, 492);
            this.screenshot.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.screenshot.TabIndex = 0;
            this.screenshot.TabStop = false;
            // 
            // linkLabel
            // 
            this.linkLabel.AutoSize = true;
            this.linkLabel.Location = new System.Drawing.Point(12, 508);
            this.linkLabel.Name = "linkLabel";
            this.linkLabel.Size = new System.Drawing.Size(31, 15);
            this.linkLabel.TabIndex = 1;
            this.linkLabel.TabStop = true;
            this.linkLabel.Text = "URL";
            this.linkLabel.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel_LinkClicked);
            // 
            // button_load
            // 
            this.button_load.Location = new System.Drawing.Point(540, 512);
            this.button_load.Name = "button_load";
            this.button_load.Size = new System.Drawing.Size(135, 32);
            this.button_load.TabIndex = 2;
            this.button_load.Text = "载入未分类数据";
            this.button_load.UseVisualStyleBackColor = true;
            this.button_load.Click += new System.EventHandler(this.button_load_Click);
            // 
            // button_final
            // 
            this.button_final.Location = new System.Drawing.Point(812, 512);
            this.button_final.Name = "button_final";
            this.button_final.Size = new System.Drawing.Size(98, 31);
            this.button_final.TabIndex = 3;
            this.button_final.Text = "final";
            this.button_final.UseVisualStyleBackColor = true;
            this.button_final.Click += new System.EventHandler(this.button_final_Click);
            // 
            // button_todo
            // 
            this.button_todo.Location = new System.Drawing.Point(812, 558);
            this.button_todo.Name = "button_todo";
            this.button_todo.Size = new System.Drawing.Size(98, 31);
            this.button_todo.TabIndex = 4;
            this.button_todo.Text = "todo";
            this.button_todo.UseVisualStyleBackColor = true;
            this.button_todo.Click += new System.EventHandler(this.button_todo_Click);
            // 
            // button_not_sure
            // 
            this.button_not_sure.Location = new System.Drawing.Point(812, 606);
            this.button_not_sure.Name = "button_not_sure";
            this.button_not_sure.Size = new System.Drawing.Size(98, 31);
            this.button_not_sure.TabIndex = 5;
            this.button_not_sure.Text = "not sure";
            this.button_not_sure.UseVisualStyleBackColor = true;
            this.button_not_sure.Click += new System.EventHandler(this.button_not_sure_Click);
            // 
            // label_img_name
            // 
            this.label_img_name.AutoSize = true;
            this.label_img_name.Location = new System.Drawing.Point(13, 527);
            this.label_img_name.Name = "label_img_name";
            this.label_img_name.Size = new System.Drawing.Size(31, 15);
            this.label_img_name.TabIndex = 6;
            this.label_img_name.Text = "Img";
            // 
            // label_result
            // 
            this.label_result.AutoSize = true;
            this.label_result.Location = new System.Drawing.Point(10, 665);
            this.label_result.Name = "label_result";
            this.label_result.Size = new System.Drawing.Size(82, 15);
            this.label_result.TabIndex = 7;
            this.label_result.Text = "执行结果：";
            // 
            // button_pre
            // 
            this.button_pre.Location = new System.Drawing.Point(694, 512);
            this.button_pre.Name = "button_pre";
            this.button_pre.Size = new System.Drawing.Size(98, 32);
            this.button_pre.TabIndex = 8;
            this.button_pre.Text = "上一个";
            this.button_pre.UseVisualStyleBackColor = true;
            this.button_pre.Click += new System.EventHandler(this.button_pre_Click);
            // 
            // label_sql
            // 
            this.label_sql.Location = new System.Drawing.Point(10, 642);
            this.label_sql.Name = "label_sql";
            this.label_sql.Size = new System.Drawing.Size(600, 23);
            this.label_sql.TabIndex = 9;
            this.label_sql.Text = "sql: ";
            // 
            // button_revisit
            // 
            this.button_revisit.Location = new System.Drawing.Point(812, 649);
            this.button_revisit.Name = "button_revisit";
            this.button_revisit.Size = new System.Drawing.Size(98, 31);
            this.button_revisit.TabIndex = 10;
            this.button_revisit.Text = "revisit";
            this.button_revisit.UseVisualStyleBackColor = true;
            this.button_revisit.Click += new System.EventHandler(this.button_revisit_Click);
            // 
            // button_load_classified
            // 
            this.button_load_classified.Location = new System.Drawing.Point(540, 558);
            this.button_load_classified.Name = "button_load_classified";
            this.button_load_classified.Size = new System.Drawing.Size(135, 31);
            this.button_load_classified.TabIndex = 11;
            this.button_load_classified.Text = "载入已分类数据";
            this.button_load_classified.UseVisualStyleBackColor = true;
            this.button_load_classified.Click += new System.EventHandler(this.button_load_classified_Click);
            // 
            // button_next
            // 
            this.button_next.Location = new System.Drawing.Point(694, 558);
            this.button_next.Name = "button_next";
            this.button_next.Size = new System.Drawing.Size(98, 31);
            this.button_next.TabIndex = 12;
            this.button_next.Text = "下一个";
            this.button_next.UseVisualStyleBackColor = true;
            this.button_next.Click += new System.EventHandler(this.button_next_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(922, 692);
            this.Controls.Add(this.button_next);
            this.Controls.Add(this.button_load_classified);
            this.Controls.Add(this.button_revisit);
            this.Controls.Add(this.label_sql);
            this.Controls.Add(this.button_pre);
            this.Controls.Add(this.label_result);
            this.Controls.Add(this.label_img_name);
            this.Controls.Add(this.button_not_sure);
            this.Controls.Add(this.button_todo);
            this.Controls.Add(this.button_final);
            this.Controls.Add(this.button_load);
            this.Controls.Add(this.linkLabel);
            this.Controls.Add(this.screenshot);
            this.Name = "Form1";
            this.Text = "Classify";
            this.Resize += new System.EventHandler(this.Form1_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.screenshot)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox screenshot;
        private System.Windows.Forms.LinkLabel linkLabel;
        private System.Windows.Forms.Button button_load;
        private System.Windows.Forms.Button button_final;
        private System.Windows.Forms.Button button_todo;
        private System.Windows.Forms.Button button_not_sure;
        private System.Windows.Forms.Label label_img_name;
        private System.Windows.Forms.Label label_result;
        private System.Windows.Forms.Button button_pre;
        private System.Windows.Forms.Label label_sql;
        private System.Windows.Forms.Button button_revisit;
        private System.Windows.Forms.Button button_load_classified;
        private System.Windows.Forms.Button button_next;
    }
}


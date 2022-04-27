namespace Helper
{
    partial class helper
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
            this.yt_pic_box = new System.Windows.Forms.PictureBox();
            this.tt_pic_box = new System.Windows.Forms.PictureBox();
            this.is_same = new System.Windows.Forms.Button();
            this.not_same = new System.Windows.Forms.Button();
            this.score = new System.Windows.Forms.Label();
            this.load_data = new System.Windows.Forms.Button();
            this.result_listview = new System.Windows.Forms.ListView();
            this.yt_img_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tt_img_md5_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tt_img_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.score_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.final_result_listview = new System.Windows.Forms.ListView();
            this.yt_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tt_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.yt_img_name = new System.Windows.Forms.Label();
            this.tt_img_name = new System.Windows.Forms.Label();
            this.export_data = new System.Windows.Forms.Button();
            this.not_sure = new System.Windows.Forms.Button();
            this.is_same_column_header = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.index_label = new System.Windows.Forms.Label();
            this.import_data = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.yt_pic_box)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tt_pic_box)).BeginInit();
            this.SuspendLayout();
            // 
            // yt_pic_box
            // 
            this.yt_pic_box.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.yt_pic_box.Location = new System.Drawing.Point(12, 34);
            this.yt_pic_box.Name = "yt_pic_box";
            this.yt_pic_box.Size = new System.Drawing.Size(572, 352);
            this.yt_pic_box.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.yt_pic_box.TabIndex = 0;
            this.yt_pic_box.TabStop = false;
            // 
            // tt_pic_box
            // 
            this.tt_pic_box.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.tt_pic_box.Location = new System.Drawing.Point(611, 34);
            this.tt_pic_box.Name = "tt_pic_box";
            this.tt_pic_box.Size = new System.Drawing.Size(569, 352);
            this.tt_pic_box.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.tt_pic_box.TabIndex = 1;
            this.tt_pic_box.TabStop = false;
            // 
            // is_same
            // 
            this.is_same.Font = new System.Drawing.Font("宋体", 9F);
            this.is_same.Location = new System.Drawing.Point(810, 398);
            this.is_same.Name = "is_same";
            this.is_same.Size = new System.Drawing.Size(109, 33);
            this.is_same.TabIndex = 2;
            this.is_same.Text = "是";
            this.is_same.UseVisualStyleBackColor = true;
            this.is_same.Click += new System.EventHandler(this.is_same_Click);
            // 
            // not_same
            // 
            this.not_same.Font = new System.Drawing.Font("宋体", 9F);
            this.not_same.Location = new System.Drawing.Point(939, 398);
            this.not_same.Name = "not_same";
            this.not_same.Size = new System.Drawing.Size(109, 33);
            this.not_same.TabIndex = 3;
            this.not_same.Text = "否";
            this.not_same.UseVisualStyleBackColor = true;
            this.not_same.Click += new System.EventHandler(this.not_same_Click);
            // 
            // score
            // 
            this.score.AutoSize = true;
            this.score.Font = new System.Drawing.Font("宋体", 9F);
            this.score.Location = new System.Drawing.Point(12, 398);
            this.score.Name = "score";
            this.score.Size = new System.Drawing.Size(63, 15);
            this.score.TabIndex = 6;
            this.score.Text = "Score: ";
            // 
            // load_data
            // 
            this.load_data.Font = new System.Drawing.Font("宋体", 9F);
            this.load_data.Location = new System.Drawing.Point(423, 704);
            this.load_data.Name = "load_data";
            this.load_data.Size = new System.Drawing.Size(161, 33);
            this.load_data.TabIndex = 7;
            this.load_data.Text = "加载原始数据";
            this.load_data.UseVisualStyleBackColor = true;
            this.load_data.Click += new System.EventHandler(this.load_data_Click);
            // 
            // result_listview
            // 
            this.result_listview.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.yt_img_column_header,
            this.tt_img_md5_column_header,
            this.tt_img_column_header,
            this.score_column_header});
            this.result_listview.FullRowSelect = true;
            this.result_listview.GridLines = true;
            this.result_listview.HideSelection = false;
            this.result_listview.Location = new System.Drawing.Point(12, 440);
            this.result_listview.Name = "result_listview";
            this.result_listview.Size = new System.Drawing.Size(572, 258);
            this.result_listview.TabIndex = 9;
            this.result_listview.UseCompatibleStateImageBehavior = false;
            this.result_listview.View = System.Windows.Forms.View.Details;
            this.result_listview.SelectedIndexChanged += new System.EventHandler(this.result_listview_SelectedIndexChanged);
            // 
            // yt_img_column_header
            // 
            this.yt_img_column_header.Text = "YouTube封面图片";
            this.yt_img_column_header.Width = 131;
            // 
            // tt_img_md5_column_header
            // 
            this.tt_img_md5_column_header.Text = "TikTok用户MD5";
            this.tt_img_md5_column_header.Width = 122;
            // 
            // tt_img_column_header
            // 
            this.tt_img_column_header.Text = "TikTok封面图片";
            this.tt_img_column_header.Width = 121;
            // 
            // score_column_header
            // 
            this.score_column_header.Text = "Score";
            this.score_column_header.Width = 112;
            // 
            // final_result_listview
            // 
            this.final_result_listview.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.yt_column_header,
            this.tt_column_header,
            this.is_same_column_header});
            this.final_result_listview.FullRowSelect = true;
            this.final_result_listview.GridLines = true;
            this.final_result_listview.HideSelection = false;
            this.final_result_listview.Location = new System.Drawing.Point(610, 440);
            this.final_result_listview.Name = "final_result_listview";
            this.final_result_listview.Size = new System.Drawing.Size(569, 258);
            this.final_result_listview.TabIndex = 10;
            this.final_result_listview.UseCompatibleStateImageBehavior = false;
            this.final_result_listview.View = System.Windows.Forms.View.Details;
            this.final_result_listview.SelectedIndexChanged += new System.EventHandler(this.final_result_listview_SelectedIndexChanged);
            // 
            // yt_column_header
            // 
            this.yt_column_header.Text = "YouTube封面图片";
            this.yt_column_header.Width = 164;
            // 
            // tt_column_header
            // 
            this.tt_column_header.Text = "TikTok封面图片";
            this.tt_column_header.Width = 185;
            // 
            // yt_img_name
            // 
            this.yt_img_name.AutoSize = true;
            this.yt_img_name.Location = new System.Drawing.Point(12, 13);
            this.yt_img_name.Name = "yt_img_name";
            this.yt_img_name.Size = new System.Drawing.Size(63, 15);
            this.yt_img_name.TabIndex = 11;
            this.yt_img_name.Text = "yt_img:";
            // 
            // tt_img_name
            // 
            this.tt_img_name.AutoSize = true;
            this.tt_img_name.Location = new System.Drawing.Point(611, 12);
            this.tt_img_name.Name = "tt_img_name";
            this.tt_img_name.Size = new System.Drawing.Size(63, 15);
            this.tt_img_name.TabIndex = 12;
            this.tt_img_name.Text = "tt_img:";
            // 
            // export_data
            // 
            this.export_data.Font = new System.Drawing.Font("宋体", 9F);
            this.export_data.Location = new System.Drawing.Point(1029, 705);
            this.export_data.Name = "export_data";
            this.export_data.Size = new System.Drawing.Size(151, 33);
            this.export_data.TabIndex = 13;
            this.export_data.Text = "导出结果数据";
            this.export_data.UseVisualStyleBackColor = true;
            this.export_data.Click += new System.EventHandler(this.export_data_Click);
            // 
            // not_sure
            // 
            this.not_sure.Location = new System.Drawing.Point(1072, 398);
            this.not_sure.Name = "not_sure";
            this.not_sure.Size = new System.Drawing.Size(108, 33);
            this.not_sure.TabIndex = 14;
            this.not_sure.Text = "不确定";
            this.not_sure.UseVisualStyleBackColor = true;
            this.not_sure.Click += new System.EventHandler(this.not_sure_Click);
            // 
            // is_same_column_header
            // 
            this.is_same_column_header.Text = "是否同一人";
            this.is_same_column_header.Width = 129;
            // 
            // index_label
            // 
            this.index_label.AutoSize = true;
            this.index_label.Location = new System.Drawing.Point(12, 713);
            this.index_label.Name = "index_label";
            this.index_label.Size = new System.Drawing.Size(119, 15);
            this.index_label.TabIndex = 15;
            this.index_label.Text = "Current Index:";
            // 
            // import_data
            // 
            this.import_data.Location = new System.Drawing.Point(610, 704);
            this.import_data.Name = "import_data";
            this.import_data.Size = new System.Drawing.Size(151, 34);
            this.import_data.TabIndex = 16;
            this.import_data.Text = "导入结果数据";
            this.import_data.UseVisualStyleBackColor = true;
            this.import_data.Click += new System.EventHandler(this.import_data_Click);
            // 
            // helper
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1192, 749);
            this.Controls.Add(this.import_data);
            this.Controls.Add(this.index_label);
            this.Controls.Add(this.not_sure);
            this.Controls.Add(this.export_data);
            this.Controls.Add(this.tt_img_name);
            this.Controls.Add(this.yt_img_name);
            this.Controls.Add(this.final_result_listview);
            this.Controls.Add(this.result_listview);
            this.Controls.Add(this.load_data);
            this.Controls.Add(this.score);
            this.Controls.Add(this.not_same);
            this.Controls.Add(this.is_same);
            this.Controls.Add(this.tt_pic_box);
            this.Controls.Add(this.yt_pic_box);
            this.Name = "helper";
            this.Text = "Helper";
            this.Load += new System.EventHandler(this.helper_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.yt_pic_box)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tt_pic_box)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox yt_pic_box;
        private System.Windows.Forms.PictureBox tt_pic_box;
        private System.Windows.Forms.Button is_same;
        private System.Windows.Forms.Button not_same;
        private System.Windows.Forms.Label score;
        private System.Windows.Forms.Button load_data;
        private System.Windows.Forms.ListView result_listview;
        private System.Windows.Forms.ColumnHeader yt_img_column_header;
        private System.Windows.Forms.ColumnHeader tt_img_md5_column_header;
        private System.Windows.Forms.ColumnHeader tt_img_column_header;
        private System.Windows.Forms.ColumnHeader score_column_header;
        private System.Windows.Forms.ListView final_result_listview;
        private System.Windows.Forms.ColumnHeader yt_column_header;
        private System.Windows.Forms.ColumnHeader tt_column_header;
        private System.Windows.Forms.Label yt_img_name;
        private System.Windows.Forms.Label tt_img_name;
        private System.Windows.Forms.Button export_data;
        private System.Windows.Forms.Button not_sure;
        private System.Windows.Forms.ColumnHeader is_same_column_header;
        private System.Windows.Forms.Label index_label;
        private System.Windows.Forms.Button import_data;
    }
}


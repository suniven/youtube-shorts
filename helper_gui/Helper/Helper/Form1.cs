using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using MySql.Data.MySqlClient;

namespace Helper
{
    public partial class helper : Form
    {
        public String[] results;

        #region 控件大小随窗体大小等比例缩放
        private float x;//定义当前窗体的宽度
        private float y;//定义当前窗体的高度
        private void setTag(Control cons)
        {
            foreach (Control con in cons.Controls)
            {
                con.Tag = con.Width + ";" + con.Height + ";" + con.Left + ";" + con.Top + ";" + con.Font.Size;
                if (con.Controls.Count > 0)
                {
                    setTag(con);
                }
            }
        }
        private void setControls(float newx, float newy, Control cons)
        {
            //遍历窗体中的控件，重新设置控件的值
            foreach (Control con in cons.Controls)
            {
                //获取控件的Tag属性值，并分割后存储字符串数组
                if (con.Tag != null)
                {
                    string[] mytag = con.Tag.ToString().Split(new char[] { ';' });
                    //根据窗体缩放的比例确定控件的值
                    con.Width = Convert.ToInt32(System.Convert.ToSingle(mytag[0]) * newx);//宽度
                    con.Height = Convert.ToInt32(System.Convert.ToSingle(mytag[1]) * newy);//高度
                    con.Left = Convert.ToInt32(System.Convert.ToSingle(mytag[2]) * newx);//左边距
                    con.Top = Convert.ToInt32(System.Convert.ToSingle(mytag[3]) * newy);//顶边距
                    Single currentSize = System.Convert.ToSingle(mytag[4]) * newy;//字体大小
                    con.Font = new Font(con.Font.Name, currentSize, con.Font.Style, con.Font.Unit);
                    if (con.Controls.Count > 0)
                    {
                        setControls(newx, newy, con);
                    }
                }
            }
        }
        private void Form1_Resize(object sender, EventArgs e)
        {
            float newx = (this.Width) / x;
            float newy = (this.Height) / y;
            setControls(newx, newy, this);
        }

        #endregion

        public helper()
        {
            InitializeComponent();
            x = this.Width;
            y = this.Height;
            setTag(this);
        }

        private void helper_Load(object sender, EventArgs e)
        {

        }

        private void load_data_Click(object sender, EventArgs e)
        {   
            this.result_listview.Items.Clear();

            string path = string.Empty;
            OpenFileDialog openFileDialog = new OpenFileDialog()
            {
                InitialDirectory = "D:\\Python\\youtube-tiktok\\",
                Filter = "Files (*.txt)|*.txt"  // 筛选txt文件
            };

            // var result = openFileDialog.ShowDialog();
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                // path = openFileDialog.FileName;
                // MessageBox.Show("成功打开文件：" + openFileDialog.FileName);    //显示选择的文件名
                FileStream fs = new FileStream(openFileDialog.FileName, FileMode.Open);
                StreamReader sr = new StreamReader(fs, Encoding.UTF8);
                String line;
                while ((line = sr.ReadLine()) != null)  // ReadLine()不包括换行符
                {
                    String[] strs = line.Split('\t');
                    String yt_img = strs[0];
                    String tt_md5 = strs[1];
                    String tt_img = String.Empty;
                    String score = strs[2];

                    // 连接数据库通过md5查询图片              
                    var connectionString = new MySqlConnectionStringBuilder
                    {
                        Server = "localhost",
                        Port = 3306,
                        UserID = "root",
                        Password = "1101syw",
                        Database = "test"  // 数据库
                    }.ToString();
                    var connection = new MySqlConnection(connectionString);
                    try
                    {
                        connection.Open();
                        var sql = "SELECT * FROM tt_cover WHERE user_id like '" + tt_md5 + "';";
                        var command = new MySqlCommand(sql, connection);
                        using (MySqlDataReader dataReader = command.ExecuteReader())
                        {
                            while (dataReader.Read())
                            {
                                tt_img = dataReader.GetString("file_name");
                                break;  // 如果有多条只返回第一条就行了
                            }
                        }
                    }
                    catch (MySqlException err)
                    {
                        Console.WriteLine(err.Message);
                    }
                    finally
                    {
                        connection.Close();
                    }

                    ListViewItem item = new ListViewItem(new string[] { yt_img, tt_md5, tt_img, score });
                    this.result_listview.Items.Add(item);
                }
                fs.Dispose();
                sr.Dispose();
            }           
        }

        private void to_next_result_listview_item()
        {
            if (this.result_listview.SelectedItems.Count == 0)
                return;
            else
            {
                // 自动切换到Listview的下一行
                if (this.result_listview.SelectedItems[0].Index == this.result_listview.Items.Count-1)
                    return;
                else
                {
                    int index = this.result_listview.SelectedItems[0].Index + 1;
                    this.result_listview.Items[index].Selected = true;
                    this.result_listview.Items[index - 1].Selected = false;
                    this.result_listview.Items[index].EnsureVisible();
                }
            }
        }

        private void not_same_Click(object sender, EventArgs e)
        {
            this.to_next_result_listview_item();
        }

        private void is_same_Click(object sender, EventArgs e)
        {
            String yt = this.result_listview.SelectedItems[0].Text;
            String tt = this.result_listview.SelectedItems[0].SubItems[2].Text;
            String is_same = "Yes";
            ListViewItem item = new ListViewItem(new string[] { yt, tt, is_same });
            this.final_result_listview.Items.Add(item);
            this.to_next_result_listview_item();

            this.to_next_result_listview_item();
        }

        private void not_sure_Click(object sender, EventArgs e)
        {
            String yt = this.result_listview.SelectedItems[0].Text;
            String tt = this.result_listview.SelectedItems[0].SubItems[2].Text;
            String is_same = "Not Sure";
            ListViewItem item = new ListViewItem(new string[] { yt, tt, is_same });
            this.final_result_listview.Items.Add(item);

            this.to_next_result_listview_item();
        }

        private void result_listview_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.result_listview.SelectedItems.Count == 0)
                return;
            else
            {
                this.index_label.Text = "Current Index: " + this.result_listview.SelectedItems[0].Index.ToString();
                String yt_name = result_listview.SelectedItems[0].Text + ".jpg";
                String tt_name = result_listview.SelectedItems[0].SubItems[2].Text + ".jpg";
                this.yt_img_name.Text = "yt_img: " + yt_name;
                this.tt_img_name.Text = "tt_img: " + tt_name;
                this.score.Text = "Score: " + result_listview.SelectedItems[0].SubItems[3].Text;

                String yt_img_path = "D:\\Python\\youtube-tiktok\\cover_img\\yt\\" + yt_name;
                String tt_img_path = "D:\\Python\\youtube-tiktok\\cover_img\\tt\\" + tt_name;
                
                FileStream fs_yt = new FileStream(yt_img_path, FileMode.Open, FileAccess.Read);
                this.yt_pic_box.Image = Image.FromStream(fs_yt);
                FileStream fs_tt = new FileStream(tt_img_path, FileMode.Open, FileAccess.Read);
                this.tt_pic_box.Image = Image.FromStream(fs_tt);
                fs_yt.Close();
                fs_yt.Dispose();
                fs_tt.Close();
                fs_tt.Dispose();
                
            }
        }

        private void export_data_Click(object sender, EventArgs e)
        {
            if (this.final_result_listview.Items.Count > 0)
            {
                FolderBrowserDialog dialog = new FolderBrowserDialog();
                dialog.Description = "请选择文件保存路径";
                String save_path = String.Empty;
                if (dialog.ShowDialog() == DialogResult.OK)
                {
                    save_path = dialog.SelectedPath + @"\" + "final_result.txt";
                    FileStream fs= new FileStream(save_path, FileMode.Create, FileAccess.ReadWrite);
                    StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);
                    foreach (ListViewItem item in this.final_result_listview.Items)
                    {
                        String str = item.Text + "\t" + item.SubItems[1].Text + "\t" + item.SubItems[2].Text;
                        sw.WriteLine(str);
                        sw.Flush();
                    } 
                    sw.Close();
                    sw.Dispose();
                    fs.Close();
                    fs.Dispose();
                    MessageBox.Show("结果数据导出成功！");
                }
            }
            else
                return;
        }

        private void import_data_Click(object sender, EventArgs e)
        {
            this.final_result_listview.Items.Clear();
            OpenFileDialog openFileDialog = new OpenFileDialog()
            {
                InitialDirectory = "D:\\Python\\youtube-tiktok\\",
                Filter = "Files (*.txt)|*.txt"  // 筛选txt文件
            };
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                FileStream fs = new FileStream(openFileDialog.FileName, FileMode.Open);
                StreamReader sr = new StreamReader(fs, Encoding.UTF8);
                String line;
                while ((line = sr.ReadLine()) != null)  // ReadLine()不包括换行符
                {
                    String[] strs = line.Split('\t');
                    String yt_img = strs[0];
                    String tt_img = strs[1];
                    String is_same = strs[2];

                    ListViewItem item = new ListViewItem(new string[] { yt_img, tt_img, is_same });
                    this.final_result_listview.Items.Add(item);
                }
                fs.Dispose();
                sr.Dispose();
            }
        }

        private void final_result_listview_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.final_result_listview.SelectedItems.Count == 0)
                return;
            else
            {
                String yt_name = final_result_listview.SelectedItems[0].Text + ".jpg";
                String tt_name = final_result_listview.SelectedItems[0].SubItems[1].Text + ".jpg";
                this.yt_img_name.Text = "yt_img: " + yt_name;
                this.tt_img_name.Text = "tt_img: " + tt_name;
                this.score.Text = "Score: NaN";
                this.index_label.Text = "Current Index: NaN";

                String yt_img_path = "D:\\Python\\youtube-tiktok\\cover_img\\yt\\" + yt_name;
                String tt_img_path = "D:\\Python\\youtube-tiktok\\cover_img\\tt\\" + tt_name;

                FileStream fs_yt = new FileStream(yt_img_path, FileMode.Open, FileAccess.Read);
                this.yt_pic_box.Image = Image.FromStream(fs_yt);
                FileStream fs_tt = new FileStream(tt_img_path, FileMode.Open, FileAccess.Read);
                this.tt_pic_box.Image = Image.FromStream(fs_tt);
                fs_yt.Close();
                fs_yt.Dispose();
                fs_tt.Close();
                fs_tt.Dispose();

            }
        }
    }
}

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;
using System.IO;
using MySql.Data.MySqlClient;

namespace classify_1
{
    public partial class Form1 : Form
    {
        private Dictionary<string, string> img_dic = new Dictionary<string, string>();
        // 截图列表
        private ArrayList img_list = new ArrayList();
        private String current_link;
        private int current_list_index = 0;

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

        public Form1()
        {
            InitializeComponent();
            x = this.Width;
            y = this.Height;
            setTag(this);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button_load_Click(object sender, EventArgs e)
        {
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
                var sql = "SELECT DISTINCT landing_page, landing_page_md5 FROM round_1 WHERE checked like '' and status_code like '200';";
                var command = new MySqlCommand(sql, connection);
                using (MySqlDataReader dataReader = command.ExecuteReader())
                {
                    while (dataReader.Read())
                    {
                        String img_name = dataReader.GetString("landing_page_md5");
                        String landing_page = dataReader.GetString("landing_page");
                        img_dic.Add(img_name, landing_page);
                        img_list.Add(img_name);
                    }
                    if (img_list.Count==0)
                    {
                        MessageBox.Show("没有需要分类的数据。");
                    }
                }
            }
            catch (MySqlException err)
            {
                Console.WriteLine(err.Message);
                MessageBox.Show(err.Message);
            }
            finally
            {
                connection.Close();
                connection.Dispose();
            }

            if (img_list.Count>=1)
            {
                String img_path = "D:\\Python\\youtube-tiktok\\landing page\\data\\round-1\\" + img_list[0].ToString() + ".png";
                if (File.Exists(img_path))
                {
                    FileStream fs_img = new FileStream(img_path, FileMode.Open, FileAccess.Read);
                    this.screenshot.Image = Image.FromStream(fs_img);
                    fs_img.Close();
                    fs_img.Dispose();
                    if (img_dic[img_list[0].ToString()].Length > 60)
                        this.linkLabel.Text = img_dic[img_list[0].ToString()].Substring(0, 60) + "...";
                    else
                        this.linkLabel.Text = img_dic[img_list[0].ToString()];
                    this.label_img_name.Text = img_list[0].ToString();
                    this.current_link = img_dic[img_list[0].ToString()];
                }
                else
                {
                    this.screenshot.Image = null;
                    label_img_name.Text = "截图文件不存在";
                }
            }
        }

        private void update_mysql_data(String landing_page_md5, String type)
        {
            var rows = 0;
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
                var sql = "update round_1 set checked = '" + type + "' where landing_page_md5 like '" + landing_page_md5 + "';";
                // MessageBox.Show(sql);
                var command = new MySqlCommand(sql, connection);
                rows = command.ExecuteNonQuery();//执行SQL语句，并返回受影响的行数
                this.label_sql.Text = "sql: " + sql;
            }
            catch (MySqlException err)
            {
                Console.WriteLine(err.Message);
                this.label_result.Text = err.Message;
            }
            finally
            {
                this.label_result.Text = "执行结果：" + type + " 成功。" + "Affected rows: " + rows.ToString();
                connection.Close();
                connection.Dispose();
            }
        }

        private void show_img()
        {
            if (this.current_list_index < img_list.Count)
            {
                String img_path = "D:\\Python\\youtube-tiktok\\landing page\\data\\round-1\\" + img_list[current_list_index].ToString() + ".png";
                if (File.Exists(img_path))
                {
                    FileStream fs_img = new FileStream(img_path, FileMode.Open, FileAccess.Read);
                    this.screenshot.Image = Image.FromStream(fs_img);
                    fs_img.Close();
                    fs_img.Dispose();
                    if (img_dic[img_list[current_list_index].ToString()].Length > 60)
                        this.linkLabel.Text = img_dic[img_list[current_list_index].ToString()].Substring(0, 60) + "...";
                    else
                        this.linkLabel.Text = img_dic[img_list[current_list_index].ToString()];
                    this.label_img_name.Text = img_list[current_list_index].ToString();
                    this.current_link = img_dic[img_list[current_list_index].ToString()];
                }
                else
                {
                    this.screenshot.Image = null;
                    label_img_name.Text = "截图文件不存在";
                }
            }
            else
            {
                MessageBox.Show("All checked!");
            }
        }

        private void button_final_Click(object sender, EventArgs e)
        {
            update_mysql_data(img_list[current_list_index].ToString(), "final");
            this.current_list_index++;
            show_img();
        }

        private void button_todo_Click(object sender, EventArgs e)
        {
            update_mysql_data(img_list[current_list_index].ToString(), "todo");
            this.current_list_index++;
            show_img();
        }

        private void button_not_sure_Click(object sender, EventArgs e)
        {
            update_mysql_data(img_list[current_list_index].ToString(), "not sure");
            this.current_list_index++;
            show_img();
        }

        private void linkLabel_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(this.current_link);  // 调用浏览器打开链接以确定空白截图或其余不确定的部分
        }

        private void button_pre_Click(object sender, EventArgs e)
        {
            if (this.current_list_index >= 1)
            {
                this.current_list_index--;
                show_img();
            }
            else
                MessageBox.Show("已经是第一个");
        }
    }
}

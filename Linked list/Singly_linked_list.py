# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:50:02 2022

@author: nick
"""
class Node(object):
    """聲明節點"""
    def __init__(self, element):
        self.element = element  # 給定一個元素
        self.next = None  # 初始設置下一節點為空
        
        
class Singly_linked_list:
    """Python實現單鏈表"""
    def __init__(self):
        self.__head = None  # head設置為私有屬性，禁止外部訪問
    def is_empty(self):
        """判斷鏈表是否為空"""
        return self.__head is None
    def length(self):
        """返回鏈表長度"""
        cur = self.__head  # cur遊標，用來移動遍歷節點
        count = 0  # count記錄節點數量
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    def travel_list(self):
        """遍歷整個鏈表，打印每個節點的數據"""
        cur = self.__head
        while cur is not None:
            print(cur.element, end=" ")
            cur = cur.next
            print("\n")
    def insert_head(self, element):
        """頭插法：在單鏈表頭部插入一個節點"""
        newest = Node(element)  # 創建一個新節點
        if self.__head is not None:  # 如果初始不為空，就將新節點的"next"指針指向head
            newest.next = self.__head
        self.__head = newest  # 把新節點設置為head
    def insert_tail(self, element):
        """尾插法：在單鏈表尾部增加一個節點"""
        if self.__head is None:
            self.insert_head(element)  # 如果這是第一個節點，調用insert_head函數
        else:
            cur = self.__head
            while cur.next is not None:  # 遍歷到最後一個節點
                cur = cur.next
            cur.next = Node(element)  # 創建新節點並連接到最後
    def insert(self, pos, element):
        """指定位置插入元素""" 
        # 如果位置在0或者之前，調用頭插法
        if pos < 0:
            self.insert_head(element)
            # 如果位置在原鏈表長度之後，調用尾插法
        elif pos > self.length() - 1:
            self.insert_tail(element)
        else:
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            newest = Node(element)
            newest.next = cur.next
            cur.next = newest
    def delete_head(self):
        
        """刪除頭結點"""
        #cur = self.__head
        if self.__head is not None:
            self.__head = self.__head.next
        #    cur.next = None
        #return cur
    def delete_tail(self): 
        """刪除尾節點"""
        cur = self.__head 
        if self.__head is not None:
            if self.__head.next is None:  # 如果頭結點是唯一的節點
                self.__head = None
            else:
                while cur.next.next is not None:
                    cur = cur.next                   
                #cur.next, cur = (None, cur.next)
                cur.next = None
                
    def remove(self, element): 
        """刪除指定元素"""
        cur, prev = self.__head, None
        while cur is not None:
            if cur.element == element:
                if cur == self.__head:  # 如果該節點是頭結點
                    self.__head = cur.next
                else:
                    prev.next = cur.next
                    break
            else:
                prev, cur = cur, cur.next
        return cur.element
    def modify(self, pos, element):
        """修改指定位置的元素"""
        cur = self.__head
        if pos < 1 or pos > self.length():
            return False
        for i in range(pos - 1):
            cur = cur.next
        cur.element = element
        #return cur
    def search(self, element):
        """查找節點是否存在"""
        cur = self.__head
        if cur:
            counter = 1
            
        while cur:
            if cur.element == element:
                return counter, True
            else:
                cur = cur.next
                counter += 1                
        return 0, False
    def reverse_list(self):
        """反轉整個鏈表"""
        cur, prev = self.__head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            self.__head = prev


def main():
    List1 = Singly_linked_list()
    print("鏈表是否為空", List1.is_empty())
    List1.insert_head(1)
    List1.insert_head(2)
    List1.insert_tail(3)
    List1.insert_tail(4)
    List1.insert_tail(5)
    length_of_list1 = List1.length()
    print("插入節點後，List1 的長度為：", length_of_list1)
    print("遍歷並打印整個鏈表: ")
    List1.travel_list()
    print("反轉整個鏈表: ")
    List1.reverse_list() 
    List1.travel_list()
    print("刪除頭節點: ")
    List1.delete_head()
    List1.travel_list()
    print("刪除尾節點: ")
    List1.delete_tail()
    List1.travel_list()
    print("在第二個位置插入5: ")
    List1.insert(1, 5)
    List1.travel_list()
    print("在第-1個位置插入100：")
    List1.insert(-1, 100)
    List1.travel_list()
    print("在第100個位置插入2：")
    List1.insert(100, 2)
    List1.travel_list()
    print("刪除元素：", List1.remove(5))
    List1.travel_list()
    print("修改第5個位置的元素為7: ")
    List1.modify(5, 7)
    List1.travel_list()
    print("查找元素1:")
    print(List1.search(1))
if __name__ == "__main__":
    main()
# sectionPair class

class SectionPair:
    class Section:
        def __init__(self, sect):
            temp_sect = sect.split("-")
            self.section = [int(t) for t in temp_sect]
            self.complete_section = [i for i in range(self.section[0], self.section[1] + 1)]
            self.range = self.section[1] - self.section[0] + 1

        def __str__(self):
            return f"{self.section} ({self.range})"

    def __init__(self, pair):
        section_pair = pair.split(",")
        self.section1 = self.Section(section_pair[0])
        self.section2 = self.Section(section_pair[1])

    def overlap(self):
        count = 0
        if self.section1.range < self.section2.range:
            for sect in self.section1.complete_section:
                if sect in self.section2.complete_section:
                    count += 1
        else:
            for sect in self.section2.complete_section:
                if sect in self.section1.complete_section:
                    count += 1
        return count

    def enclosed(self):
        if self.section1.range < self.section2.range:
            return self.overlap() == self.section1.range
        else:
            return self.overlap() == self.section2.range

    def __str__(self):
        bool = "YES!" if self.enclosed() else "NO"
        return f"{self.section1.__str__()}\n{self.section2.__str__()}\n" \
               f"Overlap : {self.overlap()}\n{bool}"

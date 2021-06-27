class Locker(object):
    locker_data = []

    def __init__(self, input):
        input = input.split()
        self.command = input[0]
        self.args = input[1:]

    def validate(self):
        no_argument = ['status', 'exit']
        single_argument = ['search', 'find', 'leave', 'init']
        two_argument = ['input']
        available_command = ['status', 'exit', 'search', 'find', 'leave', 'init', 'input']
        message = None

        if self.command not in available_command:
            message = "%s pilihan tidak ada ada." % self.command
        elif self.command != 'init' and self.command != 'exit' and len(self.locker_data) < 1:
            message = "Anda belum memasukan jumlah loker."
        elif self.command in single_argument and len(self.args) != 1:
            message = "%s Hanya bisa 1 argument." % self.command
        elif self.command in two_argument and len(self.args) != 2:
            message = "%s Sukses membuat loker dengan jumlah." % self.command
        elif self.command in no_argument and len(self.args):
            message = "%s tidak bisa menerima argument." % self.command

        return message

    def run(self):
        error_message = self.validate()
        if error_message:
            print(error_message)
            return False

        if self.command == 'init':
            if len(self.locker_data):
                self.locker_data.clear()
            return self.init()
        elif self.command == 'exit':
            return self.exit()
        elif self.command == 'status':
            return self.status()
        elif self.command == 'leave':
            return self.leave()
        elif self.command == 'input':
            return self.input()
        elif self.command == 'search':
            return self.search()
        elif self.command == 'find':
            return self.find()

        return False

    def init(self):
        try:
            jumlah_loker = int(self.args[0])
            if jumlah_loker < 1:
                print("argument harus angka, mulai dari 1.")
                return False

            for i in range(jumlah_loker):
                self.locker_data.append([i + 1, None, None])

            print("Sukses membuat loker dengan jumlah %s." % jumlah_loker)

        except:
            print("argument harus angka, mulai dari angka 1.")

    def input(self):
        input = self.args
        kode_tipe = input[0]
        kode_nomer = input[1]

        loker_ada = False
        no_loker = 0

        for loker in self.locker_data:
            if loker[1]:
                continue
            else:
                loker_ada = True
                no_loker = loker[0]
                break

        if not loker_ada:
            print("Loker sudah terisi.")
            return False

        self.locker_data[no_loker-1] = [no_loker, kode_tipe, kode_nomer]
        print("Kartu identitas sudah tersimpan pada loker nomer %d." % no_loker)

    def status(self):
        print("No loker  Tipe identitas           No identitas\n")
        for loker in self.locker_data:
            no = loker[0]
            kode_tipe = loker[1] or 'kosong'
            kode_nomer = loker[2] or 'kosong'
            print("%d       %s                      %s" %
                  (no, kode_tipe, kode_nomer))

    def find(self):
        no_loker = 0
        for loker in self.locker_data:
            if loker[2] == self.args[0]:
                no_loker = loker[0]
                break
        if no_loker:
            print("Kartu identitas %s berada pada loker nomer %s." % (self.args[0], no_loker))
        else:
            print("Nomer identitas tidak ada.")

    def search(self):
        id_numbers = []
        for locker in self.locker_data:
            if locker[1] == self.args[0]:
                id_numbers.append(locker[2])

        if id_numbers:
            id_numbers = ', '.join(id_numbers)
            print("No identitas dengan tipe %s: %s." % (self.args[0], id_numbers))
        else:
            print("Tipe identitas tidak ada.")

    def leave(self):
        if int(self.args[0]) > len(self.locker_data):
            print("Hanya bisa mengosongkan loker dari 1 - %s." % len(self.locker_data))
            return False

        no_loker = int(self.args[0])
        self.locker_data[no_loker-1] = [no_loker, None, None]
        print("Loker no %s berhasil dikosongkan." % no_loker)

    def exit(self):
        return exit()





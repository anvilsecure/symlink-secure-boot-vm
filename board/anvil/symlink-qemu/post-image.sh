#!/bin/bash


# create  log disk image
STORAGE_IMAGE="${BINARIES_DIR}/storage.img"
if [ ! -f ${STORAGE_IMAGE} ]; then
	fallocate -l 20M ${STORAGE_IMAGE}
	mkfs.ext4 -j ${STORAGE_IMAGE}
fi

START_QEMU_SCRIPT="${BINARIES_DIR}/start-qemu.sh"

cat <<-_EOF_ > "${START_QEMU_SCRIPT}"
#!/bin/sh
IMAGE_DIR="\${0%/*}/"

if [ "\${1}" = "serial-only" ]; then
    EXTRA_ARGS='-nographic'
else
    EXTRA_ARGS='-serial stdio'
fi

PORT_FWD='hostfwd=tcp::8888-:80,hostfwd=tcp::2121-:21'

exec   qemu-system-x86_64 -M pc -kernel \${IMAGE_DIR}/bzImage -drive file=\${IMAGE_DIR}/storage.img,if=virtio,format=raw -append "root=/dev/ram0 console=tty1 console=ttyS0"  -net nic,model=virtio -net user,\${PORT_FWD}  \${EXTRA_ARGS}

echo "Failed to launch qemu-system-x86_64, make sure it is in your PATH"
_EOF_

chmod +x "${START_QEMU_SCRIPT}"

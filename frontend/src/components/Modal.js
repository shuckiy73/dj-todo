import React, { useState } from "react";
import PropTypes from "prop-types";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

const CustomModal = ({ activeItem, toggle, onSave }) => {
  const [item, setItem] = useState(activeItem || {
    title: "",
    description: "",
    completed: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setItem({
      ...item,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSave = () => {
    if (!item.title.trim()) {
      alert("Заголовок не может быть пустым!");
      return;
    }
    onSave(item);
  };

  return (
    <Modal isOpen={true} toggle={toggle}>
      <ModalHeader toggle={toggle}>Задача</ModalHeader>
      <ModalBody>
        <Form>
          <FormGroup>
            <Label for="title">Заголовок</Label>
            <Input
              type="text"
              name="title"
              value={item.title}
              onChange={handleChange}
              placeholder="Введите заголовок задачи"
            />
          </FormGroup>
          <FormGroup>
            <Label for="description">Описание</Label>
            <Input
              type="text"
              name="description"
              value={item.description}
              onChange={handleChange}
              placeholder="Введите описание задачи"
            />
          </FormGroup>
          <FormGroup check>
            <Label for="completed">
              <Input
                type="checkbox"
                name="completed"
                checked={item.completed}
                onChange={handleChange}
              />
              Выполнено
            </Label>
          </FormGroup>
        </Form>
      </ModalBody>
      <ModalFooter>
        <Button color="success" onClick={handleSave}>
          Сохранить
        </Button>
      </ModalFooter>
    </Modal>
  );
};

CustomModal.propTypes = {
  activeItem: PropTypes.shape({
    title: PropTypes.string,
    description: PropTypes.string,
    completed: PropTypes.bool,
  }),
  toggle: PropTypes.func.isRequired,
  onSave: PropTypes.func.isRequired,
};

CustomModal.defaultProps = {
  activeItem: {
    title: "",
    description: "",
    completed: false,
  },
};

export default CustomModal;
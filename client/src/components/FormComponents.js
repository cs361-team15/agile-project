import styled from '@emotion/styled';

const Input = styled.input`
  border: 1px solid #ababab;
  padding: 5px;
  font-size: 18px;
`;

const TextArea = Input.withComponent('textarea');

const Button = styled.button`
  background-color: #2b7bbe;
  color: #fff;
  border: 2px solid #2b7bbe;
  border-radius: 3px;
  font-size: 18px;
  font-weight: 300;
  padding: 5px 10px;
  margin: 5px;
  cursor: pointer;
  &:hover {
    background-color: #71b5ed;
  }
`;

export { Input, TextArea, Button };
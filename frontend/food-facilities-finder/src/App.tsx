import { useState, useMemo } from "react";
import { Card, Input, List, Typography, Select, Spin, Alert } from "antd";
import { useFoodFacilities } from "./hooks/useFoodFacilities";
import type { FoodFacility } from "./types/FoodFacility";

const { Title } = Typography;
const { Option } = Select;

export default function App() {
  const { data, loading, error } = useFoodFacilities();
  const [searchText, setSearchText] = useState("");
  const [statusFilter, setStatusFilter] = useState<string | null>(null);

  // Filter facilities based on search and status
  const filteredFacilities = useMemo(() => {
    return data.filter((facility) => {
      const matchesApplicant = facility.applicant
        .toLowerCase()
        .includes(searchText.toLowerCase());
      const matchesAddress = facility.address
        .toLowerCase()
        .includes(searchText.toLowerCase());
      const matchesStatus = statusFilter
        ? facility.status === statusFilter
        : true;
      return (matchesApplicant || matchesAddress) && matchesStatus;
    });
  }, [data, searchText, statusFilter]);

  if (loading) {
    return <Spin tip="Loading data..." style={{ margin: 40 }} />;
  }

  if (error){
    return <Alert message="Error" description={error} type="error" />;
  } 

  return (
    <div style={{ maxWidth: 800, margin: "40px auto" }}>
      <Card>
        <Title level={2}>SF Mobile Food Facilities</Title>

        <Input.Search
          placeholder="Search by applicant or street name"
          allowClear
          enterButton
          onSearch={(val) => setSearchText(val)}
          onChange={(e) => setSearchText(e.target.value)}
          style={{ marginBottom: 20 }}
        />

        <Select
          placeholder="Filter by status"
          allowClear
          onChange={(val) => setStatusFilter(val)}
          style={{ width: 200, marginBottom: 20 }}
        >
          <Option value="APPROVED">APPROVED</Option>
          <Option value="REQUESTED">REQUESTED</Option>
          <Option value="EXPIRED">EXPIRED</Option>
        </Select>

        <List
          bordered
          dataSource={filteredFacilities}
          locale={{ emptyText: "No food facilities found." }}
          renderItem={(facility: FoodFacility) => (
            <List.Item>
              <List.Item.Meta
                title={facility.applicant}
                description={
                  <>
                    <div>
                      <strong>Address:</strong> {facility.address}
                    </div>
                    <div>
                      <strong>Status:</strong> {facility.status}
                    </div>
                    <div>
                      <strong>Food Items:</strong> {facility.fooditems}
                    </div>
                  </>
                }
              />
            </List.Item>
          )}
        />
      </Card>
    </div>
  );
}

# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

Costs
- *A VM can be more expensive as there is a need to manage the infrastructure.  App Service on the other hand can be more cost-effective for smaller applications as it doesn't need to manage the infrastructure anumre.  Pricing is based on the chosen tier.*

Scalability
- "VM is scalable but manual and requires configuring additonal VMs.  App Service on the other hand can scale automatically based on demands.*

Availability
- *VM high availability is possible by setting up multiple VMs in different regions.  App Service on the other hand have options for deployment slots and regional redundancy.*

Workflow
- *VM provides full control over the environment, which is useful for applications requiring specific infrastructure configurations.  This requires more time to manage and maintain.  App Service on the otherhand simplies deployment and management with integrated CI/CD pipelines.  This allows developers to focus more on the code rather than the infrastructure*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 


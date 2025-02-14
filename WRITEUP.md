# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Costs
- A VM can be more expensive as there is a need to manage the infrastructure.  App Service on the other hand can be more cost-effective for smaller applications as it doesn't need to manage the infrastructure anumre.  Pricing is based on the chosen tier.

Scalability
- VM is scalable but manual and requires configuring additonal VMs.  App Service on the other hand can scale automatically based on demands.

Availability
- VM high availability is possible by setting up multiple VMs in different regions.  App Service on the other hand have options for deployment slots and regional redundancy.

Workflow
- VM provides full control over the environment, which is useful for applications requiring specific infrastructure configurations.  This requires more time to manage and maintain.  App Service on the otherhand simplies deployment and management with integrated CI/CD pipelines.  This allows developers to focus more on the code rather than the infrastructure.

Based on the points above, I chose App Service to deploy the CMS app.  This allowed me to focus more on the functionality of my app and not worry about the underlying infrastructure.  This also allowed me to deploy my app faster through the CI/CD pipeline.  App Service is also more cost-effective given that I have a small application only.

### Assess app changes that would change your decision.

If the CMS app grows to having more resource-intensive tasks, or if the app will require specific software and OS version not supported by App Service, then switching to VM is needed.  VM is more suitable for this as resources and other infrastructure components can be configured.



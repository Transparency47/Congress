# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3980?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3980
- Title: Federal Loan Systems Modernization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3980
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-03-23T14:34:12Z
- Update date including text: 2026-03-23T14:34:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3980",
    "number": "3980",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Federal Loan Systems Modernization Act of 2026",
    "type": "S",
    "updateDate": "2026-03-23T14:34:12Z",
    "updateDateIncludingText": "2026-03-23T14:34:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-03-04T16:23:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NH"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3980is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3980\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mrs. Blackburn (for herself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo authorize the creation of Lending.gov as a shared services platform to provide a single source of access to loans provided by Federal agencies, and modern technology to support effective management of Federal credit programs, in order to reduce costs, prevent fraud, increase the speed of origination, improve transparency, improve access and customer experience, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Loan Systems Modernization Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator; Administration**\nThe terms Administrator and Administration mean the Administrator of General Services and the General Services Administration, respectively.\n**(2) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(3) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(B)**\nthe Committee on Oversight and Government Reform of the House of Representatives.\n**(4) Customer agency**\nThe term customer agency means an agency participating in the Platform.\n**(5) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(6) Federal loan program**\nThe term Federal loan program means any direct or guaranteed Federal loan or credit program administered by an agency.\n**(7) Loan management**\nThe term loan management means a collection of credit program loan and loan guarantee administrative activities, such as application intake and process, underwriting, servicing, close-out, information exchange, document creation, reporting, and fraud detection, that\u2014\n**(A)**\nare executed at the various phases of the Federal lending process;\n**(B)**\nare core to effective program delivery, financial management, and customer experience;\n**(C)**\nare subject to modernization; and\n**(D)**\ndo not entail any change of authority of the agency overseeing the function of a Federal loan program.\n**(8) Loan management technology**\nThe term loan management technology means commercial use software adapted to meet Federal loan program requirements to streamline the execution of administrative activities relating to Federal loan management.\n**(9) Platform**\nThe term Platform means a centralized shared services lending platform established under section 4(a), which includes an electronic portal for Federal direct lending applications, which shall be known as Lending.gov .\n**(10) Provider**\nThe term Provider means a shared service provider of the Platform.\n#### 3. Purpose\nThe purposes of this Act are to\u2014\n**(1)**\naddress the inefficiencies caused by using outdated and fragmented technology to manage multiple Federal lending processes and Federal lending programs across agencies and mitigate consumer difficulties accessing Federal loan programs by incorporating commercially available technology to improve program effectiveness across all agencies through a dedicated loan application platform;\n**(2)**\nauthorize the creation of a centralized loan platform, to be known as Lending.gov , utilizing industry-standard, commercially available loan processing software to streamline access to, and the administrative activities of, Federal loan programs in accordance with section 3307 of title 41, United States Code;\n**(3)**\nestablish Government-wide requirements for loan management, which will serve as the guiding criteria in the selection of commercially available technology to manage the Platform; and\n**(4)**\nprovide agencies with the responsibility and authority for establishing and maintaining oversight of the Platform.\n#### 4. Establishment of the Lending.gov platform\nNot later than 6 months after the date of enactment of this Act, the Administrator shall submit to the Director and the appropriate congressional committees a plan to establish the Platform utilizing commercially available loan management technology, which shall include\u2014\n**(1)**\ndesignation of a lead agency as the initial Provider and operational host of the Platform;\n**(2)**\na review of Federal loan programs subject to integration into the Platform, in coordination with the Federal Credit Policy Council, including the agency that is the designated authority for each such Federal loan program;\n**(3)**\ncommon deficiencies and areas of wasteful spending resulting from the use of outdated systems, including the findings of reports from various inspectors general of agencies and reports from the Government Accountability Office, among agencies that can be addressed through the creation of the Platform utilizing modern loan management technology;\n**(4)**\nthe proposed operational framework of the Platform;\n**(5)**\na plan to integrate commercial loan management technology to assist with standing-up and operating the Platform at the best value to the Federal Government, in accordance with section 3307 of title 41, United States Code;\n**(6)**\na timeline for implementation of the Platform; and\n**(7)**\nan estimate of the costs of implementing the Platform.\n#### 5. Operations of the Lending.gov platform\n##### (a) Responsibilities of the Provider\nThe Provider shall\u2014\n**(1)**\noperate, maintain, and continuously improve the Platform, including all associated systems, tools, infrastructure, and customer-facing services necessary to support Federal loan programs;\n**(2)**\nprovide onboarding, technical assistance, and ongoing operational support to agencies migrating to, or utilizing, the Platform;\n**(3)**\nprovide participating agencies loan servicing and portfolio management solutions encompassing both financial and non-financial elements necessary to support service levels, cost benchmarking, program oversight, risk management, and customer experience metrics for both agencies and borrowers;\n**(4)**\nensure that the Platform complies with all applicable Federal requirements relating to cybersecurity, privacy, information security, data governance, cloud authorization, financial management, and credit program management;\n**(5)**\nintegrate commercially available loan management technology appropriate for the efficient operation of Federal loan programs, including tools for application intake, underwriting, servicing, reporting, fraud detection, and customer-experience management;\n**(6)**\nenter into interagency agreements, service-level agreements, or other arrangements necessary to provide shared services to customer agencies and to recover costs as appropriate;\n**(7)**\ninclude auditable financial management and subledger capabilities in the Platform that support agency oversight, reconciliation, and documentation of borrower remediation;\n**(8)**\nensure that customer agencies retain ownership and full access to all program data generated or maintained through the Platform; and\n**(9)**\nensure the portability of customer agency data, including the ability to export all records in standardized, non-proprietary formats.\n##### (b) Program manager satisfaction\n**(1) Primary performance standard**\nProgram manager satisfaction at customer agencies shall be a primary performance standard governing the operation of the Platform.\n**(2) Annual survey**\nThe Provider shall, not less frequently than annually, conduct a standardized survey of relevant program managers and staff at each customer agency to assess satisfaction with the performance, functionality, service quality, and reliability of the Platform.\n**(3) Publication of results**\nThe Provider shall\u2014\n**(A)**\ntransmit survey results to the Administrator and the Director;\n**(B)**\nprovide such results to each customer agency; and\n**(C)**\nmake survey results publicly available in a manner consistent with applicable law and protection of sensitive information.\n**(4) Remediation plans**\nIf survey results indicate that satisfaction for any customer agency or functional area falls below thresholds established jointly by the Provider and the Administrator, the Provider shall\u2014\n**(A)**\ndevelop a remediation plan to address identified deficiencies;\n**(B)**\nsubmit the plan described in subparagraph (A) to the customer agency and Administrator not later than 60 days after survey results are finalized;\n**(C)**\nimplement the plan described in subparagraph (A) promptly; and\n**(D)**\nreport quarterly to the customer agency and Administrator on progress in resolving deficiencies until satisfaction thresholds are met.\n**(5) Consultation requirement**\nIn developing remediation plans under paragraph (4), the Provider shall consult directly with the program managers and senior officials of the affected customer agency.\n##### (c) Customer agency access\nEmployees of the Provider shall be provided with appropriate badges and system access by customer agencies to facilitate seamless service provision and communications with employees of the customer agency.\n##### (d) Performance dashboards and reporting\nThe Provider shall establish, maintain, and make available to the Administrator, the Director, and customer agencies performance dashboards and regular reports on Platform availability, processing times, service levels, system performance, and other operational metrics, including metrics derived from subsection (b).\n##### (e) Coordination and oversight\nThe Provider shall carry out its responsibilities under this section in coordination with the Administrator and the Director and subject to oversight under section 7.\n#### 6. Migration to Platform\n##### (a) In general\nNot later than 2 years after the date on which the Administrator submits the report required under section 4, the Director, in consultation with the Administrator and the Provider and in collaboration with the heads of relevant agencies, shall commence migration of other agency loan management systems to the Platform, as outlined in the report.\n##### (b) Deadline\nNot later than 3 years after the date of enactment of this Act, each agency that administers a Federal loan program shall complete migration of its loan management systems to the Platform established under section 4, unless granted an exception by the Director under subsection (c)(2).\n##### (c) Migration criteria and exceptions\n**(1) Criteria for migration**\nThe Director shall, in consultation with the Administrator, establish and publish criteria for determining which agencies shall migrate their loan management systems to the Platform, which shall include loan programs\u2014\n**(A)**\nthat originate or service more than 50 loans annually; or\n**(B)**\nwith loan amounts of more than $10,000,000 in the aggregate.\n**(2) Exceptions**\n**(A) In general**\nThe Director may grant an exception to the migration requirement under this section if the Director\u2014\n**(i)**\ndetermines that migration would be impracticable or contrary to the interest of program efficiency; and\n**(ii)**\nnotifies the appropriate congressional committees not later than 30 days after making that determination.\n**(B) Duration**\nThe Director may grant an exception under subparagraph (A) for a period of no longer than 3 years.\n**(C) Notification**\nThe Director shall notify the Administrator of any exception granted under this paragraph not later than 15 days after making such determination.\n**(D) Plan**\nAny agency that is granted an exception under subparagraph (A) shall, not later than 2 years of being granted an exception, develop a plan for migration after the initial exception period under subparagraph (B).\n#### 7. Oversight of migration and management\n##### (a) In general\nThe Administrator shall provide oversight of the migration to, and management of, the Platform established under this Act, including\u2014\n**(1)**\nreviewing the adequacy of the operational framework of the Administration for the Platform, in consultation with the Federal Credit Policy Council;\n**(2)**\nestablishing Government-wide standards for loan management, in coordination with the Director and the Federal Credit Policy Council, that shall apply to the Provider and all Federal credit programs, and that shall facilitate migration to the Platform and efficient operations of loan management activities;\n**(3)**\nproviding a recommendation to the Director on each exception granted under section 6(c), including an analysis of the impact of such an exception on the long-term Government-wide cost effectiveness of loan management and the financial sustainability of the Platform;\n**(4)**\nmonitoring agency compliance with migration requirements under section; and\n**(5)**\nsubmitting to the appropriate congressional committees an annual report on the status of agency migrations, any exceptions granted by the Director under section 6(c)(2), the service levels provided to customer agencies of the Platform, any recommended investments or policy changes required to improve the functionality of the Platform, and an analysis of the long-term government-wide cost effectiveness of loan management.\n##### (b) Authority To establish a marketplace\n**(1) In general**\nAfter establishment of the initial Platform, the Administrator shall make an assessment to determine if further adoption, service level improvements, and cost efficiencies would be achieved through the designation of additional Providers to create a shared services marketplace, and if so, make such a recommendation to the Director.\n**(2) Additional designations**\n**(A) In general**\nBased on the recommendation made under paragraph (1), the Director may designate up to 3 additional agencies as shared service providers to assume and fulfill the authorities and responsibilities outlined for the Provider in section 5.\n**(B) Requirements**\nAny additional designated shared service providers under subparagraph (A)\u2014\n**(i)**\nshall utilize the public facing capabilities established and managed by the initial Provider and operational host of the Platform designated under section 4(a) to promote a consistent experience for loan applicants through the Platform and reduce fragmentation across systems; and\n**(ii)**\nmay otherwise manage separate loan management support functions, with the approval of the Administrator.\n#### 8. Financing operations\n##### (a) In general\nCustomer agencies shall reimburse the Provider for services through interagency agreements, service-level agreements, or other arrangements necessary to provide shared services through the Platform to participating customer agencies and to recover costs as appropriate.\n##### (b) Remittance fee\n**(1) In general**\nTo provide for ongoing operations and maintenance efforts to maintain the functioning standards of the Platform, the Provider may collect a remittance fee that shall be applied with respect to each Federal loan serviced through the Platform.\n**(2) Amount**\nThe amount of the remittance fee collected under paragraph (1) shall be determined by the Provider in consultation with the Administrator, but shall be not more than 0.25 percent of the face value of the Federal loan serviced, unless otherwise authorized by law or guidance issued by the Director.\n**(3) Limit for direct loans to individuals**\nA remittance fee under paragraph (1) shall not be assessed with respect to any direct loan made to an individual borrower unless the head of the agency administering the applicable Federal loan program submit to the Director a certification that\u2014\n**(A)**\nprovides that the assessment of the fee will not materially impair borrower affordability, program access, or the statutory objectives of the Federal loan program;\n**(B)**\nincludes an analysis of borrower impact; and\n**(C)**\nshall be made available to the Administrator and on the Platform.\n##### (c) Fund\nAll remittance fees collected under this section shall be held in a dedicated fund and shall be used exclusively for the operations of, and maintenance activities related to, the Platform, which funds\u2014\n**(1)**\nmay be transferred by the Provider to customer agencies, with the approval of the Administrator, to support necessary migration, operations, and maintenance activities; and\n**(2)**\nshall remain available until expended.",
      "versionDate": "",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-04",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "7789",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Loan Systems Modernization Act of 2026",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-23T14:09:19Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3980is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Federal Loan Systems Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Loan Systems Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the creation of a \"Lending.gov\" as a shared services platform to provide a single source of access to loans provided by Federal agencies, and modern technology to support effective management of Federal credit programs, in order to reduce costs, prevent fraud, increase the speed of origination, improve transparency, improve access and customer experience, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:24Z"
    }
  ]
}
```

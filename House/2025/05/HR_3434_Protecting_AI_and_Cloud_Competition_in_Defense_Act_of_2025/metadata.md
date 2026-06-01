# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3434?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3434
- Title: Protecting AI and Cloud Competition in Defense Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3434
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-12-05T22:08:27Z
- Update date including text: 2025-12-05T22:08:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3434",
    "number": "3434",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protecting AI and Cloud Competition in Defense Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:27Z",
    "updateDateIncludingText": "2025-12-05T22:08:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-05-15T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3434ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3434\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Fallon (for himself, Ms. Jacobs , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo provide for certain requirements relating to cloud, data infrastructure, and foundation model procurement.\n#### 1. Short title\nThis Act may be cited as the Protecting AI and Cloud Competition in Defense Act of 2025 .\n#### 2. Ensuring competition in artificial intelligence procurement\n##### (a) Definitions\nIn this section:\n**(1) Artificial intelligence; AI**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Cloud computing**\nThe term cloud computing has the meaning given the term in Special Publication 800\u2013145 of the National Institute of Standards and Technology, or any successor document.\n**(3) Cloud provider**\nThe term cloud provider means any company engaged in the provision, sale, or licensing of cloud computing to customers, including individuals and businesses.\n**(4) Congressional defense committees**\nThe term congressional defense committees has the meaning given the term in section 101(a) of title 10, United States Code.\n**(5) Covered provider**\nThe term covered provider means any cloud provider, data infrastructure provider, or foundation model provider that has entered into contracts with the Department of Defense totaling at least $50,000,000 in any of the 5 previous fiscal years.\n**(6) Data infrastructure**\nThe term data infrastructure means the underlying computer, network, and software systems that enable the collection, storage, processing, and analysis of data, including the ability to record, transmit, transform, categorize, integrate, and otherwise process data generated by digital data systems.\n**(7) Data infrastructure provider**\nThe term data infrastructure provider means any company engaged in the provision, sale, or licensing of data infrastructure to customers, including individuals and businesses.\n**(8) Foundation model**\nThe term foundation model means an artificial intelligence model that\u2014\n**(A)**\n**(i)**\ngenerally uses self-supervision;\n**(ii)**\ncontains at least 1,000,000,000 parameters; and\n**(iii)**\nis applicable across a wide range of contexts; or\n**(B)**\nexhibits, or could be easily modified to exhibit, high levels of performance at tasks that pose a serious risk to security, national economic security, national public health, or safety.\n**(9) Foundation model provider**\nThe term foundation model provider means any company engaged in the provision, sale, or licensing of foundation models to customers, including individuals and businesses.\n**(10) Multi-cloud technology**\nThe term multi-cloud technology means architecture and services that allow for data, application, and program portability, usability, and interoperability between infrastructure, platforms, and hosted applications of multiple cloud providers and between public, private, and edge cloud environments in a manner that securely delivers operational and management consistency, comprehensive visibility, and resiliency.\n##### (b) Cloud, data infrastructure, and foundation model procurement requirements\nThe Secretary of Defense shall, in contracting provisions with cloud providers, foundation model providers, and data infrastructure providers\u2014\n**(1)**\npromote security, resiliency, and competition in the procurement of such solutions by requiring a competitive award process for each procurement of cloud computing, data infrastructure, or foundation model solutions;\n**(2)**\nensure that the Government maintains exclusive rights to access and use of all Government data; and\n**(3)**\nensure that the competitive process\u2014\n**(A)**\nprioritizes the appropriate role for the Government with respect to intellectual property and data rights and security, interoperability, and auditability requirements;\n**(B)**\nincludes modular open systems approaches and appropriate work allocation and technical boundaries;\n**(C)**\nmitigates barriers to entry faced by small businesses and nontraditional contractors; and\n**(D)**\nprioritizes multi-cloud technology unless doing so is infeasible or presents a substantial danger to national security.\n##### (c) Data training and use protection\nThe Secretary of Defense shall direct the Chief Digital and Artificial Intelligence Office to update or promulgate provisions of the Defense Federal Acquisition Regulation Supplement (DFARS) to ensure that\u2014\n**(1)**\nGovernment-furnished data, provided for purposes of development and operation of AI products and services to the Department of Defense, is not disclosed or used without proper authorization by the Department of Defense, including that such data cannot be used to train or improve the functionality of commercial products offered by a covered provider without express authorization by the Department of Defense;\n**(2)**\nGovernment-furnished data stored on vendor systems, provided for purposes of development and operation of AI products and services to the Department of Defense, is appropriately protected from other data on such systems, and is treated in accordance with Department of Defense data decrees and Creating Data Advantage (Open DAGIR) principles;\n**(3)**\nviolation of these provisions shall be subject to specific penalties, including fines and contract termination; and\n**(4)**\ncomponent acquisition executives may issue exemptions upon\u2014\n**(A)**\ndetermining that issuing an exemption is necessary for national security; and\n**(B)**\nnotifying the Chief Digital and Artificial Intelligence Officer of the specific provisions exempted, the vendor and program being issued the exemption, and the justification for the exemption.\n##### (d) Reporting\n**(1) In general**\nNot later than January 15, 2027, and annually thereafter for four years, the Chairman of the Joint Chiefs of Staff, in coordination with the Under Secretary of Defense for Acquisition and Sustainment, shall submit to the congressional defense committees a report assessing the competition, innovation, barriers to entry, and concentrations of market power or market share in the AI space for each period covered by the report. The report shall also include a list of the exemptions granted under subsection (c)(4)(A), including the date and purpose of the exemption. The report shall also include recommendations of appropriate legislative and administrative action.\n**(2) Publication**\nThe Secretary of Defense, acting through the Assistant to the Secretary of Defense for Public Affairs, shall ensure that the report is made available to the public by\u2014\n**(A)**\nposting a publicly releasable version of the report on a website of the Department of Defense; and\n**(B)**\nupon request, transmitting the report by other means, as long as such transmission is at no cost to the Department.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-15",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "1775",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting AI and Cloud Competition in Defense Act of 2025",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-20T12:26:35Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3434ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protecting AI and Cloud Competition in Defense Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting AI and Cloud Competition in Defense Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for certain requirements relating to cloud, data infrastructure, and foundation model procurement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:24Z"
    }
  ]
}
```

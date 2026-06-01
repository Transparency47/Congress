# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5259
- Title: Permanent OPTN Fee Authority Act
- Congress: 119
- Bill type: HR
- Bill number: 5259
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-02-05T17:34:39Z
- Update date including text: 2026-02-05T17:34:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5259",
    "number": "5259",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Permanent OPTN Fee Authority Act",
    "type": "HR",
    "updateDate": "2026-02-05T17:34:39Z",
    "updateDateIncludingText": "2026-02-05T17:34:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5259ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5259\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Costa (for himself and Ms. Van Duyne ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services to collect registration fees from members of the Organ Procurement and Transplantation Network, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Permanent OPTN Fee Authority Act .\n#### 2. Organ Procurement and Transplantation Network\nSection 372 of the Public Health Service Act ( 42 U.S.C. 274 ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nby moving the margins of subparagraphs (M) through (O) 2 ems to the left;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by striking , and and inserting ; and ; and\n**(ii)**\nin clause (ii), by striking the comma at the end and inserting a semicolon;\n**(C)**\nin subparagraph (C), by striking twenty-four-hour telephone service and inserting 24-hour telephone or information technology service ;\n**(D)**\nin each of subparagraphs (B) through (M), by striking the comma at the end and inserting a semicolon;\n**(E)**\nin subparagraph (N), by striking transportation, and and inserting transportation; ;\n**(F)**\nin subparagraph (O), by striking the period and inserting ; and ; and\n**(G)**\nby adding at the end the following:\n(P) consider establishing a dashboard to display the number of transplants performed, the types of transplants performed, the number and types of organs that entered the Organ Procurement and Transplantation Network system and failed to be transplanted, and other appropriate statistics, which should be updated more frequently than annually. ; and\n**(2)**\nby adding at the end the following:\n(d) Registration fees (1) In general The Secretary may collect registration fees from any member of the Organ Procurement and Transplantation Network for each transplant candidate such member places on the list described in subsection (b)(2)(A)(i). Such registration fees shall be collected and distributed only to support the operation of the Organ Procurement and Transplantation Network. Such registration fees are authorized to remain available until expended. (2) Collection The Secretary may collect the registration fees under paragraph (1) directly or through awards made under subsection (b)(1)(A). (3) Distribution Any amounts collected under this subsection shall\u2014 (A) be credited to the currently applicable appropriation, account, or fund of the Department of Health and Human Services as discretionary offsetting collections; and (B) be available, only to the extent and in the amounts provided in advance in appropriations Acts, to distribute such fees among awardees described in subsection (b)(1)(A). (4) Transparency The Secretary shall\u2014 (A) promptly post on the website of the Organ Procurement and Transplantation Network\u2014 (i) the amount of registration fees collected under this subsection from each member of the Organ Procurement and Transplantation Network; and (ii) a list of activities such fees are used to support; and (B) update the information posted pursuant to subparagraph (A), as applicable for each calendar quarter for which fees are collected under paragraph (1). (5) GAO review Not later than 2 years after the date of enactment of this subsection, the Comptroller General of the United States shall, to the extent data are available\u2014 (A) conduct a review concerning the activities under this subsection; and (B) submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Finance of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report on such review, including related recommendations, as applicable. .",
      "versionDate": "2025-09-10",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-02",
        "text": "Received in the Senate."
      },
      "number": "1262",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mikaela Naylon Give Kids a Chance Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "532",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "OPTN Fee Collection Authority Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2751",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Permanent OPTN Fee Authority Act",
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
        "name": "Health",
        "updateDate": "2025-09-23T16:49:58Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5259ih.xml"
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
      "title": "Permanent OPTN Fee Authority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Permanent OPTN Fee Authority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services to collect registration fees from members of the Organ Procurement and Transplantation Network, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:27Z"
    }
  ]
}
```

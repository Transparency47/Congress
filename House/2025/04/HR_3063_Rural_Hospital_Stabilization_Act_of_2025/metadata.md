# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3063?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3063
- Title: Rural Hospital Stabilization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3063
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-12-03T23:26:15Z
- Update date including text: 2025-12-03T23:26:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3063",
    "number": "3063",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000481",
        "district": "2",
        "firstName": "Shomari",
        "fullName": "Rep. Figures, Shomari [D-AL-2]",
        "lastName": "Figures",
        "party": "D",
        "state": "AL"
      }
    ],
    "title": "Rural Hospital Stabilization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-03T23:26:15Z",
    "updateDateIncludingText": "2025-12-03T23:26:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:01:10Z",
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
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "AL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "GA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "AL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "AL"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "AL"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AL"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "MS"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "NE"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "GU"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "IL"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3063ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3063\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mr. Figures (for himself, Mr. Jack , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services to make grants to assist rural hospitals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Hospital Stabilization Act of 2025 .\n#### 2. Grants to assist rural hospitals\nThe Public Health Service Act ( 42 U.S.C. 201 et seq. ) is amended by inserting after section 330A\u20132 ( 42 U.S.C. 254c\u20131b ) the following:\n330A\u20133. Grants to assist rural hospitals (a) Authority To make grants The Secretary, acting through the Director of the Office of Rural Health Policy of the Health Resources and Services Administration, may make grants under this section to rural hospitals\u2014 (1) for projects to acquire, repair, and upgrade the systems, facilities, and equipment of rural hospitals; and (2) to provide financial assistance to be used toward the operational costs of rural hospitals, including payroll expenses (except payroll expenses associated with hospital leadership positions) and debt payments. (b) Applications To be eligible to receive a grant under this section, a rural hospital shall submit to the Secretary an application, at such time, in such manner, and containing such information as the Secretary may require, including\u2014 (1) a description of the projects and expenses that will receive funding under the grant; (2) a description of the manner in which the projects and expenses funded under the grant will address the financial needs of the hospital; (3) a description of how the projects and expenses funded under the grant will help ensure that residents of rural areas maintain access to hospital services; (4) a plan for sustaining projects and covering expenses at the hospital after Federal support under this section has ended; and (5) such other information as the Secretary determines to be appropriate. (c) Maximum aggregate grant amount A rural hospital may receive not more that $5,000,000, in the aggregate, in grant funds under this section for any five-year period. (d) Maintenance of effort Funds made available under this section shall be used to supplement and not supplant other Federal, State, local, and Tribal funds available for the grant purposes described in subsection (a). (e) Report to Congress Not later than 18 months after the date of the enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives, the Committee on Agriculture of the House of Representatives, the Committee on Health, Education, Labor, and Pensions of the Senate, and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report on the activities and outcomes of the grant program carried out under this section, including the impact of projects funded under this section on improving the financial viability of the grant recipients and ensuring that residents of rural areas maintain access to hospital services. (f) Definitions In this section: (1) Rural hospital The term rural hospital means a hospital that is located at least 15 miles from the nearest hospital and at least 20 miles from the nearest urbanized area (as defined by the Bureau of the Census). Such term includes public and private hospitals. (2) Hospital leadership position The term hospital leadership position has such meaning as the Secretary may prescribe by regulation. (g) Authorization of appropriations There is authorized to be appropriated to carry out this section $500,000,000, in the aggregate, for fiscal years beginning after September 30, 2025. .",
      "versionDate": "2025-04-29",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-21T10:36:14Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3063ih.xml"
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
      "title": "Rural Hospital Stabilization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:32:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Hospital Stabilization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services to make grants to assist rural hospitals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:47Z"
    }
  ]
}
```

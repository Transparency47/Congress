# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4977?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4977
- Title: Connected MOM Act
- Congress: 119
- Bill type: HR
- Bill number: 4977
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-04-07T08:05:24Z
- Update date including text: 2026-04-07T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4977",
    "number": "4977",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000462",
        "district": "22",
        "firstName": "Lois",
        "fullName": "Rep. Frankel, Lois [D-FL-22]",
        "lastName": "Frankel",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Connected MOM Act",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:24Z",
    "updateDateIncludingText": "2026-04-07T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
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
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:01:45Z",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "LA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "WA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "DE"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4977ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4977\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Ms. Lois Frankel of Florida (for herself, Ms. Salazar , Ms. Castor of Florida , and Ms. Letlow ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo identify and address barriers to coverage of remote physiologic devices under State Medicaid programs to improve maternal and child health outcomes for pregnant and postpartum women.\n#### 1. Short title\nThis Act may be cited as the Connected Maternal Online Monitoring Act or the Connected MOM Act .\n#### 2. Coverage of remote physiologic monitoring devices and impact on maternal and child health outcomes under Medicaid\n##### (a) Report to Congress\nNot later than 18 months after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to Congress a report containing information on authorities and State practices for covering remote physiological monitoring devices, including limitations and barriers to such coverage and the impact on maternal health outcomes, and to the extent appropriate, recommendations on how to address such limitations or barriers related to coverage of remote physiologic devices under State Medicaid programs, including, but not limited to, pulse oximeters, blood pressure cuffs, scales, and blood glucose monitors, with the goal of improving maternal and child health outcomes for pregnant and postpartum women enrolled in State Medicaid programs.\n##### (b) State resources\nNot later than 6 months after the submission of the report required by subsection (a), the Secretary shall update resources for State Medicaid programs, such as State Medicaid telehealth toolkits, to be consistent with the recommendations provided in such report.",
      "versionDate": "2025-08-15",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "141",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Connected MOM Act",
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
        "updateDate": "2025-09-19T15:38:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-15",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4977",
          "measure-number": "4977",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-15",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4977v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-08-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Connected Maternal Online Monitoring Act or the Connected MOM Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to report, and provide resources for states, on coverage of remote physiologic devices and related services (e.g., blood glucose monitors) under Medicaid, so as to improve maternal and child health outcomes for pregnant and postpartum women.</p>"
        },
        "title": "Connected MOM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4977.xml",
    "summary": {
      "actionDate": "2025-08-15",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Connected Maternal Online Monitoring Act or the Connected MOM Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to report, and provide resources for states, on coverage of remote physiologic devices and related services (e.g., blood glucose monitors) under Medicaid, so as to improve maternal and child health outcomes for pregnant and postpartum women.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4977"
    },
    "title": "Connected MOM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-15",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Connected Maternal Online Monitoring Act or the Connected MOM Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to report, and provide resources for states, on coverage of remote physiologic devices and related services (e.g., blood glucose monitors) under Medicaid, so as to improve maternal and child health outcomes for pregnant and postpartum women.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4977"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4977ih.xml"
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
      "title": "Connected MOM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T05:28:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Connected MOM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T05:28:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Connected Maternal Online Monitoring Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T05:28:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To identify and address barriers to coverage of remote physiologic devices under State Medicaid programs to improve maternal and child health outcomes for pregnant and postpartum women.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T05:11:16Z"
    }
  ]
}
```

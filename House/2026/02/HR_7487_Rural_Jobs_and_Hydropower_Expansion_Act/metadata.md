# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7487
- Title: Rural Jobs and Hydropower Expansion Act
- Congress: 119
- Bill type: HR
- Bill number: 7487
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-05-15T08:07:41Z
- Update date including text: 2026-05-15T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 21 - 14.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 21 - 14.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7487",
    "number": "7487",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "B000825",
        "district": "4",
        "firstName": "Lauren",
        "fullName": "Rep. Boebert, Lauren [R-CO-4]",
        "lastName": "Boebert",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Rural Jobs and Hydropower Expansion Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:41Z",
    "updateDateIncludingText": "2026-05-15T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 21 - 14.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
        "item": [
          {
            "date": "2026-05-14T14:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-11T16:04:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7487ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7487\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Ms. Boebert (for herself and Mr. Gray ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Reclamation Project Act of 1939 to encourage non-Federal hydropower development with respect to Bureau of Reclamation projects.\n#### 1. Short title\nThis Act may be cited as the Rural Jobs and Hydropower Expansion Act .\n#### 2. Amendments to Reclamation Project Act\nSection 9(c) of the Reclamation Project Act of 1939 (53 Stat. 1194) is amended\u2014\n**(1)**\nby striking (1) The Secretary is authorized and inserting The Secretary is authorized ;\n**(2)**\nby striking small conduit hydropower using Bureau of Reclamation facilities and pumped storage hydropower exclusively using Bureau of Reclamation reservoirs and inserting hydropower using all Bureau of Reclamation facilities ;\n**(3)**\nby striking No contract relating to municipal water supply and inserting the following:\n(1) No contract relating to municipal water supply ;\n**(4)**\nin paragraph (2)(A)\u2014\n**(A)**\nby striking applicable transferred conduit and inserting applicable transferred works facility ;\n**(B)**\nby striking applicable reserved conduit and inserting applicable reserved works facility ; and\n**(C)**\nby striking power privilege offer for a small conduit and inserting power privilege offer for the ;\n**(5)**\nin paragraph (3), by striking small conduit and inserting applicable ;\n**(6)**\nin paragraph (4), by striking small conduit hydropower ;\n**(7)**\nin paragraph (6)\u2014\n**(A)**\nby striking conduit before hydropower generation ; and\n**(B)**\nby striking transferred conduit and inserting transferred works facility ;\n**(8)**\nin paragraph (7), by striking conduit ;\n**(9)**\nin paragraph (8)\u2014\n**(A)**\nby inserting (referred to in this section as an authorization ) before issued by the Federal Energy Regulatory Commission ;\n**(B)**\nby striking August 9, 2013, and inserting the date of the enactment of the Rural Jobs and Hydropower Expansion Act ; and\n**(C)**\nby adding at the end Any authorization issued by the Federal Energy Regulatory Commission with respect to a project shall remain in place until such authorization becomes inactive. As allowed by the Federal Energy Regulatory Commission, an authorization may be renewed and remain active. Once the authorization becomes inactive, project site jurisdiction shall shift to the Bureau of Reclamation exclusively. ;\n**(10)**\nby redesignating paragraph (9) as paragraph (10);\n**(11)**\nby inserting after paragraph (8) the following:\n(9) Nothing in this section shall expand or otherwise amend the Bureau of Reclamation lease of power privilege authorities outside the project boundary. ; and\n**(12)**\nin paragraph (10), as so redesignated\u2014\n**(A)**\nby striking subparagraphs (A), (C), (D), and (E);\n**(B)**\nby redesignating subparagraph (B) as subparagraph (A); and\n**(C)**\nby adding at the end the following:\n(B) Reserved works facility The term reserved works facility means those facilities owned by the Bureau of Reclamation where the Bureau of Reclamation has retained responsibility for carrying out operation and maintenance activities. (C) Transferred works facility The term transferred works facility means a project facility where the operations and maintenance of that facility is carried out by a non-Federal entity under the provisions of a formal operations and maintenance transfer contract. .",
      "versionDate": "2026-02-11",
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
        "name": "Water Resources Development",
        "updateDate": "2026-02-20T19:41:45Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7487ih.xml"
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
      "title": "Rural Jobs and Hydropower Expansion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Jobs and Hydropower Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Reclamation Project Act of 1939 to encourage non-Federal hydropower development with respect to Bureau of Reclamation projects.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:36Z"
    }
  ]
}
```

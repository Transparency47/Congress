# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8285?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8285
- Title: Protecting American Competition Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8285
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-26T17:50:28Z
- Update date including text: 2026-05-26T17:50:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8285",
    "number": "8285",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Protecting American Competition Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-26T17:50:28Z",
    "updateDateIncludingText": "2026-05-26T17:50:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
            "date": "2026-04-22T20:16:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:00:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "GA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8285ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8285\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Issa (for himself, Mr. Meeks , and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to require a competitive market review of applications for a license to export, reexport, or transfer in-country certain technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting American Competition Act of 2026 .\n#### 2. Initial license review\n##### (a) In general\nSection 1756 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4815 ) is amended by adding at the end the following:\n(f) Initial license review (1) In general In reviewing an application for a license or other authorization for the export, reexport, or in-country transfer of items controlled under this part, the Under Secretary for Industry and Security (Under Secretary) shall consider whether the requested license or other authorization, if issued, would be the initial license or other authorization for the export, reexport, or in-country transfer of such item to an ultimate consignee or end user. (2) Treatment of subsequent license applications After issuing an initial license or other authorization for the export, reexport, or in-country transfer of an item described in paragraph (1), the Under Secretary should attempt to administer in a timely manner any subsequent application by other applicants for a license or other authorization for the same or a similar item to the same ultimate consignee or end user as the initial license. (3) Report to Congress No later than one year after the date of the enactment of this subsection, and annually thereafter, the Under Secretary shall submit to the appropriate congressional committees a report that details\u2014 (A) the number of initial licenses granted, if any, in the previous calendar year for which there were other applications submitted to export, re-export, or in-country transfer the same or a similar item to the same ultimate consignee or end-user; (B) the details of the initial licenses granted, if any, for which there were other applications submitted for a license to export, re-export, or in-country transfer the same or a similar item to the same ultimate consignee or end-user, and the details and outcome of such other submitted applications; and (C) the reason for creating an initial license to export, re-export, or in-country transfer of the item or a similar item to the ultimate consignee or end-user when there were other applications for the submitted for a license to export, re-export, or in-country transfer a same or similar item to the same ultimate consignee or end-user. (4) Rule of construction Nothing in this Act shall be construed to require the Under Secretary to delay a licensing decision or administer a licensing decision that is contrary to the national security or foreign policy interests of the United States. (5) Definitions In this subsection: (A) Appropriate congressional committees The term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate. (B) Under Secretary The term Under Secretary means the Under Secretary for Industry and Security, acting in consultation with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, or their designees. .\n##### (b) Report\nNot later than 90 days after the date of the enactment of this Act, the Under Secretary for Industry and Security shall submit to Congress a report on how the Under Secretary is implementing subsection (f)(2) of section 1756 of the Export Control Reform Act of 2018, as added by subsection (a), including detailing any changes to licensing policy or licensing officer operating protocols implemented pursuant to implementation of such subsection.",
      "versionDate": "2026-04-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:36:10Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-01T18:36:03Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-05-01T18:35:57Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-01T18:36:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-20T23:16:17Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8285ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting American Competition Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "title": "Protecting American Competition Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Export Control Reform Act of 2018 to require a competitive market review of applications for a license to export, reexport, or transfer in-country certain technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T12:33:45Z"
    }
  ]
}
```

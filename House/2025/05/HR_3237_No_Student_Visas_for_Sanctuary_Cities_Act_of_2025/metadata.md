# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3237
- Title: No Student Visas for Sanctuary Cities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3237
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2026-05-22T08:07:37Z
- Update date including text: 2026-05-22T08:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3237",
    "number": "3237",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "No Student Visas for Sanctuary Cities Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:37Z",
    "updateDateIncludingText": "2026-05-22T08:07:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "AZ"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "IL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "SC"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "CO"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3237ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3237\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Ms. Hageman (for herself, Mr. Gill of Texas , Mr. Gosar , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide for a limitation on availability of student visas for institutions in sanctuary jurisdictions.\n#### 1. Short title\nThis Act may be cited as the No Student Visas for Sanctuary Cities Act of 2025 .\n#### 2. Limitation on availability of F-visas and M-visas for institutions in sanctuary jurisdictions\nSection 214(m) of the Immigration and Nationality Act ( 8 U.S.C. 1184(m) ) is amended by adding at the end the following:\n(3) (A) The Secretary of Homeland Security shall, for each fiscal year, identify sanctuary jurisdictions for purposes of this paragraph. (B) In the case of an alien who seeks a visa under or to be accorded status as a nonimmigrant under section 101(a)(15)(F) to pursue a course of study at an established college, university, conservatory, academic high school, elementary school, or other academic institution or in an accredited language training program in the United States, if such college, university, conservatory, academic high school, elementary school, or other academic institution or accredited language training program is located in a sanctuary jurisdiction, such visa may not be issued nor may such status be accorded. (C) In the case of an alien who seeks a visa under or to be accorded status as a nonimmigrant under section 101(a)(15)(M) to pursue a full course of study at an established vocational or other recognized nonacademic institution (other than in a language training program) in the United States, if such vocational or other recognized nonacademic institution is located in a sanctuary jurisdiction, such visa may not be issued nor may such status be accorded. (D) The prohibition under subparagraphs (B) and (C) do not apply for a fiscal year in the case of a State or unit of local government identified as a sanctuary jurisdiction if the Secretary of Homeland Security thereafter determines that such State or unit of local government is no longer a sanctuary jurisdiction and submits a report to Congress to that effect. (E) For purposes of this paragraph, the term sanctuary jurisdiction means any State or unit of local government that has laws, ordinances, regulations, resolutions, policies, or other practices that obstruct immigration enforcement and shield criminals from U.S. Immigration and Customs Enforcement, including by\u2014 (i) refusing to or prohibiting agencies from complying with U.S. Immigration and Customs Enforcement detainers; (ii) imposing unreasonable conditions on U.S. Immigration and Customs Enforcement detainer compliance; (iii) denying U.S. Immigration and Customs Enforcement access to interview incarcerated aliens; or (iv) otherwise impeding communication or information exchanges between the jurisdiction\u2019s personnel and Federal immigration officers. .",
      "versionDate": "2025-05-07",
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
        "name": "Immigration",
        "updateDate": "2025-05-22T12:33:24Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3237ih.xml"
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
      "title": "To amend the Immigration and Nationality Act to provide for a limitation on availability of student visas for institutions in sanctuary jurisdictions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:35Z"
    },
    {
      "title": "No Student Visas for Sanctuary Cities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Student Visas for Sanctuary Cities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:25Z"
    }
  ]
}
```

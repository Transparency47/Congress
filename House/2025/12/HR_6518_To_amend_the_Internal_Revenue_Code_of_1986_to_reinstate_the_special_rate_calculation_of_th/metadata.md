# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6518
- Title: SAF Act
- Congress: 119
- Bill type: HR
- Bill number: 6518
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-13T08:06:32Z
- Update date including text: 2026-05-13T08:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6518",
    "number": "6518",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000629",
        "district": "3",
        "firstName": "Sharice",
        "fullName": "Rep. Davids, Sharice [D-KS-3]",
        "lastName": "Davids",
        "party": "D",
        "state": "KS"
      }
    ],
    "title": "SAF Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:32Z",
    "updateDateIncludingText": "2026-05-13T08:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NE"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "LA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "KS"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "KS"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "OH"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PR"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6518ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6518\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Ms. Davids of Kansas (for herself, Mr. Flood , Mr. Carter of Louisiana , and Mr. Mann ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to reinstate the special rate calculation of the clean fuel production credit with respect to sustainable aviation fuel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing America\u2019s Fuels Act or the SAF Act .\n#### 2. Extension of clean fuel production credit; reinstatement of special rate calculation for sustainable aviation fuel\n##### (a) Reinstatement of special rate\n**(1) In general**\nParagraph (3) of section 45Z(a) of the Internal Revenue Code of 1986 is amended to read as follows:\n(3) Special rate for sustainable aviation fuel (A) In general In the case of a transportation fuel which is sustainable aviation fuel, paragraph (2) shall be applied\u2014 (i) in the case of fuel produced at a qualified facility described in paragraph (2)(A), by substituting 35 cents for 20 cents , and (ii) in the case of fuel produced at a qualified facility described in paragraph (2)(B), by substituting $1.75 for $1.00 . (B) Sustainable aviation fuel For purposes of subparagraph (A), the term sustainable aviation fuel means liquid fuel, the portion of which is not kerosene, which is sold for use in an aircraft and which\u2014 (i) meets the requirements of\u2014 (I) ASTM International Standard D7566, or (II) the Fischer Tropsch provisions of ASTM International Standard D1655, Annex A1, and (ii) is not derived from palm fatty acid distillates or petroleum. .\n**(2) Conforming amendment**\nSection 45Z(c)(1) of such Code, as amended by Public Law 119\u201321 , is amended by striking and the $1.00 amount in subsection (a)(2)(B) and inserting , the $1.00 amount in subsection (a)(2)(B), the 35 cent amount in subsection (a)(3)(A)(i), and the $1.75 amount in subsection (a)(3)(A)(ii) .\n##### (b) Extension of credit\nSection 45Z(g) of such Code, as amended by Public Law 119\u201321 , is amended by striking fuel sold after December 31, 2029 and inserting fuel sold after December 31, 2033 .\n##### (c) Effective date\nThe amendments made by this paragraph shall apply to fuel produced after December 31, 2025.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-02-02",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3759",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAF Act",
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
        "name": "Taxation",
        "updateDate": "2026-01-08T16:51:59Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6518ih.xml"
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
      "title": "SAF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing America\u2019s Fuels Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to reinstate the special rate calculation of the clean fuel production credit with respect to sustainable aviation fuel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:20Z"
    }
  ]
}
```

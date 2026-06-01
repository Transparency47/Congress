# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6896
- Title: Federal Facilities Protection and Oversight Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6896
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-02-03T09:05:47Z
- Update date including text: 2026-02-03T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6896",
    "number": "6896",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Federal Facilities Protection and Oversight Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:47Z",
    "updateDateIncludingText": "2026-02-03T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:10:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:45:35Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-18T14:09:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6896ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6896\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Stansbury (for herself and Mr. Morelle ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for certain requirements and oversight for demolition or substantial alteration of Federal buildings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Facilities Protection and Oversight Act of 2025 .\n#### 2. Oversight and approval for certain building demolition or substantial alteration\n##### (a) Approval of Congress for demolition\n**(1) In general**\nA public building located in the District of Columbia shall not be demolished, in whole or in part, or substantially altered without the express authority of Congress.\n**(2) Requirement**\nAs a requirement for a demolition subject to paragraph (1), the site to be demolished shall have an approved and finalized plan for construction.\n**(3) Definitions**\nIn this subsection:\n**(A) Public building**\nThe term public building means a building, whether for single or multitenant occupancy, and its grounds, approaches, and appurtenances, which is generally suitable for use as office or storage space or both by 1 or more Federal agencies or mixed-ownership Government corporations.\n**(B) Substantial alteration**\nThe term substantial alteration means any alteration to a building that\u2014\n**(i)**\naffects structural integrity;\n**(ii)**\nsignificantly changes historical character; or\n**(iii)**\nexceeds thresholds described in section 3307 of title 40, United States Code.\n##### (b) National Capital Planning Commission oversight\nSection 8722 of title 40, United States Code, is amended\u2014\n**(1)**\nin subsection (b) by inserting , substantial alterations, after proposed developments ;\n**(2)**\nin subsection (d), by inserting , architectural integrity, after the location ; and\n**(3)**\nby adding at the end the following:\n(f) Substantial alteration defined In this section, the term substantial alteration means any alteration to a building that\u2014 (1) affects structural integrity; (2) significantly changes historical character; or (3) exceeds thresholds described in section 3307. .\n#### 3. Severability\nIf any provision of this Act is held invalid, the remainder shall not be affected.",
      "versionDate": "2025-12-18",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-21T16:42:53Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6896ih.xml"
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
      "title": "Federal Facilities Protection and Oversight Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Facilities Protection and Oversight Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for certain requirements and oversight for demolition or substantial alteration of Federal buildings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:27Z"
    }
  ]
}
```

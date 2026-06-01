# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3167
- Title: Noncontiguous Energy Relief and Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3167
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-02-04T04:26:30Z
- Update date including text: 2026-02-04T04:26:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-01 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-01 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3167",
    "number": "3167",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Noncontiguous Energy Relief and Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:30Z",
    "updateDateIncludingText": "2026-02-04T04:26:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-01T20:59:34Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "HI"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3167ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3167\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Torres of New York (for himself, Mr. Case , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 46, United States Code, to allow for the transportation of energy products on vessels between points in the United States to which the coastwise laws apply if at least one such point is in Alaska, Hawaii, Guam, or the Commonwealth of Puerto Rico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Noncontiguous Energy Relief and Access Act of 2025 .\n#### 2. Energy products exemption\nSection 55102 of title 46, United States Code, is amended\u2014\n**(1)**\nin subsection (a) to read as follows:\n(a) Definitions In this subsection: (1) Covered noncontiguous trade The term covered noncontiguous trade means\u2014 (A) trade between\u2014 (i) one of the contiguous 48 States; and (ii) Alaska, Hawaii, Guam, or the Commonwealth of Puerto Rico; and (B) trade between\u2014 (i) a place in Alaska, Hawaii, Guam, or the Commonwealth of Puerto Rico; and (ii) another place in Alaska, Hawaii, Guam, or the Commonwealth of Puerto Rico. (2) Energy products The term energy products means any equipment, component of equipment, or energy source for the generation, storage, transmission, and distribution of electricity. (3) Energy source The term energy source means\u2014 (A) liquefied natural gas or any other energy source needed for the generation of electricity; and (B) a petroleum product. (4) Equipment The term equipment means power generators, storage units, wind turbines, solar panels, hydroelectric plants, and any other components needed for the generation, transmission, or distribution of electricity. (5) Merchandise The term merchandise includes\u2014 (A) merchandise owned by the United States Government, a State, or a subdivision of a State; and (B) valueless material. (6) Petroleum product The term petroleum product has the meaning given such term in section 3 of the Energy Policy and Conservation Act ( 42 U.S.C. 6202 ). ;\n**(2)**\nby redesignating subsection (c) as subsection (d); and\n**(3)**\nby inserting after subsection (b) the following:\n(c) Energy products exemption Subsection (b) shall not apply with respect to transportation of energy products in covered noncontiguous trade on a vessel. .",
      "versionDate": "2025-05-01",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-30T13:40:32Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3167ih.xml"
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
      "title": "Noncontiguous Energy Relief and Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Noncontiguous Energy Relief and Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 46, United States Code, to allow for the transportation of energy products on vessels between points in the United States to which the coastwise laws apply if at least one such point is in Alaska, Hawaii, Guam, or the Commonwealth of Puerto Rico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:22Z"
    }
  ]
}
```

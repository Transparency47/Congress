# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4813
- Title: Noncontiguous Disaster Shipping Act
- Congress: 119
- Bill type: HR
- Bill number: 4813
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-10-07T08:05:25Z
- Update date including text: 2025-10-07T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-30 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-07-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-30 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-07-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4813",
    "number": "4813",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Noncontiguous Disaster Shipping Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:25Z",
    "updateDateIncludingText": "2025-10-07T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
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
      "actionDate": "2025-07-30",
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
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-07-30T21:43:18Z",
                "name": "Referred to"
              }
            },
            "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
            "systemCode": "hspw13"
          },
          {
            "activities": {
              "item": {
                "date": "2025-07-30T21:43:18Z",
                "name": "Referred to"
              }
            },
            "name": "Coast Guard and Maritime Transportation Subcommittee",
            "systemCode": "hspw07"
          }
        ]
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
      "sponsorshipDate": "2025-07-29",
      "state": "HI"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "MP"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AS"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4813ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4813\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Moylan (for himself, Mr. Case , Ms. King-Hinds , Mrs. Radewagen , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 46, United States Code, to provide for a waiver of navigation or vessel-inspection laws in noncontiguous areas upon a declaration of a major disaster or emergency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Noncontiguous Disaster Shipping Act .\n#### 2. Waiver in a noncontiguous area\nSection 501 of title 46, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively; and\n**(2)**\nby inserting after subsection (b) the following new subsection:\n(c) In a Noncontiguous Area (1) In general Upon a declaration by the President pursuant to section 401 or 501 the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ; 5191) that a major disaster or emergency exists in a noncontiguous area of the United States, the head of an agency responsible for the administration of the navigation or vessel-inspection laws shall waive compliance with such laws for a vessel transporting cargo to or from the noncontiguous area affected by such major disaster or emergency for the purpose of disaster relief. (2) Duration of waiver (A) In general Subject to subparagraphs (B) and (C), a waiver issued under this subsection shall be for a period of not more than 10 days. (B) Waiver extension Upon the termination of a waiver issued under this subsection, the head of the agency referred to in paragraph (1), in consultation with the Governor of the noncontiguous area affected by such major disaster or emergency, may extend the waiver for an additional period of not more than 10 days. (C) Aggregate duration The aggregate duration of the period of all waivers and extensions of waivers under this subsection with respect to any one major disaster or emergency shall not exceed 45 days. (3) Notice to congress (A) In general The head of the agency referred to in paragraph (1) shall notify the Committee on Transportation and Infrastructure, the Committee on Armed Services of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Armed Services of the Senate of the issuance of any waiver of the navigation or vessel-inspection laws under this subsection not later than 48 hours after such issuance. (B) Notification required for extensions For the purposes of this paragraph, an extension issued under paragraph (2)(B) shall be treated in the same manner as a waiver issued under this subsection. (4) Noncontiguous area of the United States defined For the purposes of this subsection, the term noncontiguous area of the United States means Puerto Rico, the Virgin Islands, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, Hawaii, and Alaska. .",
      "versionDate": "2025-07-29",
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
        "name": "Emergency Management",
        "updateDate": "2025-09-16T22:33:40Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4813ih.xml"
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
      "title": "Noncontiguous Disaster Shipping Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Noncontiguous Disaster Shipping Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 46, United States Code, to provide for a waiver of navigation or vessel-inspection laws in noncontiguous areas upon a declaration of a major disaster or emergency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:36Z"
    }
  ]
}
```

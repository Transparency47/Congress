# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2280
- Title: A bill to transfer administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2280
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2026-05-27T15:07:09Z
- Update date including text: 2026-05-27T15:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2026-04-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2100; text: CR S2100)
- 2026-04-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-04-29 - Discharge: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2026-04-29 - Committee: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2026-05-01 - Floor: Message on Senate action sent to the House.
- 2026-05-04 10:32:43 - Floor: Received in the House.
- 2026-05-04 10:33:00 - Floor: Held at the desk.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2026-04-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2100; text: CR S2100)
- 2026-04-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-04-29 - Discharge: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2026-04-29 - Committee: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2026-05-01 - Floor: Message on Senate action sent to the House.
- 2026-05-04 10:32:43 - Floor: Received in the House.
- 2026-05-04 10:33:00 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2280",
    "number": "2280",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "J000312",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Justice, James C. [R-WV]",
        "lastName": "Justice",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "A bill to transfer administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-27T15:07:09Z",
    "updateDateIncludingText": "2026-05-27T15:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-04",
      "actionTime": "10:33:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-04",
      "actionTime": "10:32:43",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2100; text: CR S2100)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2026-04-29T19:33:56Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-15T19:13:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2280is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2280\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Justice (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo transfer administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia, and for other purposes.\n#### 1. Transfers of administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia\n##### (a) Transfers\n**(1) Transfer to the Commissioner of U.S. Customs and Border Protection**\n**(A) In general**\nAdministrative jurisdiction over approximately 25 acres of Federal land in Harpers Ferry, West Virginia, as generally depicted on the map entitled Harpers Ferry National Historical Park Proposed Land Transfers , numbered 385/176,677, and dated May 2021 (referred to in this section as the Map ) is transferred from the Secretary of the Interior (referred to in this section as the Secretary ) to the Commissioner of U.S. Customs and Border Protection, to be administered as part of the U.S. Customs and Border Protection's Advanced Training Center in accordance with applicable law.\n**(B) Exclusion from boundary**\nThe Federal land transferred by subparagraph (A) is excluded from the boundary of Harpers Ferry National Historical Park.\n**(2) Transfer to the Secretary**\nAdministrative jurisdiction over 3 parcels of Federal land totaling approximately 71.51 acres in Harpers Ferry, West Virginia, as generally depicted on the Map, is transferred from the Commissioner of U.S. Customs and Border Protection to the Secretary, to be administered by the Secretary\u2014\n**(A)**\nas part of Harpers Ferry National Historical Park; and\n**(B)**\nin accordance with applicable law.\n**(3) No reimbursement or consideration**\nA transfer of administrative jurisdiction over Federal land under paragraph (1)(A) or (2) shall be without monetary reimbursement or additional consideration.\n##### (b) Land surveys\n**(1) In general**\nThe Commissioner of U.S. Customs and Border Protection\u2014\n**(A)**\nshall obtain a survey to finalize the exact acreage and legal description of the parcel of Federal land described in subsection (a)(1)(A); and\n**(B)**\nmay, in consultation with the Secretary, modify any clerical and typographical errors in the Map.\n**(2) Cost of survey**\nThe cost of the survey under paragraph (1)(A) shall be charged to an appropriation of the U.S. Customs and Border Protection.\n**(3) Information sharing**\nOn completion of the survey under paragraph (1)(A), the Commissioner of U.S. Customs and Border Protection shall provide to the Secretary a copy of the survey.\n**(4) Reversion and restoration**\n**(A) In general**\nIf the Commissioner of U.S. Customs and Border Protection determines that the Federal land transferred by subparagraph (A) of subsection (a)(1) is no longer required for the U.S. Customs and Border Protection's Advanced Training Center, the Commissioner of U.S. Customs and Border Protection shall transfer administrative jurisdiction over the Federal land described in that subparagraph to the Secretary in a manner and condition acceptable to the Secretary, to be included within the boundary of, and to be administered as part of, Harpers Ferry National Historical Park.\n**(B) Acreage limitation**\nThe acreage limitation under section 1(d) of the Act of June 30, 1944 (58 Stat. 645, chapter 328; 16 U.S.C. 450bb(d) ) shall not apply to the inclusion within the boundary of Harpers Ferry National Historical Park of the Federal land under subparagraph (A).",
      "versionDate": "2025-07-15",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2280es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 2280\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo transfer administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia, and for other purposes.\n#### 1. Transfers of administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia\n##### (a) Transfers\n**(1) Transfer to the Commissioner of U.S. Customs and Border Protection**\n**(A) In general**\nAdministrative jurisdiction over approximately 25 acres of Federal land in Harpers Ferry, West Virginia, as generally depicted on the map entitled Harpers Ferry National Historical Park Proposed Land Transfers , numbered 385/176,677, and dated May 2021 (referred to in this section as the Map ) is transferred from the Secretary of the Interior (referred to in this section as the Secretary ) to the Commissioner of U.S. Customs and Border Protection, to be administered as part of the U.S. Customs and Border Protection's Advanced Training Center in accordance with applicable law.\n**(B) Exclusion from boundary**\nThe Federal land transferred by subparagraph (A) is excluded from the boundary of Harpers Ferry National Historical Park.\n**(2) Transfer to the Secretary**\nAdministrative jurisdiction over 3 parcels of Federal land totaling approximately 71.51 acres in Harpers Ferry, West Virginia, as generally depicted on the Map, is transferred from the Commissioner of U.S. Customs and Border Protection to the Secretary, to be administered by the Secretary\u2014\n**(A)**\nas part of Harpers Ferry National Historical Park; and\n**(B)**\nin accordance with applicable law.\n**(3) No reimbursement or consideration**\nA transfer of administrative jurisdiction over Federal land under paragraph (1)(A) or (2) shall be without monetary reimbursement or additional consideration.\n##### (b) Land surveys\n**(1) In general**\nThe Commissioner of U.S. Customs and Border Protection\u2014\n**(A)**\nshall obtain a survey to finalize the exact acreage and legal description of the parcel of Federal land described in subsection (a)(1)(A); and\n**(B)**\nmay, in consultation with the Secretary, modify any clerical and typographical errors in the Map.\n**(2) Cost of survey**\nThe cost of the survey under paragraph (1)(A) shall be charged to an appropriation of the U.S. Customs and Border Protection.\n**(3) Information sharing**\nOn completion of the survey under paragraph (1)(A), the Commissioner of U.S. Customs and Border Protection shall provide to the Secretary a copy of the survey.\n**(4) Reversion and restoration**\n**(A) In general**\nIf the Commissioner of U.S. Customs and Border Protection determines that the Federal land transferred by subparagraph (A) of subsection (a)(1) is no longer required for the U.S. Customs and Border Protection's Advanced Training Center, the Commissioner of U.S. Customs and Border Protection shall transfer administrative jurisdiction over the Federal land described in that subparagraph to the Secretary in a manner and condition acceptable to the Secretary, to be included within the boundary of, and to be administered as part of, Harpers Ferry National Historical Park.\n**(B) Acreage limitation**\nThe acreage limitation under section 1(d) of the Act of June 30, 1944 (58 Stat. 645, chapter 328; 16 U.S.C. 450bb(d) ) shall not apply to the inclusion within the boundary of Harpers Ferry National Historical Park of the Federal land under subparagraph (A).",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2026-03-11",
        "text": "Referred to the Subcommittee on Federal Lands."
      },
      "number": "6062",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To transfer administrative jurisdiction over certain parcels of federal land in Harpers Ferry, West Virginia, and for other purposes.",
      "type": "HR"
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
            "name": "Geography and mapping",
            "updateDate": "2026-05-01T19:25:09Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-05-01T19:24:58Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-05-01T19:25:03Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-05-01T19:25:14Z"
          },
          {
            "name": "West Virginia",
            "updateDate": "2026-05-01T19:24:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-04T21:37:24Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2280is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2280es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to transfer administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:36Z"
    },
    {
      "title": "A bill to transfer administrative jurisdiction over certain parcels of Federal land in Harpers Ferry, West Virginia, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T10:56:18Z"
    }
  ]
}
```

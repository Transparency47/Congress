# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1382
- Title: To amend the Federal Water Pollution Control Act with respect to San Francisco Bay restoration, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1382
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-06-03T08:05:34Z
- Update date including text: 2025-06-03T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-15 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- 2025-02-26 - Committee: Committee Consideration and Mark-up Session Held
- 2025-02-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 13.
- 2025-02-26 - Committee: Subcommittee on Water Resources and Environment Discharged
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-15 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- 2025-02-26 - Committee: Committee Consideration and Mark-up Session Held
- 2025-02-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 13.
- 2025-02-26 - Committee: Subcommittee on Water Resources and Environment Discharged

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1382",
    "number": "1382",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend the Federal Water Pollution Control Act with respect to San Francisco Bay restoration, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-06-03T08:05:34Z",
    "updateDateIncludingText": "2025-06-03T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
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
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Water Resources and Environment Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-15",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
            "date": "2025-02-26T18:13:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-26T16:46:18Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-02-14T18:33:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-15T17:17:28Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1382ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1382\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Huffman (for himself, Mr. Mullin , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act with respect to San Francisco Bay restoration, and for other purposes.\n#### 1. San Francisco Bay Restoration Program\nSection 125 of the Federal Water Pollution Control Act ( 33 U.S.C. 1276a ) is amended\u2014\n**(1)**\nin the section heading, by striking GRANT ; and\n**(2)**\nby amending subsection (e) to read as follows:\n(e) Program implementation (1) In general The Director may provide funding through cooperative agreements, grants, interagency agreements, contracts, or other funding mechanisms to Federal, State, and local agencies, special districts, public or nonprofit agencies, and other public or private entities, institutions, and organizations, including the Estuary Partnership, for projects, activities, and studies identified on the annual priority list compiled under subsection (c). (2) Agreements with non-federal entities (A) Maximum amount Amounts provided in the form of a grant, under a cooperative agreement, or through other funding mechanisms to any non-Federal entity under this section for a fiscal year shall not exceed an amount equal to 75 percent of the total cost of any projects, activities, and studies that are to be carried out using those amounts. (B) Non-federal share Not less than 25 percent of the cost of any project, activity, or study carried out using amounts provided in the form of a grant, under a cooperative agreement, or through other funding mechanisms under this section shall be provided from non-Federal sources. (C) Limitations on non-federal recipients No non-Federal entity may receive Federal funding under this section if that entity\u2014 (i) is domiciled in, headquartered in, organized under the laws of, or whose principal place of business is located in a foreign country of concern (as defined in 42 U.S.C. 19237 ); or (ii) has in place any agreement, partnership, or relationship with a foreign country of concern. (3) Federal interagency agreements Amounts provided to Federal agencies entities under interagency agreements under this section may be used to carry out activities described in subsection (c). .",
      "versionDate": "2025-02-14",
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
            "name": "California",
            "updateDate": "2025-03-05T21:17:26Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-05T21:17:11Z"
          },
          {
            "name": "Marine pollution",
            "updateDate": "2025-03-05T21:17:42Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-03-05T21:17:20Z"
          },
          {
            "name": "Seashores and lakeshores",
            "updateDate": "2025-03-05T21:17:58Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-03-05T21:17:49Z"
          },
          {
            "name": "Wetlands",
            "updateDate": "2025-03-05T21:17:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-02-24T17:18:12Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1382ih.xml"
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
      "title": "To amend the Federal Water Pollution Control Act with respect to San Francisco Bay restoration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T04:18:33Z"
    },
    {
      "title": "To amend the Federal Water Pollution Control Act with respect to San Francisco Bay restoration, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-15T09:07:25Z"
    }
  ]
}
```

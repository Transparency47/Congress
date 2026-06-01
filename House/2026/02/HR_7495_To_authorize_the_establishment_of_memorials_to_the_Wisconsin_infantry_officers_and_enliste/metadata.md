# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7495?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7495
- Title: To authorize the establishment of memorials to the Wisconsin infantry officers and enlisted men who fought in the Battle of Antietam and the Second Battle of Bull Run, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7495
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-04-21T08:06:35Z
- Update date including text: 2026-04-21T08:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7495",
    "number": "7495",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "To authorize the establishment of memorials to the Wisconsin infantry officers and enlisted men who fought in the Battle of Antietam and the Second Battle of Bull Run, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:35Z",
    "updateDateIncludingText": "2026-04-21T08:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
        "item": {
          "date": "2026-02-11T16:03:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7495ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7495\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Fitzgerald (for himself, Mr. Steil , Mr. Van Orden , Mr. Grothman , Mr. Tiffany , and Mr. Wied ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the establishment of memorials to the Wisconsin infantry officers and enlisted men who fought in the Battle of Antietam and the Second Battle of Bull Run, and for other purposes.\n#### 1. Establishment of Wisconsin memorials at Antietam and Manassas\n##### (a) Memorials authorized\nThe Secretary of the Interior (referred to in this section as the Secretary ) shall authorize the establishment of\u2014\n**(1)**\nat a suitable location approved by the Secretary within the boundaries of Antietam National Battlefield, a memorial to the officers and enlisted men of the Second, Third, Fifth, Sixth, and Seventh Wisconsin Infantry Regiments who fought in the Battle of Antietam on September 17, 1862; and\n**(2)**\nat a suitable location approved by the Secretary within the boundaries of Manassas National Battlefield Park, a memorial to the officers and enlisted men of the Second, Sixth, and Seventh Wisconsin Infantry Regiments who fought in the Second Battle of Bull Run on August 28\u201330, 1862.\n##### (b) Authorized entity\nThe Secretary shall select the persons who may establish each of the memorials authorized by subsection (a).\n##### (c) Design approvals\nThe size, design, and inscriptions of the memorials authorized by subsection (a) shall be subject to the approval of the Secretary.\n##### (d) Prohibition on use of Federal funds for establishment\nNo Federal funds may be expended to design the memorials authorized by subsection (a), to acquire the memorials, to prepare the site selected for the memorials, or to install the memorials.\n##### (e) Suspension for misrepresentation in fundraising\nThe Secretary may suspend the authority of the persons selected under subsection (b) to establish the memorials authorized by subsection (a) if the Secretary determines that fundraising efforts relating to the memorials have misrepresented an affiliation with the memorials or the Federal Government.\n##### (f) Annual Report\nUntil each memorial authorized by subsection (a) is installed, the persons selected under subsection (b) to establish that memorial shall submit to the Secretary an annual report of operations related to fundraising efforts for the memorial and progress on the establishment of the memorial.\n##### (g) Maintenance\nUpon installation of each memorial authorized by subsection (a), the Secretary shall assume responsibility for the maintenance of that memorial. The Secretary may accept contributions for the maintenance of the memorials from the persons selected under subsection (b) to establish the memorials and from other persons. Amounts accepted under this subsection shall be merged with other funds available to the Secretary for the maintenance of the memorials and credited to a separate account with the National Park Foundation.",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-02-20T20:27:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7495ih.xml"
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
      "title": "To authorize the establishment of memorials to the Wisconsin infantry officers and enlisted men who fought in the Battle of Antietam and the Second Battle of Bull Run, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:39Z"
    },
    {
      "title": "To authorize the establishment of memorials to the Wisconsin infantry officers and enlisted men who fought in the Battle of Antietam and the Second Battle of Bull Run, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T09:06:36Z"
    }
  ]
}
```

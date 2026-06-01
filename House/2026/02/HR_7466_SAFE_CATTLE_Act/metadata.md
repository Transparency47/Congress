# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7466
- Title: SAFE CATTLE Act
- Congress: 119
- Bill type: HR
- Bill number: 7466
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-05-15T08:07:44Z
- Update date including text: 2026-05-15T08:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7466",
    "number": "7466",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SAFE CATTLE Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:44Z",
    "updateDateIncludingText": "2026-05-15T08:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-10T15:02:00Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "WY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
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
      "sponsorshipDate": "2026-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7466ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7466\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Jackson of Texas (for himself, Mr. Davis of North Carolina , Ms. Hageman , and Mr. Soto ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Agriculture and the Secretary of the Interior to enter into a memorandum of understanding or other interagency agreement, to carry out, and coordinate on, activities to prevent, control, and eradicate New World screwworm in wildlife and non-livestock species of animals on certain Federal lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding America\u2019s Food Economy and Controlling Agricultural Threats to Livestock and Enterprises Act or the SAFE CATTLE Act .\n#### 2. Interagency cooperation on New World screwworm eradication and monitoring activities\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Agriculture and the Secretary of the Interior shall enter into a memorandum of understanding or other interagency agreement, to carry out, and coordinate on, activities to prevent, control, and eradicate New World screwworm in wildlife and non-livestock species of animals on covered lands. Such activities shall include\u2014\n**(1)**\ncoordinating joint surveillance and monitoring protocols for early detection of New World screwworm in wildlife and non-livestock species of animals on covered lands;\n**(2)**\nfor purposes of controlling and containing New World screwworm in all species of animals on covered lands in the event of an outbreak, coordinating with (as appropriate) State wildlife and livestock health officers with respect to response procedures, the distribution of information, and notification procedures;\n**(3)**\ncoordinating New World screwworm eradication protocols to protect wildlife and non-livestock species of animals on covered lands, stabilize and reduce the threat to domestic animal agriculture, and safeguard the domestic food supply and the economy; and\n**(4)**\ndeveloping science-based and risk-based approaches and systems to facilitate continuity of business for non-infected animals of all species and non-contaminated areas on covered lands.\n##### (b) Report\nNot later than one year after the date of the enactment of this Act, and annually thereafter until the date on which the Secretary of Agriculture certifies to the Congress that the New World screwworm has been quarantined south of the Darien Gap in Panama, the Secretary of Agriculture and the Secretary of the Interior shall jointly submit to the Committee on Agriculture and the Committee on Natural Resources of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry and the Committee on Energy and Natural Resources of the Senate a report detailing the following:\n**(1)**\nthe extent of interagency coordination between each Federal agency involved in the prevention, control, and eradication of New World screwworm on covered lands;\n**(2)**\nany progress made in the surveillance and prevention of New World screwworm outbreaks;\n**(3)**\nany incidents of infestation of New World screwworm in the United States and Federal collaborative activities undertaken to control the spread of such infestation; and\n**(4)**\nany recommendations for legislative or administrative action to improve the Federal response capacity to the threat of New World screwworm.\n##### (c) Covered lands defined\nIn this Act, the term covered lands means lands managed by the National Park Service, the United States Fish and Wildlife Service, the Bureau of Land Management, the Bureau of Reclamation, or the Forest Service.",
      "versionDate": "2026-02-10",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-24T18:27:52Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7466ih.xml"
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
      "title": "SAFE CATTLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE CATTLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding America\u2019s Food Economy and Controlling Agricultural Threats to Livestock and Enterprises Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture and the Secretary of the Interior to enter into a memorandum of understanding or other interagency agreement, to carry out, and coordinate on, activities to prevent, control, and eradicate New World screwworm in wildlife and non-livestock species of animals on certain Federal lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:23Z"
    }
  ]
}
```

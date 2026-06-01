# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7949
- Title: NSF Plant Biology Act
- Congress: 119
- Bill type: HR
- Bill number: 7949
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-10T08:06:18Z
- Update date including text: 2026-04-10T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7949",
    "number": "7949",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000622",
        "district": "19",
        "firstName": "Josh",
        "fullName": "Rep. Riley, Josh [D-NY-19]",
        "lastName": "Riley",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "NSF Plant Biology Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:18Z",
    "updateDateIncludingText": "2026-04-10T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "IN"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7949ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7949\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Riley of New York (for himself and Mr. Baird ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the National Science Foundation Authorization Act of 2002 to provide for grants to support plant and microbial biology research with potential relevance to agriculture, food, or biotechnology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Plant Biological Research at the National Science Foundation Act or the NSF Plant Biology Act .\n#### 2. Fundamental plant biology research\n##### (a) In general\nThe National Science Foundation Authorization Act of 2002 is amended by adding at the end the following new section:\n27. Fundamental plant biology research (a) In general The Director may award grants on a competitive, merit-reviewed basis to institutions of higher education, nonprofit organizations, private sector entities, and Federal, State, local, or Tribal governments, or a consortia of such institutions, entities, or governments, to support plant and microbial biology research with potential relevance to agriculture, food, or biotechnology, including relating to the following: (1) Fundamental research regarding plant biology. (2) Tools, resources, and technology that further enable plant biology. (b) Authorization of appropriations There is authorized to be appropriated to the Director $150,000,000 for each of fiscal years 2026 through 2031 to carry out this section. .\n##### (b) Definition amendment\nSection 4 of the National Science Foundation Authorization Act of 2002 is amended by\u2014\n**(1)**\nredesignating paragraphs (13) through (16) as paragraphs (14) through (17), respectively; and\n**(2)**\nby inserting after paragraph (12) the following new paragraph:\n(13) Nonprofit organization The term nonprofit organization means an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from tax under section 15 501(a) of such Code. .",
      "versionDate": "2026-03-16",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-18T14:31:40Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7949ih.xml"
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
      "title": "NSF Plant Biology Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NSF Plant Biology Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Plant Biological Research at the National Science Foundation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Science Foundation Authorization Act of 2002 to provide for grants to support plant and microbial biology research with potential relevance to agriculture, food, or biotechnology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T08:18:32Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7925
- Title: American Families First Assistance Act
- Congress: 119
- Bill type: HR
- Bill number: 7925
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-02T18:59:46Z
- Update date including text: 2026-04-02T18:59:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7925",
    "number": "7925",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "American Families First Assistance Act",
    "type": "HR",
    "updateDate": "2026-04-02T18:59:46Z",
    "updateDateIncludingText": "2026-04-02T18:59:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:35:40Z",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "CO"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ID"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7925ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7925\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Steube (for himself and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 to limit the eligibility of aliens to receive benefits under the temporary assistance for needy families program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Families First Assistance Act .\n#### 2. Alien eligibility for temporary assistance for needy families\nSection 402 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1612 ) is amended\u2014\n**(1)**\nin subsection (b)(3), by repealing subparagraph (A); and\n**(2)**\nby adding at the end the following:\n(c) Limited eligibility for temporary assistance for needy families (1) In general Notwithstanding any other provision of law and except as provided in paragraph (2), an alien who is a qualified alien (as defined in section 431) is not eligible for the program of block grants to States for temporary assistance for needy families under part A of title IV of the Social Security Act. (2) Exception Paragraph (1) shall not apply to an alien who is described in paragraph (1), (7) (with respect to a national of Cuba), or (8) of section 431(b). .",
      "versionDate": "2026-03-12",
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
        "name": "Social Welfare",
        "updateDate": "2026-04-02T18:59:46Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7925ih.xml"
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
      "title": "American Families First Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T12:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Families First Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 to limit the eligibility of aliens to receive benefits under the temporary assistance for needy families program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:22Z"
    }
  ]
}
```

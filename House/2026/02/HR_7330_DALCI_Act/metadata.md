# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7330?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7330
- Title: DALCI Act
- Congress: 119
- Bill type: HR
- Bill number: 7330
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-02-23T22:12:02Z
- Update date including text: 2026-02-23T22:12:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-03: Introduced in House

## Actions

- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7330",
    "number": "7330",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "DALCI Act",
    "type": "HR",
    "updateDate": "2026-02-23T22:12:02Z",
    "updateDateIncludingText": "2026-02-23T22:12:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
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
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7330ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7330\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Mrs. Hinson (for herself and Mr. Sorensen ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to reestablish the Driftless Area Landscape Conservation Initiative, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Driftless Area Landscape Conservation Initiative Act or the DALCI Act .\n#### 2. Driftless Area Landscape Conservation Initiative\nSubchapter A of chapter 4 of subtitle D of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3839aa et seq. ) is amended by adding at the end the following:\n1240H\u20131. Driftless Area Landscape Conservation Initiative (a) Establishment The Secretary shall establish a Driftless Area Landscape Conservation Initiative to reduce erosion and restore cold water stream corridors in the Driftless Area of the Midwestern United States, with a focus on climate-smart agriculture, carbon sequestration, soil health, and ecological restoration. (b) Initiative elements (1) In general In carrying out the initiative established under this section, the Secretary shall provide assistance to producers to implement practices to\u2014 (A) manage working lands for year-round ground cover to rebuild soil, sequester carbon, improve water quality, increase water holding capacity of soil, reduce soil erosion, and mitigate flooding and other climate impacts; (B) manage woodlands for increased biodiversity to improve the health of the woods to provide habitat and sequester carbon; (C) restore prairies and manage grasslands, oak savannas, and barrens to expand habitat and sequester carbon; and (D) restore cold water streams, by reducing stream bank erosion and threats of flooding while improving trout habitat. (2) Partnerships In carrying out the initiative established under this section, the Secretary shall provide assistance to grassroots partnerships to educate landowners and operators on the benefits of climate-smart agriculture, soil health, and holistic grazing. (3) Types of assistance The Secretary may provide assistance under this section in the form of financial assistance, technical assistance, and payments for the conveyance of easements to the Secretary, under such terms as the Secretary may establish. (c) Funding Of the funds made available to carry out this subchapter, the Secretary shall carry out this section using $5,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2026-02-03",
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
        "updateDate": "2026-02-23T22:12:02Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7330ih.xml"
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
      "title": "DALCI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DALCI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Driftless Area Landscape Conservation Initiative Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to reestablish the Driftless Area Landscape Conservation Initiative, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T08:34:00Z"
    }
  ]
}
```

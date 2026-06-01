# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3272
- Title: COMPOST Act
- Congress: 119
- Bill type: HR
- Bill number: 3272
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-02-21T09:05:42Z
- Update date including text: 2026-02-21T09:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3272",
    "number": "3272",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "COMPOST Act",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:42Z",
    "updateDateIncludingText": "2026-02-21T09:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:00:50Z",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "ME"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3272ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3272\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Brownley (for herself and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the designation of composting as a conservation practice and activity, and to provide grants and loan guarantees for composting facilities and programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cultivating Organic Matter through the Promotion Of Sustainable Techniques Act or the COMPOST Act .\n#### 2. Composting as conservation practice\n##### (a) Conservation standards and requirements\nSection 1241(j) of the Food Security Act of 1985 ( 16 U.S.C. 3841(j) ) is amended\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (3); and\n**(2)**\nby inserting after paragraph (1) the following new paragraph:\n(2) Composting as conservation practice and activity (A) In general The Secretary shall by regulation provide that composting is a conservation practice and a conservation activity for the purposes of this title. (B) Composting defined (i) In general For the purposes of this paragraph, the term composting means\u2014 (I) an activity (including an activity that does not require the use of a composting facility) to produce compost from organic waste that is\u2014 (aa) generated on a farm; or (bb) brought to a farm from a nearby community and used to produce compost on that farm; and (II) the use and active management of compost on a farm, in accordance with any applicable Federal, State, or local law, to improve water retention and soil health. (ii) Determination of nearby communities The Secretary, in consultation with the Administrator of the Environmental Protection Agency, shall issue regulations for determining whether a community is nearby for purposes of clause (i)(I), which shall ensure that bringing organic waste from the community to the farm to produce compost results in a net reduction of greenhouse gas emissions. .\n##### (b) Conservation stewardship program\nSection 1240I(2)(B)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201321(2)(B)(i) ) is amended by inserting and composting practices after agriculture drainage management systems .\n##### (c) Environmental quality incentives program\nSection 1240A(6)(A)(ii) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131(6)(A)(ii) ) is amended by inserting , including composting practices before the semicolon at the end.\n##### (d) Delivery of technical assistance\nSection 1242(h) of the Food Security Act of 1985 ( 16 U.S.C. 3842(h) ) is amended by adding at the end the following:\n(5) Development of composting practice standard In addition to conducting a review under this subsection of any composting facility practice standard established before the date of enactment of this paragraph, the Secretary shall establish a composting practice standard under the process developed under paragraph (3). .",
      "versionDate": "2025-05-08",
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
        "updateDate": "2025-05-27T15:27:39Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3272ih.xml"
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
      "title": "COMPOST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COMPOST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cultivating Organic Matter through the Promotion Of Sustainable Techniques Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the designation of composting as a conservation practice and activity, and to provide grants and loan guarantees for composting facilities and programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T05:48:38Z"
    }
  ]
}
```

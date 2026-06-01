# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7804?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7804
- Title: BLS Act
- Congress: 119
- Bill type: HR
- Bill number: 7804
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-04-01T19:34:43Z
- Update date including text: 2026-04-01T19:34:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7804",
    "number": "7804",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "BLS Act",
    "type": "HR",
    "updateDate": "2026-04-01T19:34:43Z",
    "updateDateIncludingText": "2026-04-01T19:34:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7804ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7804\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. Pressley (for herself and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Labor to perform additional duties, to modernize certain laws regarding the Bureau of Labor Statistics, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Better Labor Statistics Act or the BLS Act .\n#### 2. Modernizing duties and terms relating to the Bureau of Labor Statistics\n##### (a) Additional duties\n**(1) Labor statistics**\nSection 4 of the Act of March 4, 1913, titled An Act to create a Department of Labor ( 29 U.S.C. 2 ; Chap. 141), is amended\u2014\n**(A)**\nin the first sentence, by striking Secretary of Labor may collate and inserting Secretary of Labor shall collate ; and\n**(B)**\nin the third sentence, by striking Such statistics shall be reported and inserting Such statistics shall be publicly reported, in accordance with the first section of Public Law 94\u2013311 , online by the first Friday of each month, including .\n**(2) Demographics**\nThe first section of Public Law 94\u2013311 ( 29 U.S.C. 8 ; 90 Stat. 688) following the resolving clause is amended by striking unemployment data and all that follows and inserting unemployment data relating to individual demographics. In each labor statistics report required by section 4 of the Act of March 4, 1913, entitled An Act to create a Department of Labor ( 29 U.S.C. 2 ; Chap. 141), the Secretary of Labor shall include, at a minimum, data disaggregated by the demographic categories of geography, race, ethnicity, and gender. .\n##### (b) Modernizing terms\nSection 4 of the Act of March 4, 1913, titled An Act to create a Department of Labor ( 29 U.S.C. 2 ; Chap. 141), as amended by subsection (a), is further amended\u2014\n**(1)**\nin the first sentence\u2014\n**(A)**\nby striking report at least once each year, or oftener and inserting publicly report, in accordance with the first section of Public Law 94\u2013311 , at least once each year, or more frequently ;\n**(B)**\nby striking provided for his department and inserting provided for the Department of Labor ; and\n**(C)**\nby striking such manner as to him and inserting such manner as the Secretary ; and\n**(2)**\nin the last sentence, by striking such manner as he may deem satisfactory and inserting such manner as the Secretary may deem satisfactory .\n##### (c) Heading\nThe Law Revision Counsel is directed to, where the first section of Public Law 94\u2013311 ( 29 U.S.C. 8 ; 90 Stat. 688), as amended by subsection (a)(2), is displayed in the United States Code, designate the heading of such section as Unemployment data relating to individual demographics .",
      "versionDate": "2026-03-04",
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
        "name": "Labor and Employment",
        "updateDate": "2026-04-01T19:34:43Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7804ih.xml"
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
      "title": "BLS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BLS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Better Labor Statistics Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Labor to perform additional duties, to modernize certain laws regarding the Bureau of Labor Statistics, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T07:18:35Z"
    }
  ]
}
```

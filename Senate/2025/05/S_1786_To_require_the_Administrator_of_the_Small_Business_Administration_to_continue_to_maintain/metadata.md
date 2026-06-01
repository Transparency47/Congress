# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1786?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1786
- Title: One Stop Shop for Small Business Licensing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1786
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-06-02T13:01:57Z
- Update date including text: 2025-06-02T13:01:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1786",
    "number": "1786",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "One Stop Shop for Small Business Licensing Act of 2025",
    "type": "S",
    "updateDate": "2025-06-02T13:01:57Z",
    "updateDateIncludingText": "2025-06-02T13:01:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
        "item": {
          "date": "2025-05-15T18:45:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "sponsorshipDate": "2025-05-15",
      "state": "WV"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1786is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1786\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Ms. Rosen (for herself, Mrs. Capito , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo require the Administrator of the Small Business Administration to continue to maintain a website regarding small business permitting and licensing requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Stop Shop for Small Business Licensing Act of 2025 .\n#### 2. Continued availability of SBA website for business permitting and licensing requirements\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Small Business Administration.\n**(2) Covered website**\nThe term covered website \u2014\n**(A)**\nmeans the website found at https://www.sba.gov/business-guide/launch-your-business/apply-licenses-permits, as of May 14, 2025; and\n**(B)**\nincludes any successor website to the website described in subparagraph (A) that\u2014\n**(i)**\nhas a different uniform resource locator than the website described in subparagraph (A); and\n**(ii)**\nmakes available information that is substantially similar to the information made available through the website described in subparagraph (A).\n##### (b) Public availability of website\nOn and after the date of enactment of this Act, the Administrator shall ensure that the covered website, and all of the information made available through the covered website (as that information may be updated by the Administrator given applicable changes with respect to the requirements that the covered website addresses), is publicly available.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in Senate"
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
        "name": "Commerce",
        "updateDate": "2025-06-02T13:01:57Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1786is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "One Stop Shop for Small Business Licensing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "One Stop Shop for Small Business Licensing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Small Business Administration to continue to maintain a website regarding small business permitting and licensing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:30Z"
    }
  ]
}
```

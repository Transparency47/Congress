# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1255?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1255
- Title: Cormorant Relief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1255
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2026-01-26T14:42:09Z
- Update date including text: 2026-01-26T14:42:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1255",
    "number": "1255",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Cormorant Relief Act of 2025",
    "type": "S",
    "updateDate": "2026-01-26T14:42:09Z",
    "updateDateIncludingText": "2026-01-26T14:42:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T18:17:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MS"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1255is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1255\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Cotton (for himself, Mr. Tuberville , Mrs. Britt , Mrs. Hyde-Smith , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Secretary of the Interior to reissue certain regulations relating to the taking of double-crested cormorants at aquaculture facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cormorant Relief Act of 2025 .\n#### 2. Regulations relating to taking of double-crested cormorants at aquaculture facilities\n##### (a) Definitions\nIn this section:\n**(1) Lake manager**\nThe term lake manager means a person that is licensed by a State regulatory agency to manage a private lake.\n**(2) Original depredation order**\nThe term original depredation order means the depredation order for double-crested cormorants at aquaculture facilities contained in section 21.47 of title 50, Code of Federal Regulations (as in effect on January 1, 2016).\n**(3) Pond manager**\nThe term pond manager means a person that is licensed by a State regulatory agency to manage a private pond.\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n##### (b) Reissuance required\nNot later than 1 year after the date of enactment of this Act, the Secretary shall reissue the original depredation order in accordance with subsection (c).\n##### (c) Requirements\nThe depredation order reissued under subsection (b) shall be the same as the original depredation order, except that the depredation order reissued under that subsection shall apply\u2014\n**(1)**\nto each of the States of California, Colorado, Connecticut, Illinois, Indiana, Iowa, Michigan, Missouri, New Jersey, Ohio, Pennsylvania, and Wisconsin in addition to, and in the same manner as, each of the States to which the original depredation order applied; and\n**(2)**\nto lake managers and pond managers in addition to, and in the same manner as, each of the entities to which the original depredation order applied.",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-10",
        "text": "Received in the Senate and Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2293",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Cormorant Relief Act of 2025",
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
            "name": "Alabama",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Aquaculture",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Arkansas",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Birds",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "California",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Connecticut",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Florida",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Georgia",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Illinois",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Indiana",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Iowa",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Kentucky",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Louisiana",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Michigan",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Mississippi",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Missouri",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "New Jersey",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Oklahoma",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Pennsylvania",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "South Carolina",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Tennessee",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-05-20T19:06:12Z"
          },
          {
            "name": "Wisconsin",
            "updateDate": "2025-05-20T19:06:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-12-08T05:22:24Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1255is.xml"
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
      "title": "Cormorant Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T03:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cormorant Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Interior to reissue certain regulations relating to the taking of double-crested cormorants at aquaculture facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:37Z"
    }
  ]
}
```

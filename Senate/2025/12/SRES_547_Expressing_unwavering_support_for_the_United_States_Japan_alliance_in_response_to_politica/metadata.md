# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/547?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/547
- Title: A resolution expressing unwavering support for the United States-Japan alliance in response to political, economic and military pressure by the People's Republic of China.
- Congress: 119
- Bill type: SRES
- Bill number: 547
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-03-11T10:56:27Z
- Update date including text: 2026-03-11T10:56:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-12-17 - IntroReferral: Submitted in Senate
- Latest action: 2025-12-17: Submitted in Senate

## Actions

- 2025-12-17 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-12-17 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/547",
    "number": "547",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution expressing unwavering support for the United States-Japan alliance in response to political, economic and military pressure by the People's Republic of China.",
    "type": "SRES",
    "updateDate": "2026-03-11T10:56:27Z",
    "updateDateIncludingText": "2026-03-11T10:56:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
            "date": "2025-12-17T21:46:34Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-17T21:46:34Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "DE"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NJ"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "CO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres547is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 547\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Ricketts (for himself, Mr. Coons , Mr. Hagerty , and Mrs. Shaheen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing unwavering support for the United States-Japan alliance in response to political, economic and military pressure by the People\u2019s Republic of China against Japan.\nThat the Senate\u2014\n**(1)**\ncondemns the Government of the People\u2019s Republic of China\u2019s use of economic, military, and diplomatic coercion and aggression against Japan, a United States defense treaty ally;\n**(2)**\ncommends the Government of Japan\u2019s opposition to the efforts of the Government of the People\u2019s Republic of China to\u2014\n**(A)**\nundermine regional stability; and\n**(B)**\nunilaterally change the status quo in the Taiwan Strait by force or coercion;\n**(3)**\nrecognizes Japan\u2019s commitments to peace and security and its continuing role as a key ally in maintaining a free and open Indo-Pacific;\n**(4)**\napplauds the Government of Japan\u2019s efforts to increase its own defense spending to invest in capabilities to enhance deterrence across the region;\n**(5)**\napplauds the Government of Japan\u2019s efforts to diffuse tensions with the Government of the People\u2019s Republic of China despite continuous unilateral provocations;\n**(6)**\nreaffirms the United States unwavering commitment to article V of the United States-Japan Treaty of Mutual Cooperation and Security, and that the Senkaku Islands fall within article V\u2019s scope; and\n**(7)**\nstands with the Government of Japan and the Japanese people against the Government of the People\u2019s Republic of China\u2019s attempts to harass and escalate tensions with Japan.",
      "versionDate": "2025-12-17",
      "versionType": "IS"
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
        "actionDate": "2026-01-30",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "71",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing unwavering support for the United States-Japan alliance in response to political, economic, and military pressure by the People's Republic of China against Japan.",
      "type": "HCONRES"
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
        "name": "International Affairs",
        "updateDate": "2025-12-19T18:06:56Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres547is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing unwavering support for the United States-Japan alliance in response to political, economic and military pressure by the People's Republic of China.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:46Z"
    },
    {
      "title": "A resolution expressing unwavering support for the United States-Japan alliance in response to political, economic and military pressure by the People's Republic of China.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T11:56:17Z"
    }
  ]
}
```

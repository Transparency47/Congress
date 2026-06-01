# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/774?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/774
- Title: WHO is Accountable Act
- Congress: 119
- Bill type: S
- Bill number: 774
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-05-27T14:12:52Z
- Update date including text: 2025-05-27T14:12:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/774",
    "number": "774",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "WHO is Accountable Act",
    "type": "S",
    "updateDate": "2025-05-27T14:12:52Z",
    "updateDateIncludingText": "2025-05-27T14:12:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T17:01:13Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s774is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 774\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mrs. Blackburn (for herself, Mr. Barrasso , Mr. Scott of Florida , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit the use of funds to seek membership in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization until certain conditions have been met.\n#### 1. Short title\nThis Act may be cited as the WHO is Accountable Act .\n#### 2. Prohibition on use of funds to seek membership in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization\n##### (a) In general\nNotwithstanding any other provision of law, no funds available to any Federal department or agency may be used to seek membership by the United States in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization until after the Secretary of State certifies to Congress that the World Health Organization meets all of the conditions described in subsection (b).\n##### (b) Conditions described\nThe conditions described in this subsection will be met when the World Health Organization\u2014\n**(1)**\nhas adopted meaningful reforms to ensure that humanitarian assistance is not politicized and is being provided to those with the most need;\n**(2)**\nis not under the control or significant malign influence of the Chinese Communist Party;\n**(3)**\nis not involved in a coverup of the Chinese Communist Party\u2019s response to the COVID\u201319 pandemic;\n**(4)**\ngrants observer status to Taiwan;\n**(5)**\nis not diverting humanitarian or medical supplies to Iran, North Korea, or Syria;\n**(6)**\nhas established mechanisms to increase transparency and accountability in its operations and eliminate waste, fraud, and abuse;\n**(7)**\nhas ceased all funding for, engagement in, and messaging with respect to certain controversial and politically charged issues that are non-germane to the World Health Organization\u2019s directive, including\u2014\n**(A)**\nso-called gender identity and harmful rhetoric relating to gender affirming care ;\n**(B)**\nclimate change; and\n**(C)**\naccess to abortion; and\n**(8)**\nhas agreed, as a condition of membership by the United States in the World Health Organization, that no directive issued by the World Health Organization may be considered to be legally binding on any United States citizen or individual State.",
      "versionDate": "2025-02-27",
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
        "name": "International Affairs",
        "updateDate": "2025-05-09T20:25:38Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s774is.xml"
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
      "title": "WHO is Accountable Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WHO is Accountable Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of funds to seek membership in the World Health Organization or to provide assessed or voluntary contributions to the World Health Organization until certain conditions have been met.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:45Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/24?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/24
- Title: A concurrent resolution recognizing the 30th anniversary of the Dayton Peace Accords.
- Congress: 119
- Bill type: SCONRES
- Bill number: 24
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2025-12-04T17:23:46Z
- Update date including text: 2025-12-04T17:23:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S8453)
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S8453)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/24",
    "number": "24",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "A concurrent resolution recognizing the 30th anniversary of the Dayton Peace Accords.",
    "type": "SCONRES",
    "updateDate": "2025-12-04T17:23:46Z",
    "updateDateIncludingText": "2025-12-04T17:23:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S8453)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T20:41:10Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "IA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MD"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres24is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 24\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mrs. Shaheen (for herself, Mr. Welch , Mr. Schiff , Mr. Durbin , Mr. Grassley , and Mr. Van Hollen ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Relations\nCONCURRENT RESOLUTION\nRecognizing the 30th anniversary of the Dayton Peace Accords.\nThat the Senate\u2014\n**(1)**\nreaffirms the joint United States and European Union (EU) commitment to promote and protect human rights, democracy, and the rule of law in Bosnia and Herzegovina and around the world;\n**(2)**\ncommends the continued commitment of the people of Bosnia and Herzegovina to peace and cooperation 30 years after the signing of the Dayton Peace Accords;\n**(3)**\nnotes the efforts undertaken by the Government of Bosnia and Herzegovina toward North Atlantic Treaty Organization (NATO) and EU membership, including measures to resolve its constitutional issues, strengthen its governance structures, and undertake necessary economic, rule of law, and judicial reforms;\n**(4)**\nreiterates the continued importance of the Dayton Peace Accords as the basis of constitutional reform in Bosnia and Herzegovina and the promotion of political, economic, legal, and religious equality, which are also key requirements for EU accession;\n**(5)**\nurges the Government of Bosnia and Herzegovina\u2014\n**(A)**\nto continue to pursue constitutional reforms needed to reconcile the past and engage across ethnic and religious lines with empathy and respect to build a common future; and\n**(B)**\nthrough its respective leaders, to uphold the integrity of the tripartite presidency, strengthen its key institutions, and work to achieve an independent democracy;\n**(6)**\nurges the United States Government\u2014\n**(A)**\nto maintain support for the Office of the High Representative until members of the Peace Implementation Council reach a unanimous agreement that the presence of the Office of the High Representative is no longer necessary; and\n**(B)**\nto work closely with Bosnia and Herzegovina and its neighboring countries, especially countries who are signatories of the Dayton Peace Accords, to support full implementation of Stabilisation and Association Agreements between the EU and the Balkan States;\n**(7)**\nencourages continued regional cooperation to combat the malign influence of foreign actors, such as the Russian Federation and the People's Republic of China;\n**(8)**\nrecognizes the State of Ohio and the greater Dayton community for\u2014\n**(A)**\ntheir roles in fostering the Dayton Peace Accords; and\n**(B)**\ntheir continued support for diplomacy, security, and peace around the world; and\n**(9)**\nacknowledges the important contributions of the Bosnian-American diaspora in their communities throughout the United States.",
      "versionDate": "2025-12-02",
      "versionType": "IS"
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
        "updateDate": "2025-12-04T17:23:46Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres24is.xml"
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
      "title": "A concurrent resolution recognizing the 30th anniversary of the Dayton Peace Accords.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T11:56:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A concurrent resolution recognizing the 30th anniversary of the Dayton Peace Accords.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T11:56:23Z"
    }
  ]
}
```

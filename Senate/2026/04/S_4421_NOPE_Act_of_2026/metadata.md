# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4421?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4421
- Title: NOPE Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4421
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-12T19:53:24Z
- Update date including text: 2026-05-12T19:53:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4421",
    "number": "4421",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "NOPE Act of 2026",
    "type": "S",
    "updateDate": "2026-05-12T19:53:24Z",
    "updateDateIncludingText": "2026-05-12T19:53:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T22:19:07Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NH"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "MS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4421is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4421\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mr. Gallego (for himself, Mr. Grassley , Mrs. Shaheen , Mr. Kaine , Mr. Blumenthal , Mr. Wicker , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Countering America\u2019s Adversaries Through Sanctions Act to expand review by Congress of actions relating to sanctions imposed with respect to the Russian Federation.\n#### 1. Short title\nThis Act may be cited as the No Oil Profits for Enemies Act of 2026 or the NOPE Act of 2026 .\n#### 2. Modifications to congressional review of sanctions with respect to the Russian Federation\n##### (a) Expansion of sanctions subject To review\nSection 216(a)(2)(B)(i) of the Countering America\u2019s Adversaries Through Sanctions Act ( 22 U.S.C. 9511(a)(2)(B)(i) ) is amended\u2014\n**(1)**\nin subclause (II), by striking ; or and inserting a semicolon;\n**(2)**\nin subclause (III), by striking ; and and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(IV) any Executive order addressing the national emergency declared in Executive Order 14024 ( 50 U.S.C. 1701 note; relating to blocking property with respect to specified harmful foreign activities of the Government of the Russian Federation). .\n##### (b) Review of energy-Related actions\nSection 216(a)(2) of the Countering America\u2019s Adversaries Through Sanctions Act ( 22 U.S.C. 9511(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (ii), by striking ; or and inserting a semicolon;\n**(B)**\nin clause (iii), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(iv) an action, including a licensing action, taken during the period described in subparagraph (C) relating to the application of sanctions described in subparagraph (B) with respect to crude oil, petroleum products, natural gas, or other energy products of Russian Federation origin. ; and\n**(2)**\nby adding at the end the following:\n(C) Period for review for energy-related actions The period described in this subparagraph is the period\u2014 (i) beginning on the date of the enactment of this subparagraph; and (ii) ending on the date on which the Secretary of State, in consultation with the Secretary of the Treasury, the Secretary of Defense, and the Director of National Intelligence, certifies to the appropriate congressional committees and leadership that the Government of the Russian Federation has ended its war in Ukraine and credibly committed to a just peace settlement that includes compensating Ukraine for war damages. .\n##### (c) Exception To take action during initial congressional review period\nSection 216(b)(3) of the Countering America\u2019s Adversaries Through Sanctions Act ( 22 U.S.C. 9511(b)(3) ) is amended\u2014\n**(1)**\nby striking unless a joint resolution and inserting the following: \u201cunless\u2014\n(A) a joint resolution ;\n**(2)**\nby striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(B) the action relates to crude oil, petroleum products, natural gas, or other energy products of Russian Federation origin to be used\u2014 (i) for the preservation of the health or safety of the crew of an energy transport vessel; (ii) for emergency repairs or environmental mitigation or protection activities relating to an energy transport vessel; or (iii) to address an urgent need to mitigate an economic impact in a foreign jurisdiction other than the Russian Federation. .",
      "versionDate": "2026-04-28",
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
        "updateDate": "2026-05-12T19:53:24Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4421is.xml"
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
      "title": "NOPE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-09T05:23:46Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NOPE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Oil Profits for Enemies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Countering America's Adversaries Through Sanctions Act to expand review by Congress of actions relating to sanctions imposed with respect to the Russian Federation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:37Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7081
- Title: Sara’s Law and the Preventing Unfair Sentencing Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7081
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-02-10T09:05:27Z
- Update date including text: 2026-02-10T09:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7081",
    "number": "7081",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000821",
        "district": "4",
        "firstName": "Bruce",
        "fullName": "Rep. Westerman, Bruce [R-AR-4]",
        "lastName": "Westerman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Sara\u2019s Law and the Preventing Unfair Sentencing Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:27Z",
    "updateDateIncludingText": "2026-02-10T09:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "GA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "MO"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MI"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7081ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7081\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Westerman (for himself, Ms. Kamlager-Dove , Mr. Carter of Georgia , Mrs. Wagner , Mr. Valadao , Ms. Dean of Pennsylvania , Ms. Ross , and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the court to depart from a statutory minimum in the case of a juvenile offender, youthful victim offender, and certain other minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sara\u2019s Law and the Preventing Unfair Sentencing Act of 2026 .\n#### 2. Sentencing youthful victim offenders who have been trafficked, abused, or assaulted\n##### (a) Sentencing youthful victim offenders\n**(1) In general**\nSection 3553 of title 18, United States Code, is amended by adding at the end the following:\n(h) Sentencing youthful victim offenders (1) Statutory minimums In the case of a youthful victim offender, the court shall have the authority to impose a sentence that is below a level established by statute as a minimum sentence so as to consider the effect of trauma on the offender\u2019s conduct. (2) Suspension of sentence In the case of a youthful victim offender, the court shall have the authority to suspend any portion of an imposed sentence. (3) Youthful victim offender defined In this subsection, the term youthful victim offender means an individual who\u2014 (A) has not attained the age of 18; and (B) has been convicted of a violent offense against a person who the court finds, by clear and convincing evidence, engaged in conduct against such individual, not earlier than 1 year before such violent offense, that is an offense under section 1591 or an offense under chapter 71, 109A, 110, or 117. .\n**(2) Application**\nThe amendments made by this section shall apply only to a conviction entered on or after the date of the enactment of this Act.\n##### (b) Directive to sentencing commission\nPursuant to its authority under section 994(p) of title 28, United States Code, and in accordance with this section, the United States Sentencing Commission shall review and amend, if appropriate, its guidelines and its policy statements with respect to youthful victim offenders (as such term is defined in section 3553 of title 18, United States Code) to ensure that the guidelines and policy statements are consistent with the amendments made by subsection (a).",
      "versionDate": "2026-01-14",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-05T19:13:00Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7081ih.xml"
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
      "title": "Sara\u2019s Law and the Preventing Unfair Sentencing Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sara\u2019s Law and the Preventing Unfair Sentencing Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the court to depart from a statutory minimum in the case of a juvenile offender, youthful victim offender, and certain other minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:58Z"
    }
  ]
}
```

# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5649
- Title: Judicial Accountability for Public Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5649
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-12-16T09:05:33Z
- Update date including text: 2025-12-16T09:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5649",
    "number": "5649",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Judicial Accountability for Public Safety Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:33Z",
    "updateDateIncludingText": "2025-12-16T09:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:06:20Z",
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "AK"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5649ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5649\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Moore of North Carolina introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for civil liability in the case of any judicial officer who acts with intentional disregard for public safety or gross negligence in a bond determination or sentencing decision.\n#### 1. Short title\nThis Act may be cited as the Judicial Accountability for Public Safety Act of 2025 .\n#### 2. Civil Liability\n##### (a) Cause of action\nAny person who establishes by clear and convincing evidence that such person was injured by any action taken, with intentional disregard for public safety or with gross negligence, by a judicial officer in a bond determination or sentencing hearing may obtain, in a civil action, such relief as the court may determine appropriate, which may include punitive damages.\n##### (b) Rule of construction\nThis Act may not be construed to apply to a judicial act taken in good faith or within the scope of ordinary judicial discretion.\n##### (c) Limitation on immunity\nAny immunity otherwise applicable to such a judicial officer under Federal or State law may not be asserted in a civil action under this section.\n#### 3. Definitions\nFor purposes of this Act:\n**(1)**\nThe term judicial officer means\u2014\n**(A)**\nany United States district judge, magistrate judge, bankruptcy judge, or other Federal judicial officer; and\n**(B)**\nany State or local judge or magistrate,\nacting in a criminal proceeding.\n**(2)**\nThe term intentional disregard for public safety means an intentional act or omission that ignores or overrides evidence, statutory mandates, or clear risks to community safety in the exercise of bond or sentencing discretion.\n**(3)**\nThe term bond determination includes any judicial order regarding bail, pretrial release, or conditions of release.\n**(4)**\nThe term sentencing decision includes any judicial order, issued upon conviction, that imposes\u2014\n**(A)**\na term of imprisonment, probation, parole, supervised release, or involuntary commitment;\n**(B)**\nany conditions on release;\n**(C)**\nforfeiture; or\n**(D)**\nany other criminal sanction.",
      "versionDate": "2025-09-30",
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
        "name": "Law",
        "updateDate": "2025-12-11T15:40:16Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5649ih.xml"
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
      "title": "Judicial Accountability for Public Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Judicial Accountability for Public Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for civil liability in the case of any judicial officer who acts with intentional disregard for public safety or gross negligence in a bond determination or sentencing decision.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:15Z"
    }
  ]
}
```

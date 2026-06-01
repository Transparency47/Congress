# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/223?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/223
- Title: Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 223
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/223",
    "number": "223",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T20:03:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MO"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s223is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 223\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Lee (for himself, Mr. Wicker , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to repeal prohibitions relating to freedom of access to clinic entrances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025 .\n#### 2. Repeal of prohibitions relating to freedom of access to clinic entrances\n##### (a) In general\nSection 248 of title 18, United States Code, is repealed.\n##### (b) Clerical amendment\nThe table of sections for chapter 13 of title 18, United States Code, is amended by striking the item relating to section 248.\n##### (c) Applicability\nThe repeal made in subsection (a) shall apply to any prosecution of an offense that is pending on, or commenced on or after, the date of enactment of this Act.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-06-10",
        "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 13 - 10."
      },
      "number": "589",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FACE Act Repeal Act of 2025",
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
            "name": "Assault and harassment offenses",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Family planning and birth control",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-03-21T19:24:20Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-03-21T19:24:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-01T16:16:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s223",
          "measure-number": "223",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s223v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025</strong></p><p>This bill repeals provisions of federal criminal law that prohibit conduct intended to injure, intimidate, or interfere with persons who are seeking to (1)\u00a0obtain or provide reproductive health services, or (2) exercise their right of religious freedom at a place of religious worship.</p>"
        },
        "title": "Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s223.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025</strong></p><p>This bill repeals provisions of federal criminal law that prohibit conduct intended to injure, intimidate, or interfere with persons who are seeking to (1)\u00a0obtain or provide reproductive health services, or (2) exercise their right of religious freedom at a place of religious worship.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s223"
    },
    "title": "Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025</strong></p><p>This bill repeals provisions of federal criminal law that prohibit conduct intended to injure, intimidate, or interfere with persons who are seeking to (1)\u00a0obtain or provide reproductive health services, or (2) exercise their right of religious freedom at a place of religious worship.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s223"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s223is.xml"
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
      "title": "Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring the First Amendment and Right to Peaceful Civil Disobedience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to repeal prohibitions relating to freedom of access to clinic entrances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:27Z"
    }
  ]
}
```

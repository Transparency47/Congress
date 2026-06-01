# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3614?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3614
- Title: Internet Application I.D. Act
- Congress: 119
- Bill type: S
- Bill number: 3614
- Origin chamber: Senate
- Introduced date: 2026-01-12
- Update date: 2026-02-10T00:10:02Z
- Update date including text: 2026-02-10T00:10:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in Senate
- 2026-01-12 - IntroReferral: Introduced in Senate
- 2026-01-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-01-12: Introduced in Senate

## Actions

- 2026-01-12 - IntroReferral: Introduced in Senate
- 2026-01-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3614",
    "number": "3614",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Internet Application I.D. Act",
    "type": "S",
    "updateDate": "2026-02-10T00:10:02Z",
    "updateDateIncludingText": "2026-02-10T00:10:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T23:06:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sponsorshipDate": "2026-01-12",
      "state": "IA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3614is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3614\nIN THE SENATE OF THE UNITED STATES\nJanuary 12, 2026 Ms. Cortez Masto (for herself, Mr. Grassley , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require any person that maintains an internet website or that sells or distributes a mobile application that is owned, wholly or partially, by a foreign adversary country, by a foreign adversary country-owned-entity, or by a non-state-owned entity located in a foreign adversary country, or that stores and maintains information collected from such website or application in a foreign adversary country, to disclose that fact to any individual who downloads or otherwise uses such website or application.\n#### 1. Short title\nThis Act may be cited as the Internet Application Integrity and Disclosure Act or the Internet Application I.D. Act .\n#### 2. Disclosure requirements relating to ownership, storage, and maintenance of information in a foreign adversary country\n##### (a) Disclosure requirements\nBeginning 1 year after the date of enactment of this Act, any person who owns, controls, or distributes access to a covered service shall clearly and conspicuously disclose to any individual who downloads or otherwise uses the covered service the following:\n**(1)**\nWhether the covered service is owned, wholly or partially, by a foreign adversary country, by a foreign adversary country-owned entity, or by a non-state-owned entity located in a foreign adversary country.\n**(2)**\nWhether information collected from the covered service is stored and maintained in a foreign adversary country.\n**(3)**\nWhether a foreign adversary country or a foreign adversary country-owned entity has access to such information.\n##### (b) False information\nIt shall be unlawful for any person to knowingly disclose false information under this section.\n##### (c) Definitions\nIn this section:\n**(1) Covered service defined**\nThe term covered service means an internet website or a mobile application that\u2014\n**(A)**\nis owned, wholly or partially, by a foreign adversary country, by a foreign adversary country-owned entity, or by a non-state-owned entity located in a foreign adversary country; or\n**(B)**\nstores and maintains information collected from such website or application in a foreign adversary country.\n**(2) Foreign adversary country**\nThe term foreign adversary country means a country specified in section 4872(f)(2) of title 10, United States Code.\n**(3) Individual**\nThe term individual means a natural person residing in the United States.\n**(4) Non-state-owned entity located in a foreign adversary country**\nThe term non-state-owned entity located in a foreign adversary country means an entity that is\u2014\n**(A)**\ncontrolled (as such term is defined in section 800.208 of title 31, Code of Federal Regulations, or a successor regulation) by any governmental organization of a foreign adversary country; or\n**(B)**\norganized under the laws of a foreign adversary country.\n#### 3. Enforcement\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act is a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Federal Trade Commission\n**(1) In general**\nThe Federal Trade Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person that violates this Act shall be subject to the penalties, and entitled to the privileges and immunities, provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Federal Trade Commission under any other provision of law.",
      "versionDate": "2026-01-12",
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
        "updateDate": "2026-02-10T00:10:02Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3614is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require any person that maintains an internet website or that sells or distributes a mobile application that is owned, wholly or partially, by a foreign adversary country, by a foreign adversary country-owned-entity, or by a non-state-owned entity located in a foreign adversary country, or that stores and maintains information collected from such website or application in a foreign adversary country, to disclose that fact to any individual who downloads or otherwise uses such website or application.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:39Z"
    },
    {
      "title": "Internet Application I.D. Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Internet Application I.D. Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Internet Application Integrity and Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```

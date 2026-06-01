# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2687?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2687
- Title: CLEAN DC Act
- Congress: 119
- Bill type: S
- Bill number: 2687
- Origin chamber: Senate
- Introduced date: 2025-09-02
- Update date: 2026-04-06T16:11:01Z
- Update date including text: 2026-04-06T16:11:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-02: Introduced in Senate
- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-02: Introduced in Senate

## Actions

- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2687",
    "number": "2687",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CLEAN DC Act",
    "type": "S",
    "updateDate": "2026-04-06T16:11:01Z",
    "updateDateIncludingText": "2026-04-06T16:11:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T20:53:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "ID"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "UT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AL"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MS"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MO"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "SC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2687is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2687\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Mr. Cruz (for himself, Mr. Risch , Mr. Lee , Mr. Tuberville , Mr. Budd , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo repeal the Comprehensive Policing and Justice Reform Amendment Act of 2022 enacted by the District of Columbia Council.\n#### 1. Short title\nThis Act may be cited as the Common-Sense Law Enforcement and Accountability Now in DC Act or the CLEAN DC Act .\n#### 2. Repeal of Comprehensive Policing and Justice Reform Amendment Act of 2022\nThe Comprehensive Policing and Justice Reform Amendment Act of 2022 (D.C. Law 24\u2013345) is repealed, and any provision of law amended or repealed by that Act shall be restored or revived as if that Act had not been enacted into law.",
      "versionDate": "2025-09-02",
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
        "actionDate": "2025-11-20",
        "text": "Received in the Senate."
      },
      "number": "5107",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Common-Sense Law Enforcement and Accountability Now in DC Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-23T18:19:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-02",
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
          "measure-id": "id119s2687",
          "measure-number": "2687",
          "measure-type": "s",
          "orig-publish-date": "2025-09-02",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2687v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-09-02",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Common-Sense Law Enforcement and Accountability Now in DC Act or the CLEAN DC Act</strong></p><p>This bill repeals the Comprehensive Policing and Justice Reform Amendment Act of 2022, enacted by the Council of the District of Columbia.</p><p>Any provision of law amended or repealed by that act is restored or revived as if it had not been enacted.</p><p>(The act sets forth a variety of measures that focus on policing, including measures prohibiting the use of certain neck restraints by law enforcement officers, requiring additional procedures related to body-worn cameras, and expanding access to police disciplinary records.)</p>"
        },
        "title": "CLEAN DC Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2687.xml",
    "summary": {
      "actionDate": "2025-09-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Common-Sense Law Enforcement and Accountability Now in DC Act or the CLEAN DC Act</strong></p><p>This bill repeals the Comprehensive Policing and Justice Reform Amendment Act of 2022, enacted by the Council of the District of Columbia.</p><p>Any provision of law amended or repealed by that act is restored or revived as if it had not been enacted.</p><p>(The act sets forth a variety of measures that focus on policing, including measures prohibiting the use of certain neck restraints by law enforcement officers, requiring additional procedures related to body-worn cameras, and expanding access to police disciplinary records.)</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2687"
    },
    "title": "CLEAN DC Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Common-Sense Law Enforcement and Accountability Now in DC Act or the CLEAN DC Act</strong></p><p>This bill repeals the Comprehensive Policing and Justice Reform Amendment Act of 2022, enacted by the Council of the District of Columbia.</p><p>Any provision of law amended or repealed by that act is restored or revived as if it had not been enacted.</p><p>(The act sets forth a variety of measures that focus on policing, including measures prohibiting the use of certain neck restraints by law enforcement officers, requiring additional procedures related to body-worn cameras, and expanding access to police disciplinary records.)</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2687"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2687is.xml"
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
      "title": "CLEAN DC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLEAN DC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Common-Sense Law Enforcement and Accountability Now in DC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the Comprehensive Policing and Justice Reform Amendment Act of 2022 enacted by the District of Columbia Council.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:21Z"
    }
  ]
}
```

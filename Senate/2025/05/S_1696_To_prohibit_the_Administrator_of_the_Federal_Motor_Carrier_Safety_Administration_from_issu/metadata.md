# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1696?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1696
- Title: DRIVE Act
- Congress: 119
- Bill type: S
- Bill number: 1696
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-09-17T11:03:17Z
- Update date including text: 2025-09-17T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1696",
    "number": "1696",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "DRIVE Act",
    "type": "S",
    "updateDate": "2025-09-17T11:03:17Z",
    "updateDateIncludingText": "2025-09-17T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T19:14:53Z",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "ND"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "UT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "ID"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "OH"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1696is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1696\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Daines (for himself, Ms. Ernst , Mr. Cramer , Mr. Sheehy , Mr. Lee , Mr. Budd , Mr. Risch , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the Administrator of the Federal Motor Carrier Safety Administration from issuing a rule or promulgating a regulation requiring certain commercial motor vehicles to be equipped with speed limiting devices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deregulating Restrictions on Interstate Vehicles and Eighteen-wheelers Act or the DRIVE Act .\n#### 2. Prohibition on requiring speed limiting devices\nNotwithstanding any other provision of law, the Administrator of the Federal Motor Carrier Safety Administration may not issue any rule or promulgate any regulation to require a commercial motor vehicle (as defined in section 390.5 of title 49, Code of Federal Regulations (or a successor regulation)) to be equipped with a speed limiting device set to a maximum speed.",
      "versionDate": "2025-05-08",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-28T17:22:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119s1696",
          "measure-number": "1696",
          "measure-type": "s",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1696v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Deregulating Restrictions on Interstate Vehicles and Eighteen-wheelers Act or the DRIVE Act</strong></p><p>This bill prohibits the Federal Motor Carrier Safety Administration (FMCSA) from issuing any rule or regulation to require a commercial motor vehicle to be equipped with a speed limiting device set to a maximum speed.\u00a0The\u00a0FMCSA issued an advance notice of supplemental proposed rulemaking on this subject on May 4, 2022.</p><p>A commercial motor vehicle includes a vehicle operating in interstate commerce that\u00a0(1) has a gross vehicle weight of 10,001 pounds or more, (2) is designed or used to transport more than 8 passengers\u00a0for compensation, (3) is designed or used to transport more than 15 passengers and is not used to transport passengers for compensation, or (4) is used to transport certain quantities of hazardous materials.</p>"
        },
        "title": "DRIVE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1696.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Deregulating Restrictions on Interstate Vehicles and Eighteen-wheelers Act or the DRIVE Act</strong></p><p>This bill prohibits the Federal Motor Carrier Safety Administration (FMCSA) from issuing any rule or regulation to require a commercial motor vehicle to be equipped with a speed limiting device set to a maximum speed.\u00a0The\u00a0FMCSA issued an advance notice of supplemental proposed rulemaking on this subject on May 4, 2022.</p><p>A commercial motor vehicle includes a vehicle operating in interstate commerce that\u00a0(1) has a gross vehicle weight of 10,001 pounds or more, (2) is designed or used to transport more than 8 passengers\u00a0for compensation, (3) is designed or used to transport more than 15 passengers and is not used to transport passengers for compensation, or (4) is used to transport certain quantities of hazardous materials.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119s1696"
    },
    "title": "DRIVE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Deregulating Restrictions on Interstate Vehicles and Eighteen-wheelers Act or the DRIVE Act</strong></p><p>This bill prohibits the Federal Motor Carrier Safety Administration (FMCSA) from issuing any rule or regulation to require a commercial motor vehicle to be equipped with a speed limiting device set to a maximum speed.\u00a0The\u00a0FMCSA issued an advance notice of supplemental proposed rulemaking on this subject on May 4, 2022.</p><p>A commercial motor vehicle includes a vehicle operating in interstate commerce that\u00a0(1) has a gross vehicle weight of 10,001 pounds or more, (2) is designed or used to transport more than 8 passengers\u00a0for compensation, (3) is designed or used to transport more than 15 passengers and is not used to transport passengers for compensation, or (4) is used to transport certain quantities of hazardous materials.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119s1696"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1696is.xml"
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
      "title": "DRIVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DRIVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deregulating Restrictions on Interstate Vehicles and Eighteen-wheelers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Administrator of the Federal Motor Carrier Safety Administration from issuing a rule or promulgating a regulation requiring certain commercial motor vehicles to be equipped with speed limiting devices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:38Z"
    }
  ]
}
```
